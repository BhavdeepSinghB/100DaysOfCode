from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questionid>/', views.detail, name='detail'),
    path('<int:questionid>/results/', views.results, name='results'),
    path('<int:questionid>/vote/', views.vote, name='vote'),
]