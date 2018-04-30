from django import forms
from django.contrib.auth.models import User
from account.models import Profile

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25,label='Имя отправителя')
    title = forms.CharField(max_length=30,label='Тема письма')
    email = forms.EmailField(label='Email отправителя')
    to = forms.EmailField(label='Получатель')
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Пароль еще раз', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_first_name(self):
        cd = self.cleaned_data
        if len(cd['first_name']) < 2:
            raise forms.ValidationError('Это поле должно содержать минимум 2 буквы')
        return cd['first_name'].title()
    def clean_last_name(self):
        cd = self.cleaned_data
        if len(cd['last_name']) < 2:
            raise forms.ValidationError('Это поле должно содержать минимум 2 буквы')
        return cd['last_name'].title()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')
    def clean_first_name(self):
        cd = self.cleaned_data
        if len(cd['first_name']) < 2:
            raise forms.ValidationError('Это поле должно содержать минимум 2 буквы')
        return cd['first_name'].title()
    def clean_last_name(self):
        cd = self.cleaned_data
        if len(cd['last_name']) < 2:
            raise forms.ValidationError('Это поле должно содержать минимум 2 буквы')
        return cd['last_name'].title()

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday', 'other_info')

