#!C:/Users/---->Your Folder Name<----/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html\n")

import cgi,pymysql,cgitb;cgitb.enable()                                     #importing the Common Gateway Interface,sql ,cgi trackback

print("""                                                                   #Html and css
<html>
<head>
<title>Forget Password</title>
</head>
<body>
<center>
<h3>Forget Password</h3>                                                     #to get username 
    <form method = "post" action = "#">
        Username:
        <input type = "text" name = "username"><br><br>
        <input type = "submit" value = "OK" name = "submit"> 
        <input type ="button" value ="cancel" onclick = "location.href = 'volunteerlogin.py'">
        </form>
        </center>
        </body>
        </html>""")

conn = pymysql.connect(host = "localhost",user="root",password = "",database="sports")          # connection with phpmysql using xampp
cur = conn.cursor()

f = cgi.FieldStorage()                                                                          #to get field data from form
username = f.getvalue("username")                                                               #to get the value of username
v = f.getvalue("submit")

if v != None:
    q = """select password ,email from volunteer where username = '%s'"""%(username)            #selecting username and password from sql
    cur.execute(q)
    r = cur.fetchone()

    if r[0] != None:
        import smtplib                                                                          #importing Email
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

                                                                                                # Email sender address and password
        sender_address = 'Your Mail@gmail.com'
        sender_pass = 'Your password'
        to_address = r[1]
        msg = """                                                                               #content to display in mail inbox
            hi Welcome %s,
                password : %s
            """%(username,r[0])
                                                                                                # Email reciever address and subject fields
        receiver_address = to_address
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'New Password'
        message.attach(MIMEText(msg, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address,sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()                                                                          #mail condition ends
        print('Mail sent')                                                                      #print message if sucessfull
        print("""
            <script>                                                                            #shows alert message 
            alert("Please check your mail");
            location.href="login.py";
            </script>
            """)
