import graphene
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .models import Branch, DiningType, MealType, OpeningHour, Product, Restaurant, CuisineType, User, UserProfile

class UserType(DjangoObjectType):
    class Meta:
        model = User

class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile

class CuisineTypeType(DjangoObjectType):
    class Meta:
        model = CuisineType

class MealTypeType(DjangoObjectType):
    class Meta:
        model = MealType

class DiningTypeType(DjangoObjectType):
    class Meta:
        model = DiningType

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch

class OpeningHourType(DjangoObjectType):
    class Meta:
        model = OpeningHour

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')
    all_cuisine_types = graphene.List(CuisineTypeType)
    all_meal_types = graphene.List(MealTypeType)
    all_dining_types = graphene.List(DiningTypeType)
    all_restaurants = graphene.List(RestaurantType)
    all_branches = graphene.List(BranchType)
    all_products = graphene.List(ProductType)

    user = graphene.Field(UserType, id=graphene.ID())
    user_profile = graphene.Field(UserProfileType, id=graphene.ID())

    cuisine_type = graphene.Field(CuisineTypeType, id=graphene.ID())
    meal_type = graphene.Field(MealTypeType, id=graphene.ID())
    dining_type = graphene.Field(DiningTypeType, id=graphene.ID())

    restaurant = graphene.Field(RestaurantType, id=graphene.ID())
    branch = graphene.Field(BranchType, id=graphene.ID())
    product = graphene.Field(ProductType, id=graphene.ID())


    # Resolve ALLS
    def resolve_all_cuisine_types(root, info):
        return CuisineType.objects.all()

    def resolve_all_meal_types(root, info):
        return MealType.objects.all()

    def resolve_all_dining_types(root, info):
        return DiningType.objects.all()


    def resolve_all_restaurants(root, info):
        return Restaurant.objects.prefetch_related('product_set', 'branch_set', 'branch_set__openinghour_set', 'meal_types', 'dining_types', 'cuisine_types').all()

    def resolve_all_branches(root, info):
        return Branch.objects.all()

    def resolve_all_products(root, info):
        return Product.objects.all()


    # Resolve one
    def resolve_user(root, info, id):
        return User.objects.select_related('userprofile', 'userprofile__restaurant').get(pk=id)
    def resolve_restaurant(root, info, id):
        return Restaurant.objects.prefetch_related('product_set', 'branch_set', 'branch_set__openinghour_set', 'meal_types', 'dining_types', 'cuisine_types').get(pk=id)
    def resolve_branch(root, info, id):
        return Branch.objects.get(pk=id)
    def resolve_product(root, info, id):
        return Product.objects.get(pk=id)

schema = graphene.Schema(query=Query)
