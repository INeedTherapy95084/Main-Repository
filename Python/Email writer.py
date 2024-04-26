import smtplib
import os
os.system('cls')

u_email = input("Please enter your Gmail address: ")
os.system('cls')
reciver_email = input("Please enter the reciving Gmail address: ")
os.system('cls')
subject = input("Please enter the Eamil subject: ")
os.system('cls')
body = input("Please enter the Email body: \n")
os.system('cls')

text = f"Subject: {subject}\n\n{body}"

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(u_email, 'akfp jfdf aztb zbuk')

    server.sendmail(u_email, reciver_email, text)
except:
    print("ERROR_PLEASE_TRY_AGAIN_LATER_\n")
    quit()

print (f"Email has been sent to {reciver_email}")