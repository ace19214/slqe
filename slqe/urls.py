from django.conf.urls import url 
from slqe import views 
 
urlpatterns = [
    url(r'^users', views.user_list),
    url(r'^users/{id}', views.user_detail),
]