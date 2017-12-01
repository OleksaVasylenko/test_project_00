from django.conf.urls import url
from user import views


urlpatterns = (
    url(r'^sign_up$', views.SignUp.as_view(), name='sign_up'),
    url(r'^sign_in$',views.SignIn.as_view(), name='sign_in_page'),
    url(r'^sign_out$', views.SignOut.as_view(), name='sign_out'),
    url(r'^activate/(?P<uid_b64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.Activate.as_view(), name='activate'),
)
