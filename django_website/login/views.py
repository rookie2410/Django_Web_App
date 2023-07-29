from django.shortcuts import render
import mysql.connector as sql

Email=''
Password=''

# Create your views here.
def loginaction(request):
    global Email,Password
    if request.method=="POST":
        dbConnector=sql.connect(host="localhost" , user = "root" , passwd="dev1", database="django_website")
        cursor = dbConnector.cursor()
        data=request.POST
        for key,value in data.items():
            if key=="email":
                Email=value
            if key=="password":
                Password=value

        sqlquery="select * from users where Email='{}' and Password='{}'".format(Email,Password)
        cursor.execute(sqlquery)
        DatafromDB=tuple(cursor.fetchall())
        
        if DatafromDB==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')



