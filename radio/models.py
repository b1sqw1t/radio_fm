
from django.db import models

# Create your models here.



class Country(models.Model):
    class Meta:
        verbose_name =          'Страна'
        verbose_name_plural =   'Страны'
        db_table = 'Country'

    name = models.CharField(max_length=40, blank=True, null=True, verbose_name='Страна')

    def __str__(self):
        return "%s" % self.name




class City(models.Model):
    class Meta:
        verbose_name =          'Город'
        verbose_name_plural =   'Города'
        db_table = 'City'

    name = models.CharField(max_length=50,blank=True,null=True,verbose_name='Город')
    country = models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name='Страна')

    def __str__(self):
        return "%s" %self.name

class Style(models.Model):
    class Meta:
        verbose_name =          'Жанр'
        verbose_name_plural =   'Жанры'
        db_table = 'Style'

    name = models.CharField(max_length=20, verbose_name='Название',unique=True)
    info = models.TextField(verbose_name='Информация о жанре')
    popular = models.BooleanField(default=False,verbose_name='Популярный')

    def __str__(self):
        return "%s" %self.name



class Radioitem(models.Model):
    class Meta:
        verbose_name =          'Радиостанция'
        verbose_name_plural =   'Радиостанции'
        db_table = 'Radioitem'
        ordering = ['id']


    radio_name =        models.CharField(max_length=40,verbose_name='Название',unique=True)
    radio_description = models.TextField(verbose_name='Описание радиостанции')
    radio_style =       models.ForeignKey(Style,on_delete=models.CASCADE,verbose_name='Жанр')
    radio_flow =        models.URLField(blank=True,null=True,verbose_name="Ссылка на поток")
    radio_logo =        models.ImageField(upload_to='logo',verbose_name='Лого Радиостанции',blank=True)
    radio_logo_link =   models.URLField(blank=True,verbose_name='Ссылка на изображение',max_length=200)
    radio_view =        models.IntegerField(default=0,verbose_name='Просмотры')
    radio_likes=        models.IntegerField(default=0,verbose_name='Лайки')
    radio_city =        models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='Город',blank=True,null=True)
    radio_error=        models.BooleanField(verbose_name='Ошибка',default=False)
    created =           models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Добавлен')
    changed =           models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='Редактирован')

    def get_absolute_url(self): #TODO: Доработать!!!!!
        from django.urls import reverse
        return reverse('radio:radioview', args=[str(self.id)])
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


class Comment(models.Model):
    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural =   'Комментарии'


    radiostation = models.ForeignKey(Radioitem,on_delete=models.SET_NULL,null=True, related_name='comments',verbose_name='Радиостанция')
    author  = models.CharField(max_length=40,verbose_name='Автор')
    email   = models.EmailField(verbose_name='e-mail')
    text    = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Создан')
    changed = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Изменен')
    visible = models.BooleanField(default=True,verbose_name='Отображать')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('radio:radioview', args=[str(self.radiostation.id)])

    def __str__(self):
        return 'Пользователь: {}. Комментарий: {} '.format(self.author,self.text)