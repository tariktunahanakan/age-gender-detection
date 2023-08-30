import smtplib
from email.message import EmailMessage
import imghdr
  
email_subject = "Email test from Python"
sender_email_address = "akantariktunahan@gmail.com"
receiver_email_address = "akantariktunahan@gmail.com"
email_smtp = "smtp.gmail.com"
email_password = "ottvneegwkmzhpdu"
  
# create an email message object
message = EmailMessage()

with open('/home/tarikakan/Desktop/age-gender-detection/ornek.jpg', 'rb') as file:
   image_data = file.read()
  
message.set_content("Email from Python with image attachment")
# attach image to email
message.add_attachment(image_data, maintype='image', subtype=imghdr.what(None, image_data))
  

# configure email headers
message['Subject'] = email_subject
message['From'] = sender_email_address
message['To'] = receiver_email_address
    
# set smtp server and port
server = smtplib.SMTP(email_smtp, '587')
# identify this client to the SMTP server
server.ehlo()
# secure the SMTP connection
server.starttls()
  
# login to email account
server.login(sender_email_address, email_password)
# send email
server.send_message(message)
# close connection to server
server.quit()