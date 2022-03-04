# Gmail_messaging_control_test

Environment

Windows 10, Chrome, Gmail Inbox



Objective of the test

Verify:

•	Number of messages in Gmail Inbox is limited ( to 5 items, for the test sake);

•	Each mail sent has got a priority label on;

•	If on coming of new mail the total of messages exceeds the limit (5 items), the oldest message of lower priority is deleted;


Test’s implementation

On running the test from [ start_test_amy.py ]:

•	Asks a sender to set priority to the message, via combo box’s drop menu. If nothing is selected, priority is set to ‘low’;

•	In Subject section of the mail:

  •	At the beginning of the Subject, adds indices formed within a range of 0, 1;
  
  •	After an index, adds a unique ID number;
  
  •	At the end of the Subject adds one of the labels: [ Low ], [ Medium ], [ High ].
  
•	Lists the messages already present in the Inbox;

•	Arranges the list in ascending order so the messages labelled ‘low’ stand first;

•	Deletes the redundant messages in subsequence as in the list, that is the lower priority is thrown out first;

•	When in the Inbox remain 4 messages, sends the new mail.


QA notes

•	Priority: Priority is a sender choice. So the most correct and polite a way to set a priority is to ask a sender for marking hers/his message with. So I suggest to use a combo box;

•	Order of messages in the Inbox:	Unfortunately, Gmail obviously does not allow to order mails by Subject or like. Yet, if it so, it worth to take into account while developing the App. Otherwise the app won’t work properly with this very popular mailer. As a workaround I suggest using the pre-arranged list to delete the old messages ( see Test’s Implementation section above  );

•	Unique ID	In case of this test it is a random hash. It is needed to represent each mail as separate entry. Otherwise they are kept in single stack. It makes the counting of messages more complicated a task. Besides, the unique ID may be useful for another purposes which can pop up while developing the App.

•	Indices: There are 3 indices necessary, while the range between integers 0 and 1 offers only two option. So I converted integers to floats, getting thus: 0.0 for ‘High’, 0.1 for ‘Medium’, 1.0 for ‘Low’. These appear as 2 first characters in Subject, the dot being deleted. So the mail priority can be traced by 2 first character in the Subject string. 

•	As a second option for the app's development, I would suggest to deal off with indices and instead use the Subject labels [ Low ], [ Medium ] and [ High ] in combination with a date/time for identification. It’s easier and more human-friendly an approach.

•	Attached files are ot a token of important message. They presence says us nothing of priority. Let’s a sender to label a message in accordance with her/his preferences.
