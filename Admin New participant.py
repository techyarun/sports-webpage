#!C:/Users/---->Your folder name<----/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb;cgitb.enable()                                             #importing the Common Gateway Interface,sql ,cgi trackback
conn=pymysql.connect(host="localhost",user="root",password="",database="sports")    # connection with phpmysql using xampp
cur=conn.cursor()
f=cgi.FieldStorage()                                                                #to get field data from form
sid = f.getvalue("sid")                                                             #to get value of particular id
q ="""select * from participant where accept='New'"""
cur.execute(q)
r = cur.fetchall()                                                                  #to fetch all details
count=0

print("""                                                                           #html and css 
    <html>
    <head><title>my profile</title></head>                                          #title of webpage
    <style>                                                                         #style sheet
        table,th,td{
        border-collapse:collapse;
        border:3px solid powderblue;
        padding:30px;
        }
    </style>
    <body>
    <table border="2" width="50">
    <tr>
    <th>id</th>
    <th>ptid</th><th>name</th><th>gender</th><th>email</th><th>contact</th><th>age</th><th>game</th><th>bloodgroup</th><th>username</th>
    <th>password</th><th>photo</th><th>accept</th><th>remove</th>
    </tr>""")
for i in r:                                               #loop to print table
    count=count+1
    print("""
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><img src="image/%s" width="30" height="40"></td>
    <td><a href="participantupdate.py?sid=%s&id=%s">accept</a></td></td>
    <td><a href="adminparticipantremove.py?rid=%s&id=%s">remove</a></td></tr>
"""%(count,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[0],id,i[0],id))
print("""
</table>
</body>
</html>
""")
if sid!=None:                                                               #verify the details and accept the user
    q1="""update participant set accept='verified' where id=%s"""%(sid)
    cur.execute(q1)
    conn.commit()
    print("""                                                               #alert displays
        <script>
          alert("Request accepted");
          location.href="adminparticipantdetails.py"
          </script>
         """)
conn.close()
