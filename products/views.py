import imp
from turtle import back


import requests
from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Products
from .forms import ProductForm
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import Products


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
def editProducts(request):
    myproducts = Products.objects.all().values()
    template = loader.get_template('p_edit.html')
    context = {
    'myproducts': myproducts,
  }
    if request.method == "POST":
        form = request.POST
        p_id = form['p_id']
        product = Products()
        product.id = p_id
        product.delete()
    return HttpResponse(template.render(context, request))
def edit_post(request, id):
    form = ProductForm(request.POST)
    req = request
    post = get_object_or_404(Products, id=id)
    if request.method == 'GET':
        myproducts = Products.objects.all().values()
        x = str(req).split(' ')
        y = x[2].split('/')
        z = y[3]

        for i in myproducts:
            if str(i['id']) == str(z):
                myproduct = i
        return render(request, 'product-edit.html', {'form': form, 'product':myproduct})
    if request.method == "POST":
        myproducts = Products.objects.all().values()
        inde = 0
        for x in myproducts:
            if str(x['id']) == str(request.POST['p_id']):
                i = Products.objects.all()[inde]
                i.p_name= request.POST['p_name']
                i.p_desc= request.POST['p_desc']
                i.p_owner= request.POST['p_owner']
                i.p_stock= request.POST['p_stock']
                i.p_category= request.POST['p_category']
                i.p_price= request.POST['p_price']
                i.save()
            inde = inde + 1
        template = loader.get_template('p_edit.html')
        context = {
        'myproducts': myproducts,
        }
        return HttpResponse(template.render(context, request))
