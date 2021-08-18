#!C:/Users/----->Your folder name<-----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html \r\n\r\n")

import cgi, pymysql, cgitb;cgitb.enable()                   #importing the Common Gateway Interface,sql ,cgi trackback

conn = pymysql.connect(host="localhost", user="root", password="", database="sports")  # connection with phpmysql using xampp
cur = conn.cursor()
print("""                                               #Html and css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login </title>                                             #Title of an webpage
    <style>                                                                 #CSS 
        body{
            background-image: url("bg1.jpg");
            background-size: cover;
            text-align: left;
            margin-left: 10%;
            margin-top: 200px;
            font-size: large; 
        }
        form{
            display: inline-block;
            text-align: center;
            padding: 20px;
        }
        h1{
            color: chartreuse;
            margin-left: 50px;
        }
        div{
            padding: 20px;
            justify-content: center;
            align-items: center;

        }
        div form{
            color: black;
            background: #5100E5;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <h1>Admin Login</h1>
    <div>
        <form>                                                                  #Form with username and password fields
            <label for="username">Username</label><br>
            <input type="text" name="username" id="username" ><br><br>
            <label for="password">password</label><br>
            <input type="password" name="password" id="password"><br><br>
            <button type="submit" name="login" value="login">Login</button>
            <button type="submit"><a href="mainpage.py" style="text-decoration: none;" class="reg">Cancel</a></button>
            
        </form>

    </div>
</body>
</html>
""")

f = cgi.FieldStorage()                                        #to get field data from form
username = f.getvalue("username")                             #to get the value of username
password = f.getvalue("password")                             #to get the value of password
v = f.getvalue("login")
if v != None:
    q = """select id from adminlogin where username='%s' and password = '%s'""" % (username, password)
    cur.execute(q)
    r = cur.fetchone()                                                      #to fetch the login details

    if r != None:                                                           #check the login success part
        print("""                                                           
            <script>                                
                alert("Login successfully")
                location.href = "admin.py"
            </script>
        """)
    else:
        print("""
            <script>
                alert("Login error")
                location.href="adminlogin.py"
            </script>
        """)
