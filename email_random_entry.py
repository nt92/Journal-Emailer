import sqlite3
import smtplib

FROM_ADDRESS = 'nthota.testing@gmail.com'
TO_ADDRESS = 'nthota92@gmail.com'
PASSWORD = 'PASSWORD'

conn = sqlite3.connect('entries.db')
cursor = conn.cursor()

# fetch random entry object
cursor.execute("SELECT * FROM entries ORDER BY RANDOM()")
date = cursor.fetchone()[0]
entry = cursor.fetchone()[1]

# set up email server
server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
server.ehlo()
server.starttls()
server.login(FROM_ADDRESS, PASSWORD)

# create message
message = (date + '\n' + entry).encode('utf-8')

server.sendmail(FROM_ADDRESS, TO_ADDRESS, message)
print(message)
del message

server.quit()
