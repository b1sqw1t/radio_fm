from django.contrib             import admin
from django.urls                import path,re_path,include
from account import views
from django.urls import reverse_lazy
from django.contrib.auth.views        import login,logout,password_change,password_change_done,\
            PasswordChangeView,PasswordChangeDoneView,PasswordResetView


app_name = 'account'

urlpatterns = [
    re_path('^test',                        views.post_share,       name='post_share'),
    re_path('^index',                       views.test,            name='test'),
    re_path('^profile',                     views.my_account,      name='my_account'),
    re_path('^login$',                      login,                 name='login'),
    re_path('^logout/$',                    logout,                name='logout'),
    re_path('^password-change/$',           PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    re_path('^password-change/done/$',      PasswordChangeDoneView.as_view(),  name='password_change_done'),
    #re_path('^password-reset/$',            PasswordResetView.as_view(), name='password-reset')

]