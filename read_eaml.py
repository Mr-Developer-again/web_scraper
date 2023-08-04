import imaplib
import base64

# IMAP server details for Outlook
imap_server = 'outlook.office365.com'
imap_port = 993

# Your Outlook credentials
username = 'mediumscraper@outlook.com'
password = 'babak13830'

# Connect to the IMAP server
imap = imaplib.IMAP4_SSL(imap_server, imap_port)

# Login to your Outlook account
imap.login(username, password)

# Select the mailbox (in this case, the 'INBOX' mailbox)
imap.select('INBOX')

# Search for all emails in the mailbox
typ, message_numbers = imap.search(None, 'ALL')

# Get a list of email IDs
email_ids = message_numbers[0].split()

# Retrieve the latest email (in this case, the last email)
latest_email_id = email_ids[-1]

# Fetch the email data
typ, data  = imap.fetch(latest_email_id, '(RFC822)')


# The email data is returned as a tuple, where the actual email content is in the second element of the tuple
email_data = data[0][1]
print(f"this is data after fetch ===   {data}")
data1 = base64.b64decode(data[0][1])
# Print the email content
print('Message %s\n%s\n' % (latest_email_id, data1))

# Logout from your Outlook account
imap.logout()
