from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from cart.models import CartItem, Cart
from cart.serializers import CartItemSerializer


# Create your views here.

class CartItemListCreateApiView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart.cartitem_set.all()

    def perform_create(self, serializer):
        cart = Cart.objects.create(user=self.request.user)
        serializer.save(cart=cart)


class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = generics.get_object_or_404(queryset, cart__user=self.request.user, pk=self.kwargs['pk'])
        return obj


class CartClearAPIView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.cartitem_set.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
