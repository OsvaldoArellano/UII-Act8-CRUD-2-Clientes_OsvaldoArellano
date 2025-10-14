from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

# Create your views here.
# Listar clientes
def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

# Ver cliente
def ver_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'listar_clientes.html', {'cliente': cliente})

# Agregar cliente
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']

        Cliente.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, email=email, direccion=direccion)
        return redirect('index')
    return render(request, 'agregar_cliente.html')

# Editar cliente
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.direccion = request.POST['direccion']
        cliente.save()
        return redirect('index')
    return render(request, 'editar_cliente.html', {'cliente': cliente})

# Borrar cliente
def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('index')
    return render(request, 'borrar_cliente.html', {'cliente': cliente})
