import graphene
from graphene_django import DjangoObjectType
from .models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = (
            'id',
            'description',
            'status',
            'created_at',
            'updated_at',
        )


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    products = graphene.List(ProductType)

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()


schema = graphene.Schema(query=Query)
