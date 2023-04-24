#!C:\Python311\python.exe
print("Content-type:text/html\n\r")

import pymysql
db=pymysql.Connect(host="localhost",user="root",password="10114nov",database="travel")
cur=db.cursor()

import cgi
form=cgi.FieldStorage()

c=form.getvalue("r1")



cur.execute("select * from r1")
for i in cur:
    if c=="vkv":
        print('''
        <html>
        <head>
            <title>Passenger Boarding details</title>
            <link rel="stylesheet" href="style1-1.css">
        </head>
        <body>
            <div class="Report-form">
                <center><h2 style='color:blue;'>Passenger Boarding details</h2></center>
                <form action="passenger.py" method="post">
                    <p>No.of Passangers:</p><br>
                    <input type="number" name="seat" placeholder="No.of seats"><br><br><br><br><br><br>
        <style>
		.dropdown-container {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
	    
		}

		.dropdown {
			margin-bottom: 100px;

                }
		.dropdown select {
			padding: 25px 150px;
			font-size: 16px;
			border: none;
			border-radius: 5px;
			box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.3);
			background-color: #fff;
			cursor: pointer;
		}
		.container{
                        margin: auto;
                }
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
</head>
<body>  
	<div class="dropdown-container">
		<div class="dropdown">
			<select  name="from" id="from">
				<option> Boarding Point/Time</option>
				<option value="Koyambedu/19:45" >Koyambedu/19:45</option>
				<option value="Tambaram/21:00" >Tambaram/21:00</option>
				<option value="Perungulathur/21:30" >Perungulathur/21:30</option>
			</select>
		</div>

		<div class="dropdown">
			<select  name="to" id="to">
				<option>Dropping Point/Time</option>
				<option value="Vadaserry-Depot/6:55">Vadaserry-Depot/6:55</option>
				<option value="Arulvaimozhi/6:30" >Arulvaimozhi/6:30</option>
				<option value="Monday Market/6:15" >Monday Market/6:15</option>
			</select>
		</div>
	</div>

                    <center><button type="submit">Submit</button></center>
                </form>
            </div>
        </body>
        </html>
        ''')


