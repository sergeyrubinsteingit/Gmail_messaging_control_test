# -*- coding: UTF-8 -*-

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "rubiserg.aidock.e2e.test@gmail.com"
sender_password = "rubisergAutomation222"
recipient_email = "rubiserg.aidock.amy.test@gmail.com"
message_ = """AMY testing"""


def priority_selector(): # The function starts the track: priority_selector() => select_priority_combo module =>
    # back here to: send_mail()
    from select_priority_combo import select_priority_combo
    select_priority_combo()


def send_mail(gener_hash_, selected_priority, priority_lbl): # Waits for select_priority_combo module to return Priority
    # mark string
    from all_imports_amy import time, ssl, smtplib, MIMEText, formataddr, Header
    from emails_handler import emails_handler
    idx_: str = gener_hash_
    print(idx_)
    time.sleep(2)

    context = ssl.create_default_context() # Creates a secure SSL context, otherwise connection is rejected
    server = smtplib.SMTP(smtp_server, port) # Establishes connection
    msg = MIMEText(message_, 'html') # HTML option is just for the case
    msg['Subject'] = str(priority_lbl).replace(".","") + "-" + str(idx_) + " [ " + str(selected_priority) + " ]"
    msg['From'] = formataddr((str(Header("QA will never surrender!", 'utf-8')), sender_email)) # Index as
    # 'From' section
    msg['To'] = "recipient"

    try: # Try to log in to server and send email
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, sender_password)
        emails_handler()
        time.sleep(5)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print ("Successfully sent email")
    except Exception as e:
        print(e) # Print error messages
    finally:
        server.quit()


if __name__ == '__main__':
    priority_selector()