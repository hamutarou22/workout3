from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newevent/', views.neweventfunc, name='newevent'),
    path('record/', views.recordfunc, name='record'),
    path('change/<int:pk>', views.changefunc, name='change'),
    path('table/', views.tablefunc, name='table'),
]