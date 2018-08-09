# accounts urls

from django.urls import path
from accounts.views import login, register, logout, profile
# from django.core.urlresolvers import reverse_lazy
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns=[
    path('login', login, name="login"),
    path('register', register, name='register'),
    path('logout', logout, name="logout"),
    path('profile', profile, name="profile"),
    # path('password-reset/$', password_reset,
    #     {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    # path('password-reset/done/$', password_reset_done, name='password_reset_done'),
    # path('password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    #     {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    # path('password-reset/complete/$', password_reset_complete, name='password_reset_complete'),
    ]