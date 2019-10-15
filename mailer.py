import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from data_access import fetch_name
# me == my email address
# you == recipient's email address

def get_data(to,subject,data):
    me = "e_greet_card@outlook.com"
    you = to
# Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
    text = data
    html=data
    # x=open('./templates/index.html',r)
    # for i in x:
    #     html+=i
# Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

# Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.office365.com', 587)
    s.starttls()
# s.login()
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
    s.login("e_greet_card@outlook.com", "Tesco@123")
    s.sendmail(me, you, msg.as_string())
    s.quit()


# ****************************************************************************************************************


def create_mail(to,subject,data):

    me = "e_greet_card@outlook.com"
    you = to
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you

    # print(to)


    text = "Open this link into your browser to sent a message"+data
    html="<p>Please <a href="+data+">CLICK</a> here to enter the message</p>"

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')


    msg.attach(part1)
    msg.attach(part2)



    s = smtplib.SMTP('smtp.office365.com', 587)
    s.starttls()


    s.login("e_greet_card@outlook.com", "Tesco@123")
    print("SENDING MAIL BE ALERT !!!!!!")
    s.sendmail(me, you, msg.as_string())
    # print(you,data)
    s.quit()

def send_card(to,subject,data,name):
    me = "e_greet_card@outlook.com"
    you = to
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you




    text = "Open this link into your browser to sent a message"+data
    html="""
    <span style="color:#0F0F0F;font-family:Calibri,sans-serif;">Dear {},<br>

<br>

Wishing you health, happiness and love on your special day and always!<br>

Have a wonderful birthday!<br>

Please <a href='{}'>CLICK</a> here to view your birthday card.
<br>
<br>
Regards,<br>

Talent Management </span>
    """.format(name,data)


    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')


    msg.attach(part1)
    msg.attach(part2)



    s = smtplib.SMTP('smtp.office365.com', 587)
    s.starttls()


    s.login("e_greet_card@outlook.com", "Tesco@123")
    s.sendmail(me, you, msg.as_string())
    print(you,data)
    s.quit()
