# import streamlit as st
# import json
# from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML
# from docx import Document
# import spacy
# import pandas as pd
# import base64
# from datetime import datetime

# # Initialize NLP model for AI suggestions
# nlp = spacy.load("en_core_web_sm")

# # Initialize session state
# if 'resume_data' not in st.session_state:
#     st.session_state.resume_data = {
#         'personal_info': {'name': '', 'email': '', 'phone': '', 'linkedin': '', 'github': '', 'summary': ''},
#         'education': [],
#         'experience': [],
#         'skills': [],
#         'projects': [],
#         'customizations': {'primary_color': '#2962ff', 'secondary_color': '#448aff', 'font_family': 'Arial'}
#     }

# # Template loader
# env = Environment(loader=FileSystemLoader('templates'))

# # AI Suggestions functions
# def analyze_job_description(job_text):
#     doc = nlp(job_text)
#     entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT', 'TECH']]
#     nouns = [token.text for token in doc if token.pos_ == 'NOUN']
#     return list(set(entities + nouns))

# # PDF generation
# def generate_pdf(html_content):
#     HTML(string=html_content).write_pdf("resume.pdf")
#     with open("resume.pdf", "rb") as f:
#         pdf_bytes = f.read()
#     return pdf_bytes

# # DOCX generation
# def generate_docx(html_content):
#     doc = Document()
#     doc.add_heading('Resume', 0)
#     # Add more content parsing from HTML here
#     doc.save("resume.docx")
#     with open("resume.docx", "rb") as f:
#         docx_bytes = f.read()
#     return docx_bytes

# # Template 1: Modern
# def render_template_1(data):
#     template = env.get_template('template1.html')
#     return template.render(data=data)

# # Template 2: Professional
# def render_template_2(data):
#     template = env.get_template('template2.html')
#     return template.render(data=data)

# # Main app
# def main():
#     st.set_page_config(page_title="Resume Builder", page_icon="📄", layout="wide")

#     # Sidebar
#     with st.sidebar:
#         st.header("Settings")
#         template_choice = st.selectbox("Choose Template", ["Modern", "Professional"])
#         primary_color = st.color_picker("Primary Color", value=st.session_state.resume_data['customizations']['primary_color'])
#         secondary_color = st.color_picker("Secondary Color", value=st.session_state.resume_data['customizations']['secondary_color'])
#         font_family = st.selectbox("Font Family", ["Arial", "Helvetica", "Times New Roman", "Calibri"])
        
#         st.session_state.resume_data['customizations'].update({
#             'primary_color': primary_color,
#             'secondary_color': secondary_color,
#             'font_family': font_family
#         })
        
#         # AI Suggestions
#         st.header("AI Suggestions")
#         job_description = st.text_area("Paste job description for suggestions")
#         if job_description:
#             suggestions = analyze_job_description(job_description)
#             st.write("Suggested Skills:")
#             for skill in suggestions:
#                 if skill not in st.session_state.resume_data['skills']:
#                     st.write(f"- {skill}")

#     # Main form
#     st.title("📄 Modern Resume Builder")
    
#     with st.expander("Personal Information", expanded=True):
#         cols = st.columns(2)
#         st.session_state.resume_data['personal_info']['name'] = cols[0].text_input("Full Name")
#         st.session_state.resume_data['personal_info']['email'] = cols[1].text_input("Email")
#         st.session_state.resume_data['personal_info']['phone'] = cols[0].text_input("Phone")
#         st.session_state.resume_data['personal_info']['linkedin'] = cols[1].text_input("LinkedIn")
#         st.session_state.resume_data['personal_info']['github'] = cols[0].text_input("GitHub")
#         st.session_state.resume_data['personal_info']['summary'] = st.text_area("Professional Summary")

#     with st.expander("Education"):
#         education_df = pd.DataFrame(st.session_state.resume_data['education'])
#         edited_education = st.data_editor(
#             education_df,
#             num_rows="dynamic",
#             column_config={
#                 "institution": "Institution",
#                 "degree": "Degree",
#                 "start_date": {"type": "date", "format": "YYYY-MM-DD"},
#                 "end_date": {"type": "date", "format": "YYYY-MM-DD"},
#                 "gpa": "GPA"
#             }
#         )
#         st.session_state.resume_data['education'] = edited_education.to_dict('records')

#     with st.expander("Work Experience"):
#         experience_df = pd.DataFrame(st.session_state.resume_data['experience'])
#         edited_experience = st.data_editor(
#             experience_df,
#             num_rows="dynamic",
#             column_config={
#                 "company": "Company",
#                 "position": "Position",
#                 "start_date": {"type": "date", "format": "YYYY-MM-DD"},
#                 "end_date": {"type": "date", "format": "YYYY-MM-DD"},
#                 "description": "Description"
#             }
#         )
#         st.session_state.resume_data['experience'] = edited_experience.to_dict('records')

#     with st.expander("Skills"):
#         skills = st.multiselect(
#             "Add Skills",
#             options=["Python", "JavaScript", "Machine Learning", "SQL", "AWS", "Docker", "React", "Data Analysis"],
#             default=st.session_state.resume_data['skills']
#         )
#         st.session_state.resume_data['skills'] = skills

#     # Preview
#     st.header("Resume Preview")
#     if template_choice == "Modern":
#         html_content = render_template_1(st.session_state.resume_data)
#     else:
#         html_content = render_template_2(st.session_state.resume_data)
    
#     st.components.v1.html(html_content, height=1000, scrolling=True)

#     # Export buttons
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         if st.button("Export to PDF"):
#             pdf_bytes = generate_pdf(html_content)
#             st.download_button(
#                 label="Download PDF",
#                 data=pdf_bytes,
#                 file_name="resume.pdf",
#                 mime="application/octet-stream"
#             )
#     with col2:
#         if st.button("Export to DOCX"):
#             docx_bytes = generate_docx(html_content)
#             st.download_button(
#                 label="Download DOCX",
#                 data=docx_bytes,
#                 file_name="resume.docx",
#                 mime="application/octet-stream"
#             )
#     with col3:
#         json_data = json.dumps(st.session_state.resume_data, indent=2)
#         st.download_button(
#             label="Export Data (JSON)",
#             data=json_data,
#             file_name="resume_data.json",
#             mime="application/json"
#         )

#     # Import JSON
#     uploaded_file = st.file_uploader("Import Resume Data (JSON)", type=["json"])
#     if uploaded_file:
#         imported_data = json.load(uploaded_file)
#         st.session_state.resume_data = imported_data
#         st.rerun()

# if __name__ == "__main__":
#     main()