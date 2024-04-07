import os
import smtplib
import ssl
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv 


PORT = 465
EMAIL_SERVER = "smtp.gmail.com"

# Load the env variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
env_vars = current_dir / ".env"
load_dotenv(env_vars)

# Read env variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

# Check if variables are loaded correctly
if sender_email is None or password_email is None:
    print("Error: EMAIL or PASSWORD environment variables are not set.")
    exit(1)


def send_email(subject,recevier_email, name, course_name, joining_date, last_date,):
    message = MIMEMultipart("alternative")
    message['From'] = formataddr(("ConnectWorld Technologies.",sender_email))
    message['To'] = recevier_email
    message['Subject'] = subject
    html = html_content=f"""\
    <html>    
        <body>
            <p>Dear {name.upper()},</p>
            <p>We are thrilled to offer you an internship opportunity as a<strong> {course_name}</strong> intern at ConnectWorld Technologies. We were impressed with your skills and qualifications and believed you would be a valuable addition to our team.</p>
            <p>Please reply to this mail for confirmation.</p>
            <p>Check Your Offer Letter and {course_name} Task attached to this email.</p>
            <p>{course_name} Task list: <a href="Task_Link">Click here</a></p>
            <p><strong>Internship Details:</strong></p>
            <ul>
                <li>Position: {course_name} Intern</li>
                <li>Duration: {joining_date} to {last_date} (Last Date of Task Submission)</li>
                <li>Weekly Hours: Flexible hours per week</li>
                <li>Location: Remote Work</li>
            </ul>
            <p>Link for Submission of Tasks: <a href="https://forms.gle/CW9XomY7P89xxpAq7">Task Submission Form</a></p>
            <p>Some Essential points you have to remember during this internship tenure-</p>
            <ol>
                <li>Update your LinkedIn Profile and share all your achievements (Offer Letter / Internship Completion Certificate) which you got from us and tag, @ConnectWorld Technologies also use #connectworld #ConnectWorldTech #ConnectWorldTechnologies</li>
                <li>If your project/code is found copied, your internship will be terminated and you will be banned from further opportunities from us.</li>
                <li>Share a video of the completed task on LinkedIn and tag @ConnectWorld Technologies also use #connectworld #ConnectworldTech #ConnectWorldTechnologies</li>
            </ol>
            <p>After completing the first month of your internship, you will be required to go through an interview process. If you successfully pass the interview, you will be eligible for a performance-based stipend ranging from 10,000 to 15,000 rupees. This stipend will be a reflection of your dedication, skills, and overall performance during your internship.</p>
            <p>At the end of the internship, if you wish to apply for the interview process, there will be a registration cost of 249/-. This fee covers the administrative expenses associated with the interview process, ensuring a fair and structured evaluation of candidates. However, if you choose not to participate in the interview process, you have the option to pay 149/- and obtain your Internship Completion Letter and Recommendation Letter.</p>
            <p>We are excited to have you join our team as a {course_name} Intern and look forward to working with you.</p>
            <p>Thank you for considering this internship opportunity with ConnectWorld Technologies.</p>
            <p>Join us through:</p>
            <p>LinkedIn: <a href="https://www.linkedin.com/company/cognifyz-techonologies/">ConnectWorld Technologies</a></p>
            <p><strong>If any Query?</strong></p>
            <p>Please feel free to contact us at -</p>
            <p>Email: <a href="mailto:cognifyztechnologies@gmail.com">connectworldtechnologies@gmail.com</a> Website: <a href="https://www.cognifyz.com">www.connectworldtech.com</a></p>
            <p>Regards,<br>ConnectWorld Technologies</p>
        </body>
    </html>
    """
    # Turn these into html MIMEText objects
    part1 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(EMAIL_SERVER, PORT, context=context) as server:
        server.login(sender_email,password_email)
        server.sendmail(sender_email,recevier_email,message.as_string())

if __name__=='__main__':
    send_email(
        name = "kalai",
        recevier_email = "kalai.pvs@outlook.com",
        course_name= "Python Programming",
        joining_date = datetime.strptime("12/04/2024", "%d/%m/%Y").strftime("%d,%b %Y"),
        last_date = datetime.strptime("12/05/2024", "%d/%m/%Y").strftime("%d,%b %Y")
    )


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    