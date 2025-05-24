import streamlit as st
from cryptography.fernet import Fernet
import hashlib

class SecureDataStorage:
    def __init__(self):
        self.data = {}
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def hash_passkey(self, passkey):
        return hashlib.sha256(passkey.encode()).hexdigest()

    def store_data(self, identifier, text, passkey):
        hashed_pass = self.hash_passkey(passkey)
        encrypted_text = self.fernet.encrypt(text.encode()).decode()
        self.data[identifier] = {
            "encrypted_text": encrypted_text,
            "passkey": hashed_pass
        }

    def retrieve_data(self, identifier, passkey):
        if identifier not in self.data:
            return False, "Identifier not found."

        hashed_pass = self.hash_passkey(passkey)
        if hashed_pass == self.data[identifier]["passkey"]:
            decrypted = self.fernet.decrypt(
                self.data[identifier]["encrypted_text"].encode()
            ).decode()
            return True, decrypted
        else:
            return False, "Invalid passkey."


class AuthManager:
    def __init__(self):
        if "failed_attempts" not in st.session_state:
            st.session_state.failed_attempts = 0
        if "reauthorized" not in st.session_state:
            st.session_state.reauthorized = False

    def increment_failed(self):
        st.session_state.failed_attempts += 1

    def reset_failed(self):
        st.session_state.failed_attempts = 0

    def is_blocked(self):
        return st.session_state.failed_attempts >= 3 and not st.session_state.reauthorized

    def reauthorize(self, username, password):

        return username == "admin" and password == "1234"

class UI:
    def __init__(self, storage: SecureDataStorage, auth: AuthManager):
        self.storage = storage
        self.auth = auth

    def home_page(self):
        st.title("🔐 Secure Data Locker")
        if st.button("📥 Store New Data"):
            st.session_state.page = "insert"
        if st.button("🔓 Retrieve Data"):
            st.session_state.page = "retrieve"

    def insert_data_page(self):
        st.title("📥 Store New Data")
        identifier = st.text_input("Unique Identifier (e.g. your name)")
        text = st.text_area("Enter text to encrypt")
        passkey = st.text_input("Passkey", type="password")
        if st.button("Encrypt and Save"):
            if identifier and text and passkey:
                self.storage.store_data(identifier, text, passkey)
                st.success("Data stored successfully!")
            else:
                st.warning("All fields are required.")

    def retrieve_data_page(self):
        if self.auth.is_blocked():
            st.session_state.page = "login"
            return

        st.title("🔓 Retrieve Data")
        identifier = st.text_input("Your Identifier")
        passkey = st.text_input("Your Passkey", type="password")

        if st.button("Decrypt"):
            success, message = self.storage.retrieve_data(identifier, passkey)
            if success:
                self.auth.reset_failed()
                st.success("Decrypted Data:")
                st.code(message)
            else:
                self.auth.increment_failed()
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"{message}. Attempts left: {remaining}")
                if remaining <= 0:
                    st.warning("Redirecting to login for reauthorization...")
                    st.session_state.page = "login"

    def login_page(self):
        st.title("🔑 Reauthorization Required")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if self.auth.reauthorize(username, password):
                st.session_state.reauthorized = True
                self.auth.reset_failed()
                st.success("Reauthorized. You can now try again.")
                st.session_state.page = "retrieve"
            else:
                st.error("Invalid credentials. Try again.")

def main():
    st.set_page_config(page_title="Secure Locker", page_icon="🔐")
    if "page" not in st.session_state:
        st.session_state.page = "home"

    storage = SecureDataStorage()
    auth = AuthManager()
    ui = UI(storage, auth)

    if st.session_state.page == "home":
        ui.home_page()
    elif st.session_state.page == "insert":
        ui.insert_data_page()
    elif st.session_state.page == "retrieve":
        ui.retrieve_data_page()
    elif st.session_state.page == "login":
        ui.login_page()


if __name__ == "__main__":
    main()


