import smtplib
HOST ="smtp.mydomain.com"
SUBJECT ="Test email from Python"
TO = "asarpita17@gmail.com"
FROM = "aayushiraj4050@gmail.com"
text = "blah blah blah "
BODY = "\r\n".join((
    f"From:{FROM}",
    f"To:{TO}",
    f"Subject:{SUBJECT}",
    " ",
    text)
)
server = smtplib.SMTP(HOST)
server.sendmail(FROM,[TO],BODY)
server.quit()
