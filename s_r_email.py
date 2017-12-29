# smtp is the email sending agreement
# pop/pop3 is the email receiving agreement
from email.mime.text import MIMEText
from email.header import Header
import email
#from email.parser import HeaderParser
from email.utils import parseaddr
from email.header import decode_header
from smtplib import SMTP_SSL
import poplib
# decode Chinese character from windows system
import base64

def send_mail(sender_qq='',pwd='', receiver='',mail_title='',mail_content=''):
	# stmp server of qq mail
	host_server = 'smtp.qq.com'
	# mail sender
	sender_qq_mail = sender_qq+'@qq.com'
	
	#ssl login
	smtp = SMTP_SSL(host_server)
	#set_debuglevel() is for debugging。1: debug mode，0: test mode
	smtp.set_debuglevel(1)
	smtp.ehlo(host_server)
	# login 
	smtp.login(sender_qq, pwd)

	msg = MIMEText(mail_content, "plain", 'utf-8')
	msg["Subject"] = Header(mail_title, 'utf-8')
	msg["From"] = sender_qq_mail
	msg["To"] = receiver
	smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
	smtp.quit()

#def guess_charset(msg):
#	# learn for msg
#	charset = msg.get_charset()
#	if charset is None:
#		content_type = msg.get('Content-Type', '').lower()
#		pos = content_type.find('charset=')
#		if pos >= 0:
#			charset = content_type[pos + 8:].strip()
#	return charset

# decode as charset, usually it is utf-8
def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value

def receive_mail(receiver_qq='', pwd=''):
	host_server = 'pop.qq.com'
	receiver_qq_mail = receiver_qq+'@qq.com'

	pop_conn = poplib.POP3_SSL(host_server)  
	pop_conn.set_debuglevel(1)
	# login	
	pop_conn.user(receiver_qq_mail)  
	pop_conn.pass_(pwd)  

	print('Messages: %s. Size: %s' % pop_conn.stat())
	# get the latest email
	response, listings, octets = pop_conn.list()
#	lines = pop_conn.retr(1)[1]
	print(len(listings))
#	print(listings)
#	print(lines)
#	for i in range(1,len(listings)+1):
	i = len(listings);	
	resp, lines, octe = pop_conn.retr(i)
#	print(lines)
#	print(len(lines))
#	for line in lines: 
#		message = email.message_from_bytes(line)
#		print(message)
	message = email.message_from_bytes(b'\n'.join(lines))
# depend on different mail box
#	message = email.message_from_string('\n'.join(listings[1]))

	for header in ['From', 'To', 'Subject', 'Date']:
		value = message.get(header, '')
		if value:
			if header == 'Subject':
				value = decode_str(value)
			else:
				hdr, addr = parseaddr(value)
				name = decode_str(hdr)
				value = u'%s <%s>' % (name, addr)
		print('%s%s: %s' % ('  ' * 0, header, value))

	for part in message.walk():
		if not part.is_multipart():

			fileName = part.get_filename()
			charset = part.get_content_charset()
#			content = part.get_payload(decode=True)
			
			if fileName:
				h = email.header.Header(fileName)
				dh = email.header.decode_header(h)
				filename = dh[0][0]
#				print(filename)
#				print(dh[0][1])
				filenamestr = bytes.decode(filename)
				if filenamestr[0] == '=':
				# get the encode mode
					s = filename.split(b'?')
					finalname = base64.b64decode(s[3]).decode(bytes.decode(s[1]))
				else:
					finalname = filenamestr
				print(finalname)
				# get email content
#				contentType = part.get_content_type()
				# get attachment				
				data = part.get_payload(decode=True)
				fEx = open(finalname, 'wb')
				fEx.write(data)
				fEx.close()
				
	pop_conn.quit() 
