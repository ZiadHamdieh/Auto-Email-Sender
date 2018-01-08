import smtplib
import config

subject = "" 
message = "XXXXXXX"

def send_email(subject, message):
	try:
		# establish secure connection with the server 
		smtp = smtplib.SMTP('smtp.gmail.com', 587)
		# identify yourself to server
		smtp.ehlo()
		# use TLS (Transport Layer Security) to encrypt all smtp commands that follow
		smtp.starttls()
		smtp.ehlo()
		smtp.login(config.SENDER, config.PASSWORD)

		msg = "Subject: {}\n\n{}".format(subject, message)
		smtp.sendmail(config.SENDER, config.RECIPIENT, message)
		smtp.quit()

		print("email send was successful")

	except:
		print("email failed to send")

send_email(subject, message)
