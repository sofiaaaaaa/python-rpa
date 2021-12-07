import smtplib
from account import * 

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결 수행 확인
    smtp.starttls() # 모든 내용 암호화 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "test mail" # 한글 지원안됨
    body = "mail body" 

    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "aaaaaaa@aaa.com", msg) # 발신자, 수신자, 메세지 


