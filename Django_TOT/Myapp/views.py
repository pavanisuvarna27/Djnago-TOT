from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  home(request):
    return HttpResponse('<h2>This is home page</h2>')
def  about(s):
	return HttpResponse("<h1 style='background-color:orange;color:black;padding:3px;margin-left:230px;margin-right:230px'>welcome to homepage</h1>")
def  msg(c,name):
	return HttpResponse("<center><h2>Hii...{} welcome</h2></center>".format(name))
def  data(c,name,num):
	return HttpResponse("<center><h2>Hii...{} welcome {}</h2></center>".format(name,num))
def table(c,n):
	j=""
	for i in range(1,11):
		j+="{} x {:02} ={:02}".format(n,i,n*i)+"</br>"
	#print(j)
	return HttpResponse(j)
def abc(request,name,age):
	#print(name,age)
	return render(request,"Myapp/abc.html",{"name":name,"age":age})
def sample(request):
	return render(request,"Myapp/demo.html")
def login(request):
	return render(request,"Myapp/login.html")
def register(request):
	return render(request,"Myapp/register.html")