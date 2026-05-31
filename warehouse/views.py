from django.contrib.messages import success
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from warehouse.models import Product, Category, Book
from warehouse.forms import ContactForm, CreateBookForm, UpdateBookForm


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request,'list.html',{'products':products})

def categories_list(request):
    category = Category.objects.all()
    return render(request,'categories.html',{'category':category})

def category_products(request,pk):
    products = Product.objects.filter(category_id=pk)
    return render(request,'category_products.html',{'products':products})


def success_message(request):
    return render(request,'success.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})


# ---------------------------CRUD---------------------

def book_list(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{'book_list':books})

def detail_view(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request,'detail.html',{'book':book})

def create_view(request):
    if not request.user.has_perm('warehouse.add_book'):
        return HttpResponse("Sizda ruxsat yo'q")

    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = CreateBookForm()
    return render(request,'create_book.html',{'form':form})

def update_view(request,pk):
    update_book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        form = UpdateBookForm(request.POST or None,instance=update_book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = UpdateBookForm(instance=update_book)
    return render(request,'update_book.html',{'form':form})

def delete_view(request,pk):
    del_book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        del_book.delete()
        return redirect('book_list')
    return render(request,'delete_book.html',{'del_book':del_book})








