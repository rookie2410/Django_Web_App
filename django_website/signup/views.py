from django.shortcuts import render
import mysql.connector as sql

FirstName=''
LastName=''
Sex=''
Email=''
Password=''

# Create your views here.
def signaction(request):
    global FirstName,LastName,Sex,Email,Password
    if request.method=="POST":
        dbConnector=sql.connect(host="localhost" , user = "root" , passwd="dev1", database="django_website")
        cursor = dbConnector.cursor()
        data=request.POST
        for key,value in data.items():
            if key=="first_name":
                FirstName=value
            if key=="last_name":
                LastName=value
            if key=="sex":
                Sex=value
            if key=="email":
                Email=value
            if key=="password":
                Password=value

        sqlquery="insert into users Values('{}','{}','{}','{}','{}')".format(FirstName,LastName,Sex,Email,Password)
        cursor.execute(sqlquery)
        dbConnector.commit()

    return render(request,'signup_page.html')



