#!C:\Python311\python.exe
print("Content-type:text/html\n\r")

cn="9078563412343409"
da="05/07/2030"
cv="232"
ot="121"

import cgi
form=cgi.FieldStorage()

a=form.getvalue("amt")
p=form.getvalue("c")
q=form.getvalue("exp")
r=form.getvalue("cvv")
s=form.getvalue("otp")

import pymysql
db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="travel")
cur=db.cursor()


cur.execute("select * from total")
for i in cur:
    if i[3]==a:
        if cn==p:
            if da==q:
                if r==cv:
                    if ot==s:
                        print(''' <style>
                            body{
                                    background-image:url('img57.jpg');
                                    background-repeat:no-repeat;
                                    background-size:cover;
                            }
                         </style>''')
                        print('''
                        <html>
                        <head>
                            <title>Payment Status</title>
                            <link rel="stylesheet" href="style3-1.css">
                        </head>
                        <body>
                            <center><h1 style='color:blue;'>Payment Successfull</h1></center>
                            <h2 style='color:red;'>Ticket Details</h2><br><br>''')
                        cur.execute("select * from r1")
                        for i in cur:
                            print("<h3><p style='color:indigo;'>Travels Name:",i[0],"</p></h3>")
                            print("<h3><p style='color:indigo;'>Travels Number:",i[1],"</p></h3>")
                            print("<h3><p style='color:indigo;'>Journey Date:",i[2],"</p></h3>")
                            print("<h3><p style='color:indigo;'>Start Point/Time:",i[3],"</p></h3>")
                            print("<h3><p style='color:indigo;'>End Point/Time:",i[4],"</p></h3>")
                            print("<h3><p style='color:indigo;'>Total Travel Timing:",i[5],"</p></h3>")
                            print("<h3><p style='color:indigo;'>AC/Non-AC:",i[6],"</p></h3>")
                        cur.execute("select * from total")
                        for i in cur:
                             print("<h3><p style='color:indigo;'>No.of Tickets:",i[0],"</p></h3>")
                             print("<h3><p style='color:indigo;'>Seat Numbers: S2,S3</p></h3>")
                             print("<h3><p style='color:indigo;'>Boarding Point/Time:",i[1],"</p></h3>")
                             print("<h3><p style='color:indigo;'>Dropping Point/Time:",i[2],"</p></h3>")
                             print("<h3><p style='color:indigo;'>Total Ticket Cost:",i[3],"</p></h3>")
                        cur.execute("select * from pass")
                        for i in cur:
                            print("<h3><p style='color:indigo;'>Passenger-1 Details:","Name-  ",i[0],"Age-  ",i[1],"Gender-  ",i[2],"</p></h3>")
                            print("<h3><p style='color:indigo;'>Passenger-2 Details:","Name-  ",i[4],"Age-  ",i[5],"Gender-  ",i[6],"</p></h3>")
                            print("<h3><p style='color:indigo;'>Email-ID:",i[8],"</p></h3>")
                            print("<h3><p style='color:indigo;'>Contact Number:",i[9],"</p></h3>")
                        print('''<form action="mail.py" method="post">
                                    <div class="container">
                                            <center><button class="btn" type="submit">Send Alert</button></center>
                                     </div>
                                </form>
                                     <center><a href="http://localhost/Bus/signup_frontend.html"<button class="block">logout</a></button></center>
                                </body>
                                </head>
                                </html>''')




