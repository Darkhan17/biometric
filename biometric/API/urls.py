from django.urls import path
from .views import restaurantList,getRestaurant,getPizza, pizzaList

urlpatterns = [
    path('restaurants/', restaurantList),
    path('restaurants/<int:pk>/', getRestaurant.as_view()),
    path('pizzas/', pizzaList),
    path('pizzas/<int:pk>/', getPizza.as_view())
]

