from django.urls import path
from .import views
app_name ='Ecapp'

urlpatterns = [
    path('',views.allprodcat,name="allprodcat"),
    path('<slug:C_slug>/',views.allprodcat,name="products_by_category"),
    path('<slug:C_slug>/<slug:product_slug>',views.prodetail,name="prodcatdetail"),

]