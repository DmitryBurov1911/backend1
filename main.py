from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
import smtplib


app = FastAPI()

@app.get("/")
def root():
    return FileResponse("MY_HTML/index.html")

def send_mail(message):
    sender = "sender887766@gmail.com"
    password = "yoxsxgzfpxtqjjfw"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)

        print("IHN") 
    except Exception as _ex:
        return print(f"{_ex}\n")

@app.post("/hello")
def hello(data = Body()):
    fio = data["fio"]
    html_email = data["html_email"]

    all_content = f"Способы связи - {fio}, Контент - {html_email}".encode("utf-8")
        
    send_mail(all_content)

    return print(f"Способы связи: {fio}, Контент: {html_email}")
