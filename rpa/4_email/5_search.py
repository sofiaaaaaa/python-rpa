from imap_tools import MailBox
from imap_tools.utils import EmailAddress
from account import * 

# logout 구문 없이 사용 가능함
with MailBox("imap.gmil.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailBox: 
    # for msg in mailbox.fetch(): # 전체 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailBox.fetch('(UNSEEN)'): # 읽지 않은 메일 가져오기 
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # for msg in mailBox.fetch('(FROM abc@abc.com)', limit=3, reverse=True): # 특정인이 보낸 메일 
    #      print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailBox.fetch('(TEXT "test mail")', limit=3, reverse=True): # 띄어쓰기를 포함하여 어떤 글자를 포함하는 메일 (제목, 본문)
    #      print("[{}] {}".format(msg.from_, msg.subject))


    # 한글 지원안됨
    for msg in mailBox.fetch('(SUBJECT "test mail")', limit=3, reverse=True): # 띄어쓰기를 포함하여 어떤 글자를 포함하는 메일 (제목)
        print("[{}] {}".format(msg.from_, msg.subject))
   
    
    for msg in mailBox.fetch(limit=5, reverse=True): # 한글은 if문으로 검사 
        if "테스트" in msg.subject: 
            print("[{}] {}".format(msg.from_, msg.subject))


    for msg in mailBox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5): # 특정날짜 이후 메일 가져오기 
        print("[{}] {}".format(msg.from_, msg.subject))

    for msg in mailBox.fetch('(ON 07-Nov-2020)', reverse=True, limit=5): # 특정날짜에 온 메일 가져오기 
        print("[{}] {}".format(msg.from_, msg.subject))
