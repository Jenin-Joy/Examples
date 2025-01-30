from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.

def getdata(parent):
    cat = tbl_category.objects.filter(parent=parent)
    for i in cat:
        i.data = getdata(i.id)
    return cat

def category(request):
    category = tbl_category.objects.all()
    for i in category:
        data = getdata(i.id)
        i.data = data
    if request.method == "POST":
        parent = request.POST.get('sel_parent')
        if parent:
            tbl_category.objects.create(category_name=request.POST.get("txt_category"),parent=tbl_category.objects.get(id=request.POST.get('sel_parent')))
        else:
            tbl_category.objects.create(category_name=request.POST.get("txt_category"))
        return redirect("Admin:category")
    return render(request, "Admin/Category.html", {"category": category})