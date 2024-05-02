from django.urls import  path
from .views import HomeView,ArticleDetailView, AddPostView,UpdatePostView, DeletePostView

urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(),name='detail'),
    path('addPost/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name='update'),
    path('update_post/<int:pk>/remove/', DeletePostView.as_view(), name='delete')
]