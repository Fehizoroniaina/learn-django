from django.urls import path
from . import views


app_name='blog'

urlpatterns = [
    path('create/',views.PostCreateView.as_view(),
         name = 'post_create'),
    path("",views.PostListView.as_view(),name='all'),
    path('delete/<slug:slug>',views.PostDeleteView.as_view(),name="post_delete"),
    path('update/<slug:slug>',views.PostUpdatedView.as_view(),name= "post_update"),
    path('read/<slug:slug>',views.PostDetailView.as_view(),name="post_detail"),


]