import os
from collections import Counter
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

totalsformatted = 'These are on %s the iOS versions in use with the number of active devices: \n\n' % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
oslist = []
listdir = os.listdir('c:\\reports')
lastfile = 'c:\\reports\\'+listdir[-1]
report = open(lastfile)
report.readline()
for line in report:
    ios = str(line[24:-2])
    oslist.append(ios)
totals = Counter(oslist)
for versions,numbers in totals.items():
    totalsformatted += " iOS " + versions + " : " + str(numbers) + " devices\n"

print totalsformatted

#Saving the results in a file
filename = 'c:\\reports\\AppleiOSVersions ' + datetime.now().strftime('%Y-%m-%d') + '.txt'
mailtext = open (filename, 'w')
mailtext.write(totalsformatted)
mailtext.close()

#Sending SMTP message
msg = MIMEText(totalsformatted)
me = 'MI.Prod@pwc.com'
you = 'michiel.van.der.bruggen@pwc.com'
msg['Subject'] = 'Apple iOS versions in use'
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP('10.65.90.161')
s.sendmail(me, [you], msg.as_string())
s.quit()

