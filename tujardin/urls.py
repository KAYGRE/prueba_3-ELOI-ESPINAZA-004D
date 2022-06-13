from django.urls import path
from .views import index, empresa, login, products, register, clientform, prodform

urlpatterns= [
path('', index, name="index"),
path('empresa/', empresa, name="empresa"),
path('login/', login, name="login"),
path('products/', products, name="products"),
path('register/', register, name="register"),
path('clientform/', clientform, name="clientform"),
path('prodform/', prodform, name="prodform"),
]

