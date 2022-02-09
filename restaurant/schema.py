import graphene
from graphene_django import DjangoObjectType

from .models import Branch, Product, Restaurant, CuisineType, User, UserProfile


class UserType(DjangoObjectType):
    class Meta:
        model = User

class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile

class CuisineType(DjangoObjectType):
    class Meta:
        model = CuisineType

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
    all_cuisine_types = graphene.List(CuisineType)
    all_restaurants = graphene.List(RestaurantType)
    all_branchess = graphene.List(BranchType)
    all_products = graphene.List(ProductType)

    user = graphene.Field(UserType, id=graphene.ID())
    user_profile = graphene.Field(UserProfileType, id=graphene.ID())
    cuisine_type = graphene.Field(CuisineType, id=graphene.ID())
    restaurant = graphene.Field(RestaurantType, id=graphene.ID())
    branch = graphene.Field(BranchType, id=graphene.ID())
    product = graphene.Field(ProductType, id=graphene.ID())


    def resolve_all_cuisine_types(root, info):
        return CuisineType.objects.all()

    def resolve_all_restaurants(root, info):
        return Restaurant.objects.all()

    def resolve_all_branches(root, info):
        return Branch.objects.all()

    def resolve_all_products(root, info):
        return Product.objects.all()



    def resolve_user(root, info, id):
        return User.objects.select_related('userprofile', 'userprofile__restaurant').get(pk=id)
    def resolve_restaurant(root, info, id):
        return Restaurant.objects.prefetch_related('product_set').get(pk=id)
    def resolve_branch(root, info, id):
        return Branch.objects.get(pk=id)
    def resolve_product(root, info, id):
        return Product.objects.get(pk=id)

schema = graphene.Schema(query=Query)
