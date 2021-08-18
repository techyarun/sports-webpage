#!C:/Users/----->Your Folder name<----/AppData/Local/Programs/Python/Python39/python.exe


print("Content-type: text/html \r\n\r\n")

import cgi, pymysql, cgitb;cgitb.enable()                                                 #importing the Common Gateway Interface,sql ,cgi trackback
conn = pymysql.connect(host="localhost", user="root", password="", database="sports")     # connection with phpmysql using xampp
cur = conn.cursor()
q1 = """select max(id) from volunteer"""
cur.execute(q1)
r = cur.fetchone()
if r[0] != None:
    n = r[0]
else:
    n = 0
                                                                                        #condition for creating an reg id
z = ""
if n < 10:
    z = "000"
elif n < 100:
    z = "00"
elif n < 1000:
    z = "0"
else:
    z = ""

vid = "vid" + z + str(n + 1)                                                            #common id with an certain condition
print("""                                                                               #html and css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Registration</title>
    <style>                                                                            #css 
        body{
            background: url("bg6.jpg");
            background-size: cover;
            text-align: left;
            margin-left: 5%;
            margin-top: 10px;
            font-size: large; 
        }
        h1{
            color: white;
            align-items: center;
            justify-content: center;
        }
        form{
            background: lightseagreen;
            display: inline-block;
            border-radius: 5px;
            padding-bottom: 10px;
            padding-left: 10px;
            padding-right: 10px;
        }
        
    </style>
</head>
<body>                                                                                          #registration field details
    <h1>Volunteer Registration</h1>
    <form method="post" action="#" enctype="multipart/form-data" autocomplete="off">
        <label for="id">id:</label><br>""")
print("""
        <input type="text" name="vid" id="vid" value="%s" readonly><br><br>
        <label for="name">name:</label><br>
        <input type="text" name="name" id="name" placeholder="Enter name"><br>
        <p>gender:</p>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">male</label>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">female</label><br><br>
        <label for="email">email:</label><br>
        <input type="email" name="email" id="email" placeholder="Enter email"><br><br>
        <label for="contact">contact:</label><br>
        <input type="tel" name="contact" id="contact" placeholder="Enter contact"><br><br>
        <label for="age">age:</label><br>
        <input type="text" name="age" id="age" placeholder="Enter age"><br><br>
        <label for="username">username:</label>
        <input type="text" name="username" id="username" placeholder="Enter username"><br><br>
        <label for="password">password:</label>
        <input type="password" name="password" id="password" placeholder="Enter password"><br><br>
        <label for="photo">photo:</label>
        <input type="file" name="photo" id="photo" ><br><br>
        <button type="submit" name="register" id="register">register</button>
        <input type ="button" value ="cancel" onclick = "location.href = 'volunteerlogin.py'">
    </form>
</body>
</html>
  """ % (vid))

f = cgi.FieldStorage()                                                                                  #to get field data from form
sub = f.getvalue("register")
if sub != None:                                                                                         #to get the all fields value
    vid = f.getvalue("vid")
    name = f.getvalue("name")
    gender = f.getvalue("gender")
    email = f.getvalue("email")
    contact = f.getvalue("contact")
    age = f.getvalue("age")
    username = f.getvalue("username")
    password = f.getvalue("password")
    profile = f['photo']

    if profile != None:
        if profile.filename:
            import os                                                                                   #import os

            fp = os.path.basename(profile.filename)
            open("image/" + fp, "wb").write(profile.file.read())
                                                                                                # inserting data to database
            q = """insert into volunteer(vid,name,gender,email,contact,age,username,password,photo) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (vid, name, gender, email, contact, age, username, password, fp)
            cur.execute(q)
            conn.commit()
            conn.close()

            print("""
                <script>                                                                        #alert message when data inserted
                    alert("Data inserted successfully");
                    location.href = "volunteerlogin.py"
                </script>
            """)
    else:
        print("""                                                                               #Error when not inserted
            <script>
                alert("file error");
                location.href = "volunteer.py"
            </script>
        """)

    import smtplib                                                                              #importing Email
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    mail_content = """Hello, %s
                                    USERNAME : %s,
                                    PASSWORD : %s
                            """ % (name, username, password)
                                                                                            # Email sender address and password
    sender_address = 'Your Mail @gmail.com'
    sender_pass = 'Your Password'
    receiver_address = email
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Registration successfull '
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()                                                                          #mail condition ends
    print('Mail sent')                                                                      #print message if sucessfull
