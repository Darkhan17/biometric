from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


from .serializers import RestaurantSerializer,PizzaSerializer
from .models import Restaurant,Pizza

# Create your views here.


@api_view(['GET', 'POST'])
def restaurantList(request):
    if request.method == "GET":
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=200)
    elif request.method == "POST":
        serializer = RestaurantSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)

class getRestaurant(APIView):
    def get_restaurant(self,pk):
        try:
            restaurant = Restaurant.objects.get(id = pk)
            return restaurant
        except Restaurant.DoesNotExist as error:
            raise Http404

    def get(self, request, pk):
        restaurant = self.get_restaurant(pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        restaurant = self.get_restaurant(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        restaurant = self.get_restaurant(pk)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

    def delete(self, request, pk):
        restaurant = self.get_restaurant(pk)
        restaurant.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def pizzaList(request):
    if request.method == "GET":
        pizza = Pizza.objects.all()
        serializer = PizzaSerializer(pizza, many=True)
        return Response(serializer.data, status=200)
    elif request.method == "POST":
        serializer = PizzaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors)

class getPizza(APIView):
    def get_pizza(self,pk):
        try:
            pizza = Pizza.objects.get(id = pk)
            return pizza
        except Restaurant.DoesNotExist as error:
            return Response({'message': str(error)}, status=400)

    def get(self, request, pk):
        pizza = self.get_pizza(pk)
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        pizza = self.get_pizza(pk)
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        pizza = self.get_pizza(pk)
        serializer = PizzaSerializer(pizza, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

    def delete(self, request, pk):
        pizza = self.get_pizza(pk)
        pizza.delete()
        return Response(status=204)
