import smtplib
from account import * 
from email.message import EmailMessage

# 한글도 가능한 메일보내기 방식 
msg = EmailMessage()
msg["Subject"] = "테스트 메일 제목"
msg["From"] = EMAIL_ADDRESS
# msg["To"] = "nnnnn@nnn.ccc"

# 여러명에게 메일 발송시 콤마로 연결
# msg["To"] = "aaa@aaa.com, bbb@ccc.com"

# 대량 발송시 리스트로 처리 
to_list = ["aaa@bbb.com", "cccc@ccc.com"]
msg["To"] = ", ".join(to_list)

# 참조 
msg["Cc"] = "aaa@ccc.com"

# 비밀참조 
msg["Bcc"] = "cccc@ddd.com"

# 메일 본문 
msg.set_content("본문입니다")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
