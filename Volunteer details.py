#!C:/Users/---->Your Folder Name<----/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb;cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="sports")
cur=conn.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")
q="""select * from volunteer"""
cur.execute(q)
r=cur.fetchall()
count=0
print("""
    <html>
    <head><title>my profile</title></head>
    <style>
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
    <th>vid</th><th>name</th><th>gender</th><th>email</th><th>contact</th><th>age</th><th>username</th>
    <th>password</th><th>profile</th>
    </tr>""")
for i in r:
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
    <td><img src="image/%s" width="30" height="40"></td></tr>
"""%(count,i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
print("""
</table>
</body>
</html>
""")
conn.close()
