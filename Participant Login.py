#!C:/Users/---->Your Folder Name<----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html \r\n\r\n")

import cgi,pymysql,cgitb;cgitb.enable()                                             #importing the Common Gateway Interface,sql ,cgi trackback
conn = pymysql.connect(host="localhost",user="root",password="",database="sports")  # connection with phpmysql using xampp
cur = conn.cursor()
print("""                                                                           #Html and css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Participant Login </title>
    <style>
        body{
            background-image: url("bg2.jpg");
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
            background: cornflowerblue;
            border-radius: 10px;
        }
    
    </style>
</head>
<body>
    <h1>Players Login</h1>
    <div>
        <form>                                                                                  #login form to get username and password details
            <label for="username">username</label><br>
            <input type="text" name="username" id="username" ><br><br>
            <label for="password">password</label><br>
            <input type="password" name="password" id="password"><br><br>
            <button type="submit" name="login"  value="login">Login</button>
            <button type="submit"><a href="mainpage.py" style="text-decoration: none;" class="reg">Cancel</a></button>
            <button><a href="participantforgot.py" style="text-decoration: none;" class="reg">Forgot password</a></button><br><br>
            <p>---------(OR)----------</p>
            <button class="reg1"><a href="participant.py" style="text-decoration: none;" class="reg">Register</button></a>
        </form>
    </div>
</body>
</html>
""")

f = cgi.FieldStorage()                                                                      #to get field data from form
username = f.getvalue("username")                                                           #to get the value of username
password = f.getvalue("password")                                                           #to get the value of password
v = f.getvalue("login")
if v!=None:
    q = """select id from participant where username='%s' and password = '%s'""" %(username,password)    #select id to get detail from sql
    cur.execute(q)
    r = cur.fetchone()

    if r != None:
        print("""                                                                           #alert when login sucessfully
            <script>
                alert("Login successfully");
                location.href = "participantprofile.py?id=%s";
            </script>
        """%(r[0]))
    else:                                                                                    #alert error when not login
        print("""
            <script>
                alert("Login error")
            </script>
        """)
