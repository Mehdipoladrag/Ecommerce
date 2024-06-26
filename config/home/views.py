from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
#from . import tasks
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from utils import IsAdminUserMixin
from .models import Category
from orders.forms import CartAddForm

# Create your views here.

class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, 'home/home.html', context)


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddForm()
        return render(request, 'home/detail.html', {'product': product, 'form': form})





class BucketHome(IsAdminUserMixin, View):
    template_name = 'home/bucket.html'

    def get(self, request):
       # objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name)


class DeleteBucketObject(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your object will be delete soon.', 'info')
        return redirect('home:bucket')


class DownloadBucketObject(IsAdminUserMixin, View):

    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, 'your download will start soon.', 'info')
        return redirect('home:bucket')
