#!C:\Python311\python.exe
print("Content-type:text/html\n\r")


import pymysql
db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="travel")
cur=db.cursor()


import cgi
import smtplib
import schedule
import time

email="hj.jamrahman@gmail.com"
password='syeelczrwzhzgewa'


def alert_email():
    subject = "Ticket Booking is Status"
    message = '''Dear Jameel,
                    Your Bus Ticket Booking is Sucessfull

                    For Further Deatails Kindly Visit our Website

                    Thank you '''

           
    send_email(subject, message)




def send_email(subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        cur.execute("select * from pass")
        for i in cur:
             to_email=i[8]
        body='\r\n'.join(['To: %s' % to_email,
                            'From: %s' % email,
                            'Subject: %s' % subject,
                            '', message])
        server.sendmail(email, to_email, body)
        print('Email sent successfully')
    except Exception as e:
        print('Something went wrong:', e)
    finally:
        server.quit()


schedule.every().day.at("22:06").do(alert_email)


while True:
    schedule.run_pending()
    time.sleep(1)
