import imaplib
import re

def read_email_for_login():
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

    # Logout from your Outlook account
    imap.logout()

    return data




def regex_and_find_link(link):
    file_content_str = link.replace("\n", "").replace("\r", "").replace("3D", "")
    # print(file_content_str)
    regex_pattern = "https://medium\.com/m/callback/email\?token=(\w+)=&operation=login&state=medium"

    result = re.search(regex_pattern, file_content_str)

    # print(f"result : {result.group()}")

    result = result.group()

    counter = 0
    result_str = ""
    for char in result:
        if char == "=":
            if counter == 1:
                counter += 1
                continue
            counter += 1
        result_str += char
        
    print(f"result : {result_str}")
