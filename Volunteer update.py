#!C:/Users/----->Your Folder Name<-----/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb;cgitb.enable()                                             #importing the Common Gateway Interface,sql ,cgi trackback
conn=pymysql.connect(host="localhost",user="root",password="",database="sports")    # connection with phpmysql using xampp
cur=conn.cursor()
f=cgi.FieldStorage()                                                                #to get field data from form
sid = f.getvalue("sid")
q ="""select * from newvolunteer where accept='New'"""
cur.execute(q)
r = cur.fetchall()
count=0
if sid!=None:
    q1="""update volunteer set accept='verified' where id=%s"""%(sid)               #update the details to be verified
    cur.execute(q1)
    conn.commit()
    print("""                                                                       #popup alert 
        <script>
          alert("Request accepted");
          location.href="adminvolunteerdetails.py"
          </script>
         """)
