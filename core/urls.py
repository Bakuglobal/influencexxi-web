from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('blog-post/<int:pk>', views.PostDetail.as_view(), name='detail'),

]