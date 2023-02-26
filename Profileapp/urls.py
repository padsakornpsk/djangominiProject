from django.urls import path
from django.http import HttpResponse
from Profileapp import views
from Profileapp.views import contentChart

urlpatterns = [
    path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('restaurantsList', views.restaurantsList, name='restaurantsList'),
    path('hotelListList', views.hotelList, name='hotelList'),
    path('recipeList', views.recipeList, name='recipeList'),
    path('categoriesList', views.categoriesList, name='categoriesList'),

    path('showhotel', views.showhotel, name='showhotel'),
    path('showrestaurants', views.showrestaurants, name='showrestaurants'),
    path('showrecipe', views.showrecipe, name='showrecipe'),
    path('showContent', views.showContent, name='showContent'),
    path('addContent', views.addContent, name='addContent'),
    path('addCategory', views.addCategory, name='addCategory'),
    path('<cont_id>/updateContent', views.updateContent, name='updateContent'),
    path('<cont_id>/deleteContent', views.deleteContent, name='deleteContent'),
    path('<cat_id>/updateCategory', views.updateCategory, name='updateCategory'),
    path('<cat_id>/deleteCategory', views.deleteCategory, name='deleteCategory'),

    path('contentChart/', contentChart, name='contentChart'),
]


