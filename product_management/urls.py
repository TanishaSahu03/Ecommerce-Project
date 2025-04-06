from django.urls import path, include
from . import views

urlpatterns = [
   path("product-detail/<int:pk>",views.ProductDetailView.as_view(), name = "productdetail"),
   path("addproduct/",views.ProductCreateView.as_view(), name = "addproduct"),
   path("productdelete/<int:pk>/", views.ProductDeleteView.as_view(), name = "productdelete"),
   path("product/", views.Temp.as_view(), name = "product"),
   path("products/", views.VendorProductListView.as_view(), name="showproducts"),
   path("productsearch/", views.ProductSearchView.as_view(), name = "product_search"),
   path("vendor_order/", views.VendorOrdersView.as_view(), name = "vendor_order"),
]