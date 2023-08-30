import smtplib
from email.mime.image import MIMEImage
import imghdr


gmail_user = 'akantariktunahan@gmail.com'
gmail_password = 'ottvneegwkmzhpdu'

sent_from = gmail_user
to = ['akantariktunahan@gmail.com']
subject = 'evinize hirsiz girdi'
body = 'hirsiz '

# create an email message object

  
# open image as a binary file and read the contents
with open('/home/tarikakan/Desktop/age-gender-detection/ornek.jpg', 'rb') as file:
   image_data = file.read()


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text, image_data)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

    