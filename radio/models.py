
from django.db import models

# Create your models here.
class Radioitem(models.Model):
    class Meta:
        verbose_name =          'Радиостанция'
        verbose_name_plural =   'Радиостанции'

    radio_name =        models.CharField(max_length=15,verbose_name='Название',unique=True)
    radio_description = models.TextField(verbose_name='Описание радиостанции')
    radio_flow =        models.URLField(blank=True,null=True,verbose_name="Ссылка на поток")
    radio_logo =        models.ImageField(upload_to='logo',verbose_name='Лого Радиостанции',blank=True)
    radio_view =        models.IntegerField(default=0,verbose_name='Просмотры')
    radio_likes=        models.IntegerField(default=0,verbose_name='Лайки')
    created =           models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Добавлен')
    changed =           models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='Редактирован')

    def __str__(self):
        return "%s" %self.radio_name

    def save(self,*args,**kwargs):
        try:
            this_record = Radioitem.objects.get(pk=self.id)
            if this_record.radio_logo != self.radio_logo:
                this_record.radio_logo.delete(save=False)
        except:
            pass
        super(Radioitem, self).save(*args, **kwargs)

    def delete(self,*args,**kwargs):
        self.radio_logo.delete(save=False)
        super(Radioitem,self).delete(*args,**kwargs)