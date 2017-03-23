from django.conf.urls import url, include
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/', include('lists.urls')),
]
