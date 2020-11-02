from django.shortcuts import render, redirect
from .models import Clientes
from .forms import ProductForm


def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'index.html', {'clientes': clientes})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('create_products')

    return render(request, 'product-form.html', {'form': form})


def update_product(request, id):
    cliente = Clientes.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('create_products')

    return render(request, 'product-form.html', {'form': form, 'cliente': cliente})


def delete_product(request, id):
    cliente = Clientes.objects.get(id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('create_products')

    return render(request, 'prod-delete-confirm.html', {'cliente': cliente})
