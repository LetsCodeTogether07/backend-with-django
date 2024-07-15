from django.urls import path
from . import views

urlpatterns = [
   path(route="products/", view=views.get_products, name="get_products"),
   path(route="products/add/", view=views.add_product, name="add_product"),
   path(route="products/<int:id>", view=views.get_product, name="get_product"),
   path(route="products/update/<int:id>", view=views.update_product, name="update_product"),
   path(route="products/delete/<int:id>", view=views.delete_product, name="delete_product"),
]
