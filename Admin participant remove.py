#!C:/Users/---->your folder name<----/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb;cgitb.enable()                                             #importing the Common Gateway Interface,sql ,cgi trackback
conn=pymysql.connect(host="localhost",user="root",password="",database="sports")    # connection with phpmysql using xampp
cur=conn.cursor()
f=cgi.FieldStorage()                                                                #to get field data from form
id=f.getvalue("id")
rid=f.getvalue("rid")
q=""" delete from participant where id='%s'"""%(rid)                                #delete data from particular id
cur.execute(q)
conn.commit()

print("""                                                                           #alert message display when id removed
    <script>
        alert("removed successfully");
        location.href="adminparticipantdetails.py?id=%s";
    </script>"""%(id))
conn.close()
