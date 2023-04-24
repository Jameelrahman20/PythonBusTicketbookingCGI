#!C:\Python311\python.exe
print("Content-type:text/html\n\r")






print('''
<style>
	body{
		background-image:url('img35.jpg');
		background-repeat:no-repeat;
		background-size:cover;
}
</style>


''')

print('''

<html>
<head>
	<title>Ticket Avalability check</title>
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
<body>  <form action=table.py post="method" >
	<div class="dropdown-container">
		<div class="dropdown">
			<select  name="from" id="from">
				<option>Starting Point</option>
				<option value="Chennai" >Chennai</option>
				<option value="Thanjavur" >Thanjavur</option>
				<option value="Nagercoil" >Nagercoil</option>
			</select>
		</div>

		<div class="dropdown">
			<select  name="to" id="to">
				<option>Destination Point</option>
				<option value="Chennai" >Chennai</option>
				<option value="Thanjavur" >Thanjavur</option>
				<option value="Nagercoil" >Nagercoil</option>
			</select>
		</div>
		    <div class="container">
                            <button class="btn" type="submit">Search Buses</button><br><br>
                    </div>
	</div>
	</form>
</body>
</html>

''')

