from django.urls import path

from category.views import CategoryView

app_name = "category"

urlpatterns = [path("category", CategoryView.as_view(), name="category_classification")]
