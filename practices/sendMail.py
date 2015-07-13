import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendGmailSmtp(gUser, gPwd, to, subject, msg):
	
	mailFormat = MIMEMultipart()
	mailFormat['From'] = gUser
	mailFormat['To'] = to
	mailFormat['Subject'] = subject
	mailFormat.attach(MIMEText(msg))
	
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(gUser, gPwd)
		server.sendmail(gUser, to, mailFormat.as_string())
		print('successfully sent the mail')
	except:
		print('failed to send mail')
	finally:
		server.close()
		
user = 'user'
pwd = 'password'
to = 'user@gmail.com'
subject = 'This is a test mail again'
msg = 'as title'
sendGmailSmtp(user, pwd, to, subject, msg)