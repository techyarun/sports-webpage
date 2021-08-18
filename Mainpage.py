#!C:/Users/---->Your Folder Name<----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-wEmeIV1mKuiNpC+IOBjI7aAzPcEZeedi5yW5f2yOq55WWLwNGmvvx4Um1vskeMj0" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-p34f1UUtsS3wqzfto5wAAmdvj+osOnFyQFpp4Ua3gs/ZVWx6oOypYoCJhGGScy+8" crossorigin="anonymous"></script>
    <title>Sports | A way to kind</title>
    <style>
        *{
    margin: 0;
    padding: 0;
}
body{
    background-image: url("sports.jpg");

}
h1{
    color: white;
    text-align: center;
    font-size: 60px;
}
.header{
    margin-top: 20%;
    font-style: italic;
    font-family: sans-serif;
    margin-left: 50%;
}
img{
    width: 5%;
    height: 5%;
    margin: 15px;
}
.logos{
    margin-top: -5%;
}
.logos  .content1 button{
    margin-left: 200px;
    background: chartreuse;
    padding: 10px;
    border-radius: 5px;
    padding-left: 2%;
    padding-right: 2%;
    text-align: center;
    justify-content: center;
    color: white;
}
.logos  .content2 button{
    margin-left: 50px;
    background: chartreuse;
    padding: 10px;
    border-radius: 5px;
    padding-left: 2%;
    padding-right: 2%;
    text-align: center;
    justify-content: center;
    color: white;    
}
.logos  .content3 button{
    margin-left: 50px;
    background: chartreuse;
    padding: 10px;
    border-radius: 5px;
    padding-left: 2%;
    padding-right: 2%;
    text-align: center;
    justify-content: center;
    color: white;    
}
.logos .content1 button:hover{
    background-color: indianred;
}
.logos .content2 button:hover{
    background-color: indianred;
}
.logos .content3 button:hover{
    background-color: indianred;
}
    </style>
</head>
<body>
    
    <img src="logos.png" alt="logo">
    <div class="logos">
        <a href="adminlogin.py" class="content1"><button>Admin</button></a>
        <a href="participantlogin.py" class="content2"><button>Players</button></a>
        <a href="volunteerlogin.py" class="content3"><button>Volunteer</button></a>
    </div>
    <div class="header">
        <h1>SPORTS</h1>
    </div>
    
</body>
</html>
""")
