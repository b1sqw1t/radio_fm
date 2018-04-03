from django.shortcuts import render

def index(request):
    hello = 'hello mother fucker'
    title = 'Radio_FM | Главная страница'
    return render(request,'index.html',{'title':title})

def index2(request):
    title_text = 'ПРОВЕРКА СУКА ШАБЛОНА'
    return render(request,'index.html',{'text': title_text})