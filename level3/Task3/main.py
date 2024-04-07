import os
from datetime import date,timedelta
import pandas as pd
from Automate_Emails import send_email
from pathlib import Path
from dotenv import load_dotenv 


# Load the env variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
env_vars = current_dir / ".env"
load_dotenv(env_vars)

# Read env variables
SHEET_NAME = os.getenv("SHEET_NAME")
SHEET_ID = os.getenv("SHEET_ID")

#Googlesheets url
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"



def load_df(url):
    
    df = pd.read_csv(url)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df["joining_date"] = pd.to_datetime(df["joining_date"], format="%d %B %Y")
    df["last_date"] = df["joining_date"] + pd.DateOffset(months=1)  # Calculate last date one month after joining date
    return df

def query_date_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if(present == row["joining_date"].date() + timedelta(days=1)) and (row["mail_send"].lower() == "no")and (row["course_completed_status"].lower() == "no"):
            send_email(
                subject =f"ConnectWorld Technologies:Congratulations / Internship Offer Letter for {row['course_name'].upper()}",
                name = row["name"],
                recevier_email= row["email"],
                course_name= row["course_name"],
                joining_date = row["joining_date"].strftime("%d,%b %Y"),
                last_date = row["last_date"].strftime("%d,%b %Y")                                
            )
            email_counter += 1
            
    return f"total mails sent{email_counter}"

df=load_df(URL)
result=query_date_and_send_emails(df)
print(result)