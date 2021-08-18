#!C:/Users/---->Your folder name<----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html \r\n\r\n")


import cgi,pymysql,cgitb;cgitb.enable()                                                 #importing the Common Gateway Interface,sql ,cgi trackback
conn = pymysql.connect(host = "localhost",user="root",password = "",database="sports")  # connection with phpmysql using xampp
cur = conn.cursor()
f = cgi.FieldStorage()                                                                  #to get field data from form
id  = f.getvalue("id")                                                                  #to get value of particluar id

if len(f) == 2:                                                                         #to get all field details
    id = f.getvalue("id")
    cid = f.getvalue("cid")
else:
    id = f.getvalue("id")
    cid = f.getvalue("cid")
    name = f.getvalue("name")
    email = f.getvalue("email")
    contact = f.getvalue("contact")
    age = f.getvalue("age")
    game = f.getvalue("game")
    bloodgroup = f.getvalue("bloodgroup")
    username = f.getvalue("username")
    password = f.getvalue("password")
    profile=f['photo']
    if profile.filename:
        import os                 #importing os

        fp = os.path.basename(profile.filename)
        open("image/" + fp, "wb").write(profile.file.read())

                                # updating the details of volunteer
        q1 = """update participant set name = '%s',email = '%s',contact = '%s',age = '%s',game='%s',bloodgroup='%s',username = '%s',password = '%s',photo = '%s' where id = '%s'"""%(name,email,contact,age,game,bloodgroup,username,password,fp,cid)
        cur.execute(q1)
        conn.commit()
        print("""
             <script>                        #popup alert when update successfully
                alert("Profile updated successfully");
                location.href = "adminparticipantdetails.py?id=%s";
            </script>
            """%(id))
    else:
        q1 = """update participant set name = '%s',email = '%s',contact = '%s',age = '%s',game='%s',bloodgroup='%s',username = '%s',password = '%s' where id = '%s'"""%(name,email,contact,age,game,bloodgroup,username,password,cid)
        cur.execute(q1)
        conn.commit()
        print("""
             <script>
                alert("Profile updated successfully");
                location.href = "adminparticipantdetails.py?id=%s";
            </script>
            """%(id))

q = """select * from participant where id='%s'"""%(cid)
cur.execute(q)
r = cur.fetchone()
print("""                                           #html and css
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Register</title>
            <style>
                body{
                    background-image: url("bg5.jpg");
                    background-size: cover;
                    font-size: large;
                    margin-left: 30px;
                }
                form{
                    display: inline-block;
                    width:250px;
                    border: 5px solid steelblue;
                    padding: 20px;
                    background-color: lightsteelblue;
                }
            </style>
        </head>
        <body>
            <h1>Players Registration</h1>                                           #Form to get details
    <form method="post" action="#" enctype="multipart/form-data" autocomplete="off">
        <label for="id">id:</label>
        <input type="text" name="ptid" id="ptid" value="%s" readonly"><br><br>
        <label for="name">name:</label>
        <input type="text" name="name" id="name" value="%s"><br>
        <label for="email">email:</label><br>
        <input type="email" name="email" id="email" value="%s"><br><br>
        <label for="contact">contact:</label><br>
        <input type="tel" name="contact" id="contact" value="%s"><br><br>
        <label for="age">age:</label><br>
        <input type="text" name="age" id="age" value="%s"><br><br>
        <label for="game">choose your sport:</label><br>
        <select name="game" id="game" value="%s">
            <option value="football">football</option>
            <option value="cricket">cricket</option>
            <option value="hockey">hockey</option>
            <option value="basketball">basketball</option>
        </select><br><br>
        <label for="bloodgroup">choose your bloodgroup:</label>
        <select name="bloodgroup" id="bloodgroup" value="%s">
            <option value="O positive">0 positive</option>
            <option value="O negative">0 negative</option>
            <option value="A positive">A positive</option>
            <option value="A negative">A negative</option>
            <option value="B positive">B positive</option>
            <option value="B negative">B negative</option>
            <option value="AB positive">AB positive</option>
            <option value="AB negative">Ab negative</option>
        </select><br><br>
        <label for="username">username:</label>
        <input type="text" name="username" id="username" value="%s"><br><br>
        <label for="password">password:</label>
        <input type="password" name="password" id="password" value="%s"><br><br>
        <label for="photo">photo:</label>
        <input type="file" name="photo" id="photo" value="%s"><br><br>
        <button type="submit" name="register" id="register">register</button>
        <button type="submit">Cancel</button>
    </form>
    </form>
</body>
</html>
""" %(r[1],r[2],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11]))
conn.close()
