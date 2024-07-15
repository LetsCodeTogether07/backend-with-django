from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from random import randint

products: list[dict] = []

@api_view(http_method_names=["GET"])
def get_products(request: Request):
    return Response(data=products, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def get_product(request: Request, id: int):
    response = None
    for product in products:
        if product["id"] == id:
            response = product
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["POST"])
def add_product(request: Request):
    data = request.data
    data["id"] = randint(1,10000)
    products.append(data)
    return Response(data=products,status=status.HTTP_201_CREATED)

@api_view(http_method_names=["PUT"])
def update_product(request: Request, id: int):
    data = request.data
    response = None
    for product in products:
        if product["id"] == id:
            response = product
            product.update(data)
    return Response(data=response,status=status.HTTP_202_ACCEPTED)

@api_view(http_method_names=["DELETE"])
def delete_product(request: Request, id: int):
    for product in products:
        if product["id"] == id:
            products.remove(product)
    return Response(data=None,status=status.HTTP_204_NO_CONTENT)
