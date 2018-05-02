from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from account.forms import EmailPostForm,UserRegistrationForm,UserEditForm
from django.urls import reverse_lazy
from account.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def test(request):
    return render(request,'my_account.html')

@login_required
def my_account(request):
    return render(request,'registration/my_account.html')


def post_share(request):
    # Отправка почты...ТЕСТ
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            subject = 'Radio_fm.ru. Отправитель {} ({})  "{}"'.format(cd['name'], cd['email'], cd['title'])
            message = '{}'.format(cd['comments'])
            send_mail(subject, message, 'bisqwit@yandex.ru',[cd['to']])
            sent = True
            return redirect(reverse_lazy('account:post_share'))
    else:
        form = EmailPostForm()
    return render(request, 'post/share.html', {'form': form,
                                                    'sent': sent})

def register(request):
    #Регистрация пользователя
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse_lazy('account:my_account'))
        else:
            return render(request,
                          'registration/edit.html',
                          {'user_form': user_form,
                           'profile_form': profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'registration/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


def view_profile(request,id):
    object = get_object_or_404(User, id=id)
    return render(request,'registration/view_profile.html',{'object':object})