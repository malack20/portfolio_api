from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/projects/', views.projects_api_view, name='projects-api'),
    path('api/blog-posts/', views.blog_posts_api_view, name='blog-posts-api'),
    path('api/skills/', views.skills_api_view, name='skills-api'),
    # New URL for the contact form
    path('api/contact/', views.contact_form_api, name='contact-api'),
]