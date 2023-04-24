#!C:\Python311\python.exe
print("Content-type:text/html\n\r")



import cgi
form=cgi.FieldStorage()

a=form.getvalue("from")
b=form.getvalue("to")

import pymysql
db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="travel")
cur=db.cursor()




if a=="Chennai" and b=="Nagercoil":
    print('''
    <html>
    <head>
        <title>Bus Schedules</title>
        <link rel="stylesheet" href="style-2.css">
        <link rel="stylesheet" href="style3.css">
    </head>
    <body>
        <center><h1 style='color:indigo;'>Bus Schedules</h1></center>
    <table>
    <form action="pas.py" method=post>
        <tr>
            <th>Select</th>
            <th>Travels Name</th>
            <th>Bus Number</th>
            <th>Journey Date</th>
            <th>Start Point/Time</th>
            <th>End Point/Time</th>
            <th>Travelling TIme</th>
            <th>AC/Non-AC</th>
            <th>Ticket Price</th>
            <th>No.of Seats Available</th>
            <th>Customer Rating</th>
        </tr>''')
    cur.execute("select * from r1")
    for i in cur:
        print('''
            <tr>''')
        print('''<td><input type="radio" value="vkv" name="r1" ><br></td>''')
        print("<td>",i[0],"</td>")
        print("<td>",i[1],"</td>")
        print("<td>",i[2],"</td>")
        print("<td>",i[3],"</td>")
        print("<td>",i[4],"</td>")
        print("<td>",i[5],"</td>")
        print("<td>",i[6],"</td>")
        print("<td>",i[7],"</td>")
        print("<td>",i[8],"</td>")
        print("<td>",i[9],"</td>")
        print('''
            </tr>''')
    cur.execute("select * from r2")
    for i in cur:
        print('''
            <tr>''')
        print('''<td><input type="radio" name="r2" value="srm"><br></td>''')
        print("<td>",i[0],"</td>")
        print("<td>",i[1],"</td>")
        print("<td>",i[2],"</td>")
        print("<td>",i[3],"</td>")
        print("<td>",i[4],"</td>")
        print("<td>",i[5],"</td>")
        print("<td>",i[6],"</td>")
        print("<td>",i[7],"</td>")
        print("<td>",i[8],"</td>")
        print("<td>",i[9],"</td>")
        print('''
            </tr>''')
    cur.execute("select * from r3")
    for i in cur:
        print('''
            <tr>''')
        print('''<td><input type="radio" name="r3" value="tipu"><br></td>''')
        print("<td>",i[0],"</td>")
        print("<td>",i[1],"</td>")
        print("<td>",i[2],"</td>")
        print("<td>",i[3],"</td>")
        print("<td>",i[4],"</td>")
        print("<td>",i[5],"</td>")
        print("<td>",i[6],"</td>")
        print("<td>",i[7],"</td>")
        print("<td>",i[8],"</td>")
        print("<td>",i[9],"</td>")
        print('''
            </tr>''')
    cur.execute("select * from r4")
    for i in cur:
        print('''
            <tr>''')
        print('''<td><input type="radio" name="r4" value="gm"><br></td>''')
        print("<td>",i[0],"</td>")
        print("<td>",i[1],"</td>")
        print("<td>",i[2],"</td>")
        print("<td>",i[3],"</td>")
        print("<td>",i[4],"</td>")
        print("<td>",i[5],"</td>")
        print("<td>",i[6],"</td>")
        print("<td>",i[7],"</td>")
        print("<td>",i[8],"</td>")
        print("<td>",i[9],"</td>")
        print('''
            </tr>''')


    print('''</table>
        <div class="container">
            <button class="btn" type="submit">proceed</button>
        </div>
    </form>    
    </body>
    </html>
    ''')


