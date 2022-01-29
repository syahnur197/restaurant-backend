from dataclasses import field
from itertools import product
import graphene
from graphene_django import DjangoObjectType

from .models import Branch, Product, Restaurant, Cuisine

class CuisineType(DjangoObjectType):
    class Meta:
        model = Cuisine

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class Query(graphene.ObjectType):
    all_cuisines = graphene.List(CuisineType)
    all_restaurants = graphene.List(RestaurantType)
    all_branchess = graphene.List(BranchType)
    all_products = graphene.List(ProductType)

    cuisine = graphene.Field(CuisineType, id=graphene.ID())
    restaurant = graphene.Field(RestaurantType, id=graphene.ID())
    branch = graphene.Field(BranchType, id=graphene.ID())
    product = graphene.Field(ProductType, id=graphene.ID())


    def resolve_all_cuisines(root, info):
        return Cuisine.objects.all()

    def resolve_all_restaurants(root, info):
        return Restaurant.objects.all()
   
    def resolve_all_branches(root, info):
        return Branch.objects.all()

    def resolve_all_products(root, info):
        return Product.objects.all()


    
    def resolve_cuisine(root, info, id):
        return Cuisine.objects.get(pk=id)
    def resolve_restaurant(root, info, id):
        return Restaurant.objects.get(pk=id)
    def resolve_branch(root, info, id):
        return Branch.objects.get(pk=id)
    def resolve_product(root, info, id):
        return Product.objects.get(pk=id)
    
schema = graphene.Schema(query=Query)