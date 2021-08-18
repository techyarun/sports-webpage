#!C:/Users/----->Your folder name<----/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html\n")

import cgi,pymysql,cgitb;cgitb.enable()                             #importing the Common Gateway Interface,sql ,cgi trackback

 print("""                                                           #Html file           
<html>
<head>
<title>Forget Password</title>
</head>
<body>
<center>
<h3>Forget Password</h3>
     <form method = "post" action = "#">                             #Form  with username and submit button
         Username:
        <input type = "text" name = "username"><br><br>
        <input type = "submit" value = "OK" name = "submit"> <input type ="button" value ="cancel" onclick = "location.href = 'login.py'">
        </form>
        </center>
        </body>
        </html>""")

conn = pymysql.connect(host = "localhost",user="root",password = "",database="sports")  #connection with phpmysql databasse with xampp
cur = conn.cursor()

f = cgi.FieldStorage()                                          #to get field data from form
username = f.getvalue("username")                               #to get value from username
v = f.getvalue("submit")                                        #to get value of submit button

if v != None:
    q = """select password ,email from adminlogin where username = '%s'"""%(username)
    cur.execute(q)
    r = cur.fetchone()                                          #to fetch the details from sql to login

    if r[0] != None:
        import smtplib                                          #importing Email
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
                                                            #Email sender address and password
        sender_address = 'Your mail @gmail.com'
        sender_pass = 'your password'
        to_address = r[1]
                                                            #content to display in mail inbox
        msg = """
            hi Welcome %s,
                password : %s
            """%(username,r[0])
                                                            #Email reciever address and subject fields
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
        session.quit()
                                                            #mail condition ends
        print('Mail sent')                                  #print message if sucessfull
        print("""                                           #shows alert message 
            <script>
            alert("Please check your mail");
            location.href="adminlogin.py";
            </script>
            """)
