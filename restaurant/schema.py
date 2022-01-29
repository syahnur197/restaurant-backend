from dataclasses import field
import graphene
from graphene_django import DjangoObjectType

from .models import Branch, Restaurant

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch


class Query(graphene.ObjectType):
    all_restaurants = graphene.List(RestaurantType)
    restaurant = graphene.Field(RestaurantType, id=graphene.ID())

    def resolve_all_restaurants(root, info):
        return Restaurant.objects.select_related('branches').all()
    
    def resolve_restaurant(root, info, id):
        return Restaurant.objects.get(pk=id)
    
schema = graphene.Schema(query=Query)