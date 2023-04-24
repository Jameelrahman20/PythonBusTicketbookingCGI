#!C:\Python311\python.exe
print("Content-type:text/html\n\r")


import pymysql
db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="travel")
cur=db.cursor()


import cgi
form=cgi.FieldStorage()


p1=form.getvalue("p1")
p2=form.getvalue("p2")




if p1=="gpay":
    print('''
    <html>
    <head>
        <title>UPI Page</title>
        <link rel="stylesheet" href="style1-3.css">
    </head>
    <body>
        <div class="Report-form">
            <center><h2 style='color:blue;'>UPI Payment</h2></center>
            <form action="upi.py" method="post">
                <p>UPI-ID</p><br><br>
                <input type="text" name="id" placeholder="UPI-ID"><br><br>
                 <p>UPI-PIN</p><br><br>
                <input type="password" name="pin" placeholder="UPI-PIN"><br><br>
                <p>Amount</p><br><br>
                <input type="text" name="am" placeholder="Amount"><br><br>
                <center><button type="submit">Pay</button></center>
             </form>
        </div>
    </body>
    </html>
    ''')
elif p2=="card":
    print('''
    <html>
    <head>
        <title>Card Page</title>
        <link rel="stylesheet" href="style1-4.css">
    </head>
    <body>
        <div class="Report-form">
            <center><h2 style='color:blue;'>Debit/Credit Card Payment</h2></center>
            <form action="card.py" method="post">
                <p>Card NUmber:</p><br><br>
                <input type="text" name="c" placeholder="Card Number"><br><br>
                 <p>Card Exp-Date:</p><br><br>
                <input type="text" name="exp" placeholder="Exp-Date"><br><br>
                <p>CVV:</p><br><br>
                <input type="text" name="cvv" placeholder="cvv"><br><br>
                <p>OTP:</p><br><br>
                <input type="text" name="otp" placeholder="OTP"><br><br>
                <p>Amount:</p><br><br>
                <input type="text" name="amt" placeholder="Amount"><br><br>
                <center><button type="submit">Pay</button></center>
             </form>
        </div>
    </body>
    </html>
    ''')




