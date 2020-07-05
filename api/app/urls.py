from django.conf.urls import url
from . import views
from rest_framework.documentation import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

schema_view = get_schema_view(title="Entrega Colaborativa", description="API for the Entrega Compartilhada service",
                              version="1.0.0",
                              renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

app_name = "api-docs"

urlpatterns = [
    url('^$', schema_view, name="docs"),
    url(r'^products/$', views.ProductListView.as_view(), name='product-list'),
    url(r'^products/<int:id>$', views.ProductListView.as_view(), name='product'),
    url(r'^sellers/$', views.SellerListView.as_view(), name='seller-list'),
    url(r'^sellers/<int:id>$', views.SellerView.as_view(), name='seller'),
    url(r'^orders/$', views.OrderListView.as_view(), name='order-list'),
    url(r'^orders/<int:id>$', views.OrderView.as_view(), name='order'),
    url(r'^routes/$', views.RouteListView.as_view(), name='route-list'),
    url(r'^routes/<int:id>$', views.RouteView.as_view(), name='route'),

]
