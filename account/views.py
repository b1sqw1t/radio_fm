from django.shortcuts import render,redirect
from django.core.mail import send_mail
from account.forms import EmailPostForm
from django.urls import reverse_lazy


def test(request):
    return render(request,'my_account.html')

def my_account(request):
    return render(request,'registration/my_account.html')


def post_share(request):
    # Retrieve post by id
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
