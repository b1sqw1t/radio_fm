from django.shortcuts import render,redirect
from radio.models import Radioitem,City,Country
from django.views.generic import list,base
class index(list.ListView):
    template_name = 'index.html'
    model = Radioitem
    paginate_by = 12


    def get_context_data(self,**kwargs):
        context= super(index,self).get_context_data(**kwargs)
        return context

class viewradio(base.TemplateView):
    template_name = 'radioview.html'


    def get(self,request,*args,**kwargs):
        try:
            self.radioid = self.kwargs['radioid']
        except:
            return redirect('index')
        return super(viewradio,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(viewradio,self).get_context_data(**kwargs)
        context['radioitem'] = Radioitem.objects.get(id=self.radioid)
        context['title'] = context['radioitem'].radio_name
        return context

    def get_queryset(self):
        return Radioitem.objects.get(id=self.radioid)

def index2(request):
    radioitem = Radioitem.objects.get(id=1)
    a = City.objects.get(name=radioitem.radio_city)
    b = a.country
    # b = Country.objects.get()
    # ccity = b.city_set.all()
    return render(request,'index22.html',locals())