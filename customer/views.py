
from django.shortcuts import render
from .models import customer,suppliers
from django.contrib import messages
from django.db.models import Q
import datetime
# Create your views here.


def customerDashboard(request):
    customers = customer.objects.all()
    searchquery = ""
    if request.method == "POST":
        if "add" in request.POST:
            dt = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S%z}'
            name = request.POST.get("name")
            cphone = request.POST.get("number")
            mail = request.POST.get("email")
            caddress = request.POST.get("address")
            cbalance = request.POST.get("balance")
            customer.objects.create(
                cname = name,
                cphone = cphone,
                cmail = mail,
                caddress = caddress,
                cbalance = cbalance,
                date = dt
            )
            messages.success(request, "Customer added successfully")
            
        
        elif "update" in request.POST:
            cid = request.POST.get("id")
            name = request.POST.get("name")
            cphone = request.POST.get("number")
            mail = request.POST.get("email")
            caddress = request.POST.get("address")
            cbalance = request.POST.get("balance")

            updateCustomer = customer.objects.get(cid = cid)
            updateCustomer.cname = name
            updateCustomer.cphone = cphone
            updateCustomer.cmail = mail
            updateCustomer.caddress = caddress
            updateCustomer.cbalance = cbalance
            updateCustomer.save()

            messages.success(request, "Customer updated successfully")
            
           
        elif "delete" in request.POST:
            cid = request.POST.get("id")
            customer.objects.get(cid = cid).delete()

            messages.success(request, "Customer deleted successfully")

        elif "search" in request.POST:
            searchquery = request.POST.get("search")
            customersearch = customer.objects.filter(Q(cname__icontains = searchquery) | Q(cmail__icontains = searchquery))    
            context = {"customers": customersearch, "query" : searchquery}
            return render(request, 'cindex.html', context = context)


   
    context = {"customers": customers, "query" : searchquery}
    return render(request, 'cindex.html', context = context)


def supplier(request):
    supplier = suppliers.objects.all()

    if request.method == "POST":
        if "addSupplier" in request.POST :
            sdate = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S%z}'
            sname = request.POST.get("sname")
            sphone = request.POST.get("snumber")
            smail = request.POST.get("semail")
            saddress = request.POST.get("saddress")
            sbalance = request.POST.get("sbalance")
            
            suppliers.objects.create(
                date = sdate,
                sname = sname,
                sphone = sphone,
                smail = smail,
                saddress = saddress,
                sbalance = sbalance
            )
            messages.info(request, "Supplier successfully create")

        elif "updateSupplier" in request.POST:
            sid = request.POST.get("sid")
            sname = request.POST.get("sname")
            sphone = request.POST.get("snumber")
            smail = request.POST.get("semail")
            saddress = request.POST.get("saddress")
            sbalance = request.POST.get("sbalance")

            updateSupplier = suppliers.objects.get(sid = sid)
            updateSupplier.sname = sname
            updateSupplier.sphone = sphone
            updateSupplier.smail = smail
            updateSupplier.saddress = saddress
            updateSupplier.sbalance = sbalance
            updateSupplier.save()

            messages.info(request, "Supplier successfully updated")

        elif "deleteSupplier" in request.POST:

            sid = request.POST.get("sid")
            suppliers.objects.get(sid = sid).delete()

            messages.info(request, "Supplier deleted successfully")
            
    context = {"suppliers": supplier}
    return render(request, 'sindex.html', context = context)
