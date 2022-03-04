# -*- coding: UTF-8 -*-


def delete_mail(arranged_mails, nmb_of_msgs):
    from start_test_amy import recipient_email
    from all_imports_amy import imaplib
    password_receiver: str = "rubisergAutomation322"

    imap = imaplib.IMAP4_SSL("imap.gmail.com") # IMAP4 with SSL
    imap.login(recipient_email, password_receiver) # authenticate
    imap.select("INBOX")

    is_offlimit: int = nmb_of_msgs - 4
    if is_offlimit > 0: # That is, if more than 4 msgs are in inbox, do...
        for idx_ in range(0, is_offlimit):
            index_ = arranged_mails[idx_]
            status, messages = imap.search(None, 'SUBJECT \"' + index_ + '\"') # search for specific mails by sender
            messages = messages[0].split() # convert messages to a list of email IDs

            for entry_ in messages:
                imap.store(entry_, '+X-GM-LABELS', '\\Trash')    # moves the mail to Trash
                imap.store(entry_, "+FLAGS", "\\Deleted")    # mark the mail as deleted
                imap.expunge()    # removes the mail from the selected mailbox (here, INBOX)
    imap.close() # close the mailbox
    imap.logout()# logout from the account

    print("Successfully deleted a mail nmb " + str(arranged_mails[0]))






# from imap_tools import MailBox, A
# from start_test_amy import recipient_email
# # recipient_password: str = "rubisergAutomation322"
# with MailBox('imap.gmail.com').login(recipient_email, recipient_password, 'INBOX') as mailbox_:
#     # DELETE messages that contains an index in Header from INBOX folder
#     # noinspection PyTypeChecker
#     mailbox_.delete(mailbox_.fetch(A(body='3607965527')))

