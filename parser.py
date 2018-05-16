#requirements
#pip install mail-parser
#pip install email

from emailtext import *
from email.parser import Parser
import email
import mailparser
parser = Parser()

# Insert Original Email into file: emailtext.py into the  emailtext variable

email2 = parser.parsestr(emailtext)

parsebody = email.message_from_string(emailtext)
body = ""

if parsebody.is_multipart():
    for part in parsebody.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        # skip any text/plain (txt) attachments
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
# not multipart - i.e. plain text, no attachments, keeping fingers crossed
else:
    body = parsebody.get_payload(decode=True)

bodytostring = str(body)

print ("From: \n", email2.get('From'), "\n")
print ("To: \n", email2.get('To'), "\n")
print ("Subject: \n", email2.get('Subject'), "\n")
print ("Body: \n",  bodytostring.split('\\n'))
