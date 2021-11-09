import smtplib
from account import * 
from email.message import EmailMessage

# 한글도 가능한 메일보내기 방식 
msg = EmailMessage()
msg["Subject"] = "테스트 메일 제목"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "nnnnn@nnn.ccc"

msg.set_content("테스트본문")

# MIMETYPE 미디어타입 MDN web docs 참조해서 각 파일 확장자별로 mime타입 지정해서 전송하기
# 첨부파일
with open("README.md", "rb") as f: 
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name) 

with open("README.pdf", "rb") as f: 
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name) 

with open("README.xlsx", "rb") as f: 
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name) 



msg.add_attachment()


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
