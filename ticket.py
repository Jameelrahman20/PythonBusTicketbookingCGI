#!C:\Python311\python.exe
print("Content-type:text/html\n\r")

a1="4098 45678 4567"
a2="4095 45278 4167"
import pymysql
db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="travel")
cur=db.cursor()

import cgi
form=cgi.FieldStorage()


g=form.getvalue("n")
f1=form.getvalue("age")
h=form.getvalue("from")
i=form.getvalue("aa1")
j=form.getvalue("n1")
k=form.getvalue("age1")
l=form.getvalue("to")
m=form.getvalue("aa2")
n=form.getvalue("email")
o=form.getvalue("num")

query="insert into pass values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=[g,f1,h,i,j,k,l,m,n,o]
cur.execute(query,val)
db.commit()

if i==a1:
    if m==a2:
        cur.execute("select * from total")
        for i in cur:
            print(''' <style>
                body{
                        background-image:url('img41.jpg');
                        background-repeat:no-repeat;
                        background-size:cover;
        }
        </style>''')
            print('''
            <html>
            <head>
                    <title>Payment page</title>	
            </head>''')
            print("<body>")
            print("<center><h1 style='color:blue;'>Payment Options</h1></center><br><br><br>")
            print("<h1 style=color:red;>your Total Ticket price is Rs.",i[3],"</h1><br><br><br><br>")
            print('''<form action="pay.py" method="post">
                      <h1 style="color:aqua;">
                      <input type="radio"name="p1"value="gpay">Gpay/Phonepae<br><br><br><br>
                      <input type="radio"name="p2"value="card">Credit/Debit Card<br><br><br><br>
                      </h1>'
                      <style>
                                          button{
                                padding: 18px 60px;
                                font-size: 1em;
                                font-family: sans-serif;
                                font-weight: bold;
                                cursor: pointer;
                                border: none;
                                border-radius: 10%;
                                trans
                        }
                        .btn:hover{
                                box-shadow: inset 2px 2px 2px red, inset -2px -2px 2px red;
                                background-color: black;
                                color: red;
                        }
                      </style>
                          <button type="submit">Pay</button>
                      </form>
                      </body>
                      </html>''')

                    
               


            
