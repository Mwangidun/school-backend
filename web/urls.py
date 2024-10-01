from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cbc/', views.cbc, name='cbc'),
    path('daycare/', views.daycare, name='daycare'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/add/', views.add_gallery, name='add_gallery'),
    path('login/', views.login, name='login'),
    path('news/', views.news, name='news'),
    path('news/add/', views.add_news, name='add_news'),
    path('nursery/', views.nursery, name='nursery'),
    path('pp1/', views.pp1, name='pp1'),
    path('pp2/', views.pp2, name='pp2'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('staff/', views.staff, name='staff'),
    path('enroll/', views.enroll_view, name='enroll'),
    
]
