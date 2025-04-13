from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # 🏠 Home page
    path('authors/', views.author_list, name='author_list'),  # 👨‍🎨 Authors list
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),  # 👨‍🎨 Author detail
    path('books/', views.book_list, name='book_list'),  # 📚 Books list
    path('books/<int:pk>/', views.book_detail, name='book_detail'),  # 📖 Book detail
    path('categories/', views.category_list, name='category_list'),  # 🏷️ Categories list
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),  # 🏷️ Category detail

    path('login/', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

