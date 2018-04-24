from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25,label='Имя отправителя')
    title = forms.CharField(max_length=30,label='Тема письма')
    email = forms.EmailField(label='Email отправителя')
    to = forms.EmailField(label='Получатель')
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)