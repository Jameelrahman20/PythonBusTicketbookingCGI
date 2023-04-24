#!C:\Python311\python.exe
print("Content-type:text/html\n\r")


import pymysql
db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="travel")
cur=db.cursor()

import cgi
form=cgi.FieldStorage()

d=form.getvalue("seat")
e=form.getvalue("from")
f=form.getvalue("to")

cur.execute("select * from r1")
for i in cur:
    total=int(d)*int(i[7])
    amount=str(total)
    query="insert into total values(%s,%s,%s,%s)"
    val=[d,e,f,amount]
    cur.execute(query,val)
    db.commit()



if d=="2":
    print('''
    <html>
    <head>
        <title>Passenger details</title>
        <link rel="stylesheet" href="style42.css">
    </head>
    <body>
        <div class="Report-form">
            <center><h2 style='color:blue;'>Passenger details</h2></center>
            <form action="ticket.py" method="post">
                <p>Passanger-1 Name:</p>
                <input type="text" name="n" placeholder="Name"><br>
                <p>Passanger-1 Age:</p>
                <input type="text" name="age" placeholder="Age"><br>

             <div class="dropdown-container">
		 <div class="dropdown">
			<select  name="from" id="from">
				<option> Gender</option>
				<option value="Male">Male</option>
				<option value="Female">Female</option>
			</select>
		 </div>
            </div>
                <p>Passanger-1 Aadhar Number:</p><br>
                <input type="text" name="aa1" placeholder="Aadhar Number">
                <p>Passanger-2 Name:</p><br>
                <input type="text" name="n1" placeholder="Name">
                <p>Passanger-2 Age:</p>
                <input type="text" name="age1" placeholder="Age">
             <div class="dropdown-container">
		 <div class="dropdown">
			<select  name="to" id="to">
				<option> Gender</option>
				<option value="Male">Male</option>
				<option value="Female">Female</option>
			</select>
		 </div>
            </div>
                <p>Passanger-2 Aadhar Number:</p><br>
                <input type="text" name="aa2" placeholder="Aadhar Number"><br>
                <p>Email-ID:</p><br>
                <input type="email" name="email" placeholder="Email-ID">
                <p>Mobile Number:</p><br>
                <input type="text" name="num" placeholder="Mobile Number">
                <center><button type="submit">Next</button></center>
            </form>
            </body>
            </html>''')



