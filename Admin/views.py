from django.shortcuts import render,redirect
from Admin.models import *
from django.http import JsonResponse
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

def deletecategory(request, id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category")

def search(request):
    cat = tbl_category.objects.filter(parent=None)
    return render(request, "Admin/Search.html", {"cat": cat})

# def ajaxcategory(request):
#     subcat = tbl_category.objects.filter(parent=request.GET.get("did"))
#     return render(request, "Admin/AjaxCategory.html", {"subcat": subcat})

def ajaxcategory(request):
    did = request.GET.get("did")
    subcategories = tbl_category.objects.filter(parent=did).values("id", "category_name")  # Assuming `parent_id` for hierarchy
    return JsonResponse(list(subcategories), safe=False)