from django.urls import path

from . import views

app_name = 'link'

urlpatterns = [
	path('', views.links, name='links'),
	path('create-link/', views.create_link, name='create_link'),
	path('categories', views.categories, name='categories'),
	path('categories/create-category/', views.create_category, name='create_category'),

]