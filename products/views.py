from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Products
from .forms import ProductForm
from django.http import HttpResponseRedirect


def products(request):
    myproducts = Products.objects.all().values()
    template = loader.get_template('p_view.html')
    context = {
    'myproducts': myproducts,
  }
    return HttpResponse(template.render(context, request))

def addProducts(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = Products() #gets new object
            obj.p_name= form.cleaned_data['p_name']
            obj.p_desc= form.cleaned_data['p_desc']
            obj.p_owner= form.cleaned_data['p_owner']
            obj.p_stock= form.cleaned_data['p_stock']
            obj.p_category= form.cleaned_data['p_category']
            obj.p_price= form.cleaned_data['p_price']
            obj.save()
            print(obj)
            return HttpResponseRedirect('/products/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm()

    return render(request, 'p_add.html', {'form': form})