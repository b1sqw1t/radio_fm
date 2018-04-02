from django.shortcuts import render

def index(request):
    hello = 'hello mother fucker'
    return render(request,'index.html',{'hello': hello})