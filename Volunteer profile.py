#!C:/Users/---->Your Folder Name<----/AppData/Local/Programs/Python/Python39/python.exe

print("Content-type: text/html\n")


import cgi,pymysql,cgitb;cgitb.enable()                                                 #importing the Common Gateway Interface,sql ,cgi trackback
conn = pymysql.connect(host = "localhost",user="root",password = "",database="sports")  # connection with phpmysql using xampp
cur = conn.cursor()
f = cgi.FieldStorage()                                                                  #to get field data from form
id = f.getvalue("id")                                                                   #to get the particular id

q = """select * from volunteer where id=%s"""%(id)                                      #fetching details of particular user

cur.execute(q)
r = cur.fetchone()
print("""                                                                               #html and css
<html>
<head><title>profile</title>
<style>
*{
text-align:center;
background:#4600eb;
}
#table{
justify-content:center;
margin-right:200px;
margin-top:100px;
float:right;
}
table,tr,th,td,b{
background:white;
color:black;
border-radius:10px;
padding:10px;
}
h1{
float:left;
color:white;
margin-top:250px;
margin-left:100px;
}
h1:hover{
text-shadow:4px 4px 5px black;
}

b{
text-transform:uppercase;
}
</style>
</head>
<body>                                                                              #to fetch the details
<h1><tr><td>Welcome %s</td></tr></h1>
<div class="table">
<table id="table" >
<tr><td><img src = "image\%s" width = "100" height = "100"></td></tr>
<tr><td><b>ID</b>: %s</td></tr>
<tr><td><b>NAME</b>: %s</td></tr>
<tr><td><b>GENDER</b>: %s</td></tr>
<tr><td><b>EMAIL</b>: %s</td></tr>
<tr><td><b>NUMBER</b>: %s</td></tr>
<tr><td><b>AGE</b>: %s</td></tr>
<tr><td><b>USERNAME</b>: %s</td></tr>
<tr><td><b>PASSWORD</b>: %s</td></tr>
</table></div>
</body>
</html>
""" %(r[2],r[9],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
conn.close()
