
Days_In_Year = 365
Hours_In_Day = 24
Minutes_In_Hour = 60
Seconds_In_Minute = 60

def seconds_in_year():
    seconds_in_year = Days_In_Year * Hours_In_Day * Minutes_In_Hour * Seconds_In_Minute
    print(f"There are {seconds_in_year} seconds in a year.")
if __name__ == "__main__":
    seconds_in_year();