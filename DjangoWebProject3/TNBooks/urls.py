
from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url ('authors/', views.authors),
url ('publish/', views.publish),
url ('genre/', views.genre),
url ('book/', views.book),
url('b/', views.b)
]


