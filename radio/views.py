from django.shortcuts       import render,redirect,get_object_or_404,get_list_or_404
from radio.models           import Radioitem,City,Country, Style,Comment
from django.views.generic   import list,base
from radio.forms            import CommentForm
from django.contrib.auth.decorators import login_required


class index(list.ListView):
    """
    Выводит список всех радиостанций на главную страницу сайта
    """
    template_name = 'index.html'
    model = Radioitem
    paginate_by = 4

    def get_context_data(self,**kwargs):
        context= super(index,self).get_context_data(**kwargs)
        context['title'] = 'Radio FM - Лучшее в онлайне'
        return context


def like(request,likeid=None):
    """
    Ставик лайк радиостанции
    :param likeid: id радиостанции
    """
    object = get_object_or_404(Radioitem,id=likeid)
    object.radio_likes += 1
    object.save()
    return redirect(str(object.get_absolute_url()))


def search_city(request,cityid=None):
    """
    Производит поиск радиостанции по городу и выводит на главную страницу
    :param cityid: id города
    """
    object = get_list_or_404(Radioitem,radio_city__id=cityid)
    title = 'Все радиостанции города: %s' %City.objects.get(id=cityid) #Сохраняет название города
    return render(request,'index.html',{'object_list':object, 'title':title})

def search_country(request,countryid=None):
    """
    Производит поиск радиостанции по стране и выводит на главную страницу
    :param countryid: id страны
    """
    object = get_list_or_404(Radioitem,radio_city__country__id=countryid)
    title = 'Все радиостанции страны: %s' %Country.objects.get(id=countryid)#Сохраняет название страны
    return render(request,'index.html',{'object_list':object,'title':title})

def search_style(request,styleid):
    """
    Производит поиск по стилю радиостанций
    :param styleid: id стиля музыки
    """
    print(styleid)
    object = get_list_or_404(Radioitem, radio_style__id=styleid)
    title = 'Все радиостанции со стилем музыки: %s' %Style.objects.get(id=styleid) #Сохраняет название стиля
    return render(request,'index.html',{'object_list':object,'title':title})


class viewradio(base.TemplateView):
    """
    Выводит выбранную радиостанцию
    """
    template_name = 'radioview.html'
    form = None

    def get(self,request,*args,**kwargs):
        try:
            self.radioid = self.kwargs['radioid']
            object = Radioitem.objects.get(pk=self.radioid)
            object.radio_view += 1
            object.save()
            self.form = CommentForm()
        except:
            return redirect('index')
        return super(viewradio,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(viewradio,self).get_context_data(**kwargs)
        context['radioitem'] = Radioitem.objects.get(id=self.radioid)
        context['title'] = context['radioitem'].radio_name
        context['comment_form'] = self.form
        return context

    def post(self,request,*args,**kwargs):
        self.radioid = self.kwargs['radioid']
        object = Radioitem.objects.get(pk=self.radioid)
        self.form = CommentForm(request.POST)
        if self.form.is_valid():
            new_comment = self.form.save(commit=False)
            new_comment.radiostation = object
            new_comment.author = request.user
            new_comment.email = request.user.email
            new_comment.save()
            return redirect(object)
        return super(viewradio,self).get(request,*args,**kwargs)

    def get_queryset(self):
        return Radioitem.objects.get(id=self.radioid)

def index2(request):
    """
    Тестовая функиця, просто что то тестить
    :param request:
    :return:
    """
    object = get_list_or_404(Radioitem,radio_error=True)
    return render(request,'index22.html',{'object_list':object})

def error(request,radioid=None):
    """
    Сообщает о проблемы с отображением радиостанции
    :param radioid:  id радиостанции
    """
    object = get_object_or_404(Radioitem, id=radioid)
    if not object.radio_error:
        object.radio_error = True
        object.save()
    return redirect(str(object.get_absolute_url()))

@login_required
def delete_comment(request,id):
    object = get_object_or_404(Comment, id=id)
    if request.user.username == object.author:
        object.delete()
        return redirect(object)
    else:
        return redirect(object)