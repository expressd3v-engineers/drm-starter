from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from backend.views import UserViewSet, GroupViewSet, error_400, error_403, error_404, error_500, home
from graphene_django.views import GraphQLView
from products.schema import schema

handler404 = error_404
handler400 = error_400
handler500 = error_500
handler403 = error_403

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', home, name='document'),
    path('', include('document.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
