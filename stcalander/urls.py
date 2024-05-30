from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'stcalander'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('all_events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('', views.index, name='index'),
]
