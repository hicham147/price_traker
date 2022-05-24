from django.shortcuts import render,redirect
from .forms import AddLinkform,AmazonAddlink,NiceoneAddlink,XciteAddlink
from .models import Link,Niceone,Amazon,Xcite
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy

def home(request):
    context = {"context":"context"}
    return render(request, 'home.html',context)

def about(request):
    context = {"context":"context"}
    return render(request, 'about.html',context)

def amazon(request):
    items_descount = 0
    errors = None

    form = AmazonAddlink(request.POST or None)     # ?

    if request.method =='POST':
        if request.method == 'POST':
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request,'Added a new URL !')
            except AttributeError:
                errors = "opps...the name or the price not correct"
            except:
                errors = "opps...something went wrong"
        
    form = AmazonAddlink()
    queryset = Amazon.objects.all()   # go inside the form you  jest createDocumentFragment (مجموعة الاستعلام)
    items_number = queryset.count()
    
    if items_number > 0:
        discoubt_item_list = []
        for item in queryset:
            if item.old_price > item.current_price:
                discoubt_item_list.append(item)
    
        items_descount = len(discoubt_item_list)

    context = {
        "items_descount":items_descount,
        "errors":errors,
        "items_number":items_number,
        "qr":queryset,
        "form":form,
    }

    return render(request,"links/amazon.html",context)

def ihreb(request):
    items_descount = 0
    errors = None

    form = AddLinkform(request.POST or None)     # ?

    if request.method =='POST':
        if request.method == 'POST':
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request,'Added a new URL !')
            except AttributeError:
                errors = "opps...the name or the price not correct"
            except:
                errors = "opps...something went wrong"
        
    form = AddLinkform()
    queryset = Link.objects.all()   # go inside the form you  jest createDocumentFragment (مجموعة الاستعلام)
    items_number = queryset.count()
    
    if items_number > 0:
        discoubt_item_list = []
        for item in queryset:
            if item.old_price > item.current_price:
                discoubt_item_list.append(item)
    
        items_descount = len(discoubt_item_list)

    context = {
        "items_descount":items_descount,
        "errors":errors,
        "items_number":items_number,
        "qr":queryset,
        "form":form,
    }

    return render(request,"links/ihreb.html",context)


def nicone(request):
    items_descount = 0
    errors = None

    form = NiceoneAddlink(request.POST or None)     # ?

    if request.method =='POST':
        if request.method == 'POST':
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request,'Added a new URL !')
            except AttributeError:
                errors = "opps...the name or the price not correct"
            except:
                errors = "opps...something went wrong"
        
    form = NiceoneAddlink()
    queryset = Niceone.objects.all()   # go inside the form you  jest createDocumentFragment (مجموعة الاستعلام)
    items_number = queryset.count()
    
    if items_number > 0:
        discoubt_item_list = []
        for item in queryset:
            if item.old_price > item.current_price:
                discoubt_item_list.append(item)
    
        items_descount = len(discoubt_item_list)
    ordering = ['-created']    # Order By .....
    context = {
        "items_descount":items_descount,
        "errors":errors,
        "items_number":items_number,
        "qr":queryset,
        "form":form,
    }

    return render(request,"links/nicone.html",context)


def xcite(request):
    items_descount = 0
    errors = None

    form = XciteAddlink(request.POST or None)     # ?

    if request.method =='POST':
        if request.method == 'POST':
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request,'Added a new URL !')
            except AttributeError:
                errors = "opps...the name or the price not correct"
            except:
                errors = "opps...something went wrong"
        
    form = XciteAddlink()
    queryset = Xcite.objects.all()   # go inside the form you  jest createDocumentFragment (مجموعة الاستعلام)
    items_number = queryset.count()
    
    if items_number > 0:
        discoubt_item_list = []
        for item in queryset:
            if item.old_price > item.current_price:
                discoubt_item_list.append(item)
    
        items_descount = len(discoubt_item_list)
    ordering = ['-created']    # Order By .....
    context = {
        "items_descount":items_descount,
        "errors":errors,
        "items_number":items_number,
        "qr":queryset,
        "form":form,
    }

    return render(request,"links/xcite.html",context)



def ihrab_update_prices(request):
    qr = Link.objects.all()
    for q in qr:
        q.save()
    messages.success(request,'successfully updated !')
    return redirect("ihreb")



def amazon_update_prices(request):
    qr = Amazon.objects.all()
    for q in qr:
        q.save()
    messages.success(request,'successfully updated !')

    return redirect("amazon")

def nicone_update_prices(request):
    qr = Niceone.objects.all()
    for q in qr:
        q.save()
    messages.success(request,'successfully updated !')
    return redirect("nicone")

def xcite_update_prices(request):
    qr = Xcite.objects.all()
    for q in qr:
        q.save()
    messages.success(request,'successfully updated !')
    return redirect("xcite")



class AmazonDeleteViwes(DeleteView):
    model = Amazon
    success_url = reverse_lazy('amazon')
    template_name = 'links/amazon_confirm_delete.html'

    

class NiceonedeletViews(DeleteView):
    model = Niceone
    success_url = reverse_lazy('nicone')
    template_name = 'links/amazon_confirm_delete.html'


class IhrebdeletViews(DeleteView):
    model = Link
    success_url = reverse_lazy('ihreb')
    template_name = 'links/amazon_confirm_delete.html'


class XcitedeletViews(DeleteView):
    model = Xcite
    success_url = reverse_lazy('xcite')
    template_name = 'links/amazon_confirm_delete.html'