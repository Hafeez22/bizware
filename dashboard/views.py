from django.shortcuts import render
from django.contrib import messages
from customer.models import customer,suppliers
from .models import products,size
import datetime

# Create your views here.
def mainDashboard(request):
    count_customers = customer.objects.all().count()
    count_suppliers = suppliers.objects.all().count()
    count_products = products.objects.all().count()
    context = {'customers' : count_customers,
               'products':count_products,
                "suppliers":count_suppliers,
              }
    return render(request, 'dashboard.html', context)


def product(request):
    options = size.objects.all()
    productstable = products.objects.all()
    choices = products.choices

    if request.method == "POST":
        if "addProduct" in request.POST:
            pname = request.POST.get('pname')
            psize = request.POST.get('psize')
            pzinc = request.POST.get('pzinc')
            pprice = request.POST.get('pprice')
            psprice = request.POST.get('psprice')

            products.objects.create(
                date = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S%z}',
                pname = pname,
                pzinc = pzinc,
                psize_id = psize,
                pprice = pprice,
                psellingprice = psprice
            )

            messages.info(request, "Product added successfully")

        elif "updateProduct" in request.POST:
            pass
        
    context = {'sizes' : options,
               'products':productstable,
               'zincs': choices}
    return render(request, 'products.html', context)