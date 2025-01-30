from django.urls import path
from Admin import views

app_name="Admin"
urlpatterns = [
    path("category/",views.category,name="category"),
]