import os
from email.message import EmailMessage
import ssl
import smtplib
import time
from keep_alive import keep_alive

sender="Sender"
password=os.environ.get("PASS")

reciver='reciver'
# reciver='dnotascam@gmail.com'


subject="PYTHON REMINDER BEBE"
body='''Hey,
Read Python 
Hugs 🫂  
Thats all  
- Eeman Majumder AI '''

em = EmailMessage()
em['From']=sender
em['To']=reciver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

while True:
    import time
    time=time.strftime("%H:%M:%S", time.localtime())
    # print(time)
    sus="yes" if time == '18:00:00' else "No"
    
    if sus=="yes":
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(sender,password)
            smtp.sendmail(sender,reciver,em.as_string())
            print('sent')
            break
    else :
        print('rest')
