from django.conf.urls import url
from basic_app import views

# Template urls!
app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.UserProListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.UserProDetailView.as_view(), name='detail'),
    url(r'^create/$', views.UserProCreateView.as_view(), name='create'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
