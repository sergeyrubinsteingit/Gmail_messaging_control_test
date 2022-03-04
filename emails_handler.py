# -*- coding: UTF-8 -*-


email_host = "@gmail.com"
receiver_email = "rubiserg.aidock.amy.test@gmail.com"
recipient_password = "rubisergAutomation322"
smtp_server = "imap.gmail.com"


def emails_handler():
    from organize_messages import organize_messages
    from  all_imports_amy import time, imaplib, email, traceback

    try:
        mail = imaplib.IMAP4_SSL(smtp_server)
        mail.login(receiver_email, recipient_password)
        mail.select('inbox')

        get_data = mail.search(None, 'ALL')
        mail_ids = get_data[1]
        id_list = mail_ids[0].split()
        nmb_of_msgs: int = id_list.__len__()
        if nmb_of_msgs > 4:
            organize_messages(nmb_of_msgs)
            # time.sleep(5)
        else:
            return print('Less than 5 messages in the inbox.')

        if not id_list.__len__() < 4: # Checks there are no less than 5 msgs in inbox.
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])
            print("id_list.__len__() = " + str(id_list.__len__()))
            time.sleep(5)
            for i in range(latest_email_id,first_email_id-1, -1):
                get_data = mail.fetch(str(i), '(RFC822)')
                for response_part in get_data:
                    mail_search_array = response_part[0]
                    if isinstance(mail_search_array, tuple):
                        get_msg = email.message_from_string(str(mail_search_array[1], 'utf-8'))
                        email_subject = get_msg['subject']    # email_from = get_msg['from']
                        # if str(email_subject)[:2] == "10":
                        #     print('Subject : ' + email_subject + '\n')

    except Exception as e:
        traceback.print_exc()
        print(str(e))

emails_handler()
