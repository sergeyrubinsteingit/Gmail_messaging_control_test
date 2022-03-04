# -*- coding: UTF-8 -*-

recipient_user = 'rubiserg.aidock.amy.test@gmail.com'
recipient_password = 'rubisergAutomation322'


def organize_messages(nmb_of_msgs):
    from delete_mail import delete_mail
    from all_imports_amy import Message, imaplib, email
    imap_url = "imap.gmail.com"
    connection = imaplib.IMAP4_SSL(imap_url)
    connection.login(recipient_user, recipient_password)
    connection.select()
    result, data = connection.uid('search', None, "ALL")
    date_array = []
    email_message: Message
    arranged_mails : list = [] # To sort msgs in it afterwards in order from Low to High
    if result == 'OK':
        for num in data[0].split():
            result, data = connection.uid('fetch', num, '(RFC822)')
            if result == 'OK':
                email_message = email.message_from_bytes(data[0][1])
                date_array.append(email_message['Date']) # Another option for sorting, just for a case.
                delete_msg_by = str(email_message['Subject'])
                arranged_mails.append(delete_msg_by)
    arranged_mails = sorted(arranged_mails)[::-1] # Sorts msgs Low to High
    print(arranged_mails)
    delete_mail(arranged_mails, nmb_of_msgs) # In module [delete_mail]. Fires deleting of the msgs in order
    # from Low to High
    connection.close()
    connection.logout()
