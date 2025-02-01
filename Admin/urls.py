from django.urls import path
from Admin import views

app_name="Admin"
urlpatterns = [
    path("category/",views.category,name="category"),
    path("deletecategory/<int:id>",views.deletecategory,name="deletecategory"),

    path('search/',views.search,name="search"),
    path('ajaxcategory/',views.ajaxcategory,name="ajaxcategory"),
]