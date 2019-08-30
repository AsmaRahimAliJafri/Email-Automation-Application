import pandas as pd


# creating a pandas alias as pd
# creating a pandas object as xl_file
csv_file = pd.read_csv('swh2.csv')

email_column = csv_file[['CONTACT']]

# print(email_column)
email_body = "Hello"+"\n\n"+"I am an undergraduate of NED University, applying as a software engineering intern position for your company."+"\n\n"+"I have attached my resume and cover letter to this email.\nPlease feel free to reach out to me if you have questions or information, through email or via the phone number below."+"\n\n"+"Regards,\nAsma Rahim\n0336-2908687"

print(email_body)
#prints a series, another pandas data container
just_emails_series = csv_file['CONTACT']
print(just_emails_series)

#prints a dataframe with selected rows

# test_emails = csv_file.iloc[10, 2]
# print(len(test_emails))