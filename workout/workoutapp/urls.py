from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:pk>', views.detailfunc, name='detail'),
    path('record/', views.recordfunc, name='record'),
    path('change/<int:pk>', views.changefunc, name='change'),
    path('table/<int:pk>', views.tablefunc, name='table'),
]