#lib used to send emails, simple mail transfer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


# importing email addresses
csv_file = pd.read_csv('swh2.csv')
just_emails_series = csv_file['CONTACT']



sender_email = "m"
sender_pass = ""

subject = 'Software Engineering Intern Application'
email_body = "Hello"+"\n\n"+"I am an undergraduate of NED University, applying for the position of a software engineering intern at your company."+"\n\n"+"I have attached my resume and cover letter to this email.\nPlease feel free to reach out to me if you have questions or information, through email or via the phone number below."+"\n\n"+"Regards,\nAsma Rahim\n0336-2908687"
cv = 'Asma_Rahim Ali Jafri_2018_resume.pdf'
coverletter = 'coverLetter_2018.pdf'

x=0
while x <= len(just_emails_series):
    receiver_email = just_emails_series.values[x]
    msg= MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(email_body, 'plain'))

    attach_cv = open(cv, 'rb')
    attach_cover = open(coverletter, 'rb')

    part_cv = MIMEBase('application', 'pdf', Name=cv)
    part_cv.set_payload(attach_cv.read())
    encoders.encode_base64(part_cv)
    part_cv.add_header('Content-Disposition', 'attachment', filename=cv)


    part_cover = MIMEBase('application', 'octet-stream')
    part_cover.set_payload(attach_cover.read())
    encoders.encode_base64(part_cover)
    part_cover.add_header('Content-Disposition', "attachment", filename=coverletter)

    msg.attach(part_cv)
    msg.attach(part_cover)
    text = msg.as_string()

    #specifying the server, email service and port
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #logging into the email acc
    server.login(sender_email, sender_pass)

    x = x+1
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
