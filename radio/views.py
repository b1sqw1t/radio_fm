from django.shortcuts import render
from radio.models import Radioitem,City,Country
from django.views.generic import list,base
class index(list.ListView):
    template_name = 'index.html'
    model = Radioitem
    paginate_by = 4

    def get_context_data(self,**kwargs):
        context= super(index,self).get_context_data(**kwargs)
        context['ccity'] = 'БЛЯДЬ'
        return context

class viewradio(base.TemplateView):
    template_name = 'index22.html'
    def get(self,request,*args,**kwargs):
        try:
            self.radioid = self.args[0]
            print(self.radioid)
        except:
            pass
        return super(viewradio,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(viewradio,self).get_context_data(**kwargs)
        context['radioitem'] = Radioitem.objects.get(id=self.radioid)
        context['title'] = context['radioitem'].radio_name
        context['ccity'] = 'CTLLLAAA'
        return context
    # pk_url_kwarg = args[0]
    #
    # def get(self,request,*args,**kwargs):
    #     self.radio_id = self.args[0]
    #     return super(viewradio,self).get(request,*args,**kwargs)

    # def get_queryset(self):
    #     return Radioitem.objects.get(id=self.radio_id)

def index2(request):
    radioitem = Radioitem.objects.get(id=1)
    a = City.objects.get(name=radioitem.radio_city)
    b = a.country
    # b = Country.objects.get()
    # ccity = b.city_set.all()
    return render(request,'index22.html',locals())