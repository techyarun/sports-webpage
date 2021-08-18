#!C:/Users/---->Your Folder name<----/AppData/Local/Programs/Python/Python39/python.exe
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
    username = f.getvalue("username")
    password = f.getvalue("password")
    profile = f['photo']

    if profile.filename:
        import os                               #importing os
        fp = os.path.basename(profile.filename)
        open("image/" + fp, "wb").write(profile.file.read())

                                                #updating the details of volunteer
        q1 = """update volunteer set name = '%s',email = '%s',contact = '%s',age = '%s',username = '%s',password = '%s',photo = '%s' where id = '%s'"""%(name,email,contact,age,username,password,fp,cid)
        cur.execute(q1)
        conn.commit()
        print("""                               #popup alert when update successfully
             <script>
                alert("Profile updated successfully");
                location.href = "adminvolunteerdetails.py?id=%s";
            </script>
            """%(id))
    else:
        q1 = """update volunteer set name = '%s',email = '%s',contact = '%s',age = '%s',username = '%s',password = '%s' where id = '%s'"""%(name,email,contact,age,username,password,cid)
        cur.execute(q1)
        conn.commit()
        print("""
             <script>
                alert("Profile updated successfully");
                location.href = "adminvolunteerdetails.py?id=%s";
            </script>
            """%(id))

q = """select * from volunteer where id = '%s'"""%(cid)
cur.execute(q)
r = cur.fetchone()
print("""                                                           #html and css
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Register</title>
            <style>
                body{
                    background-image: url("bg6.jpg");
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
            <h1>Volunteer Registration</h1>                                         #Form to get details
            <form method = "post" action = "#" enctype = "multipart/form-data">
            <label for="id">Id:</label><br>
            <input type="text" name = "vid" id = "vid" value = "%s" readonly><br><br>
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" value = "%s"  ><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" value = "%s" ><br><br>
            <label for="contact">Contact:</label><br>
            <input type="tel" id="contact" name="contact" value = "%s"  ><br><br>
            <label for="age">Age:</label><br>
            <input type="text" id="age" name="age" value = "%s"  ><br><br>
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" value = "%s"  ><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" value = "%s"  ><br><br>
            <label for="photo">Photo:</label><br>
            <input type="file" id="photo" value = "%s"  name="photo"><br><br>
            <button type="submit" name = "register" id = "register">Register</button>
            <button type="submit">Cancel</button>
    </form>
</body>
</html>
""" %(r[1],r[2],r[4],r[5],r[6],r[7],r[8],r[9]))
conn.close()
