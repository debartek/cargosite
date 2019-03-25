from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import OrderForm

def package_list(request):
    packages = Package.objects.all().order_by('pack_type')
    return render(request,'drobnica/package_list.html',{'packages' : packages})

def consignee_list(request):
    consignees = Consignee.objects.all().order_by('name')
    return render(request, 'drobnica/consignees.html', {'consignees':consignees})

def order_detail(request, pk):
    order = get_object_or_404(Order,pk=pk)
    return render(request,'drobnica/order_detail.html',{'order':order})

def order_new(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('order_detail',pk=order.pk)
    else:
        form = OrderForm()
        return render(request, 'drobnica/order_new.html', {'form':form})

def order_edit(request,pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer=request.user
            order.save()
        return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request,'drobnica/order_new.html', {'form':form})