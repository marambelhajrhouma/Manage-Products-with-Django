
from django.urls import path
from django.urls.conf import include
from product import views


urlpatterns = [
    path('prod/',views.prod),
    path('show',views.show),
    path('search/', views.search_product, name='search_product'),
    path('search_by_price/', views.search_by_price, name='search_by_price'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
    #path('url' , 'route dans l'app', 'name(optionnel)'),
]