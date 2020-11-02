from django.urls import include, path

from app.models import Clientes
from app.views import lista_clientes

from .views import (create_product, delete_product, lista_clientes,
                    update_product)

urlpatterns = [
    path('lista', lista_clientes, name='lista_clientes'),
    path('', create_product, name='create_products'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
    #path('boot', form_boot, name='form_boot'),
]
