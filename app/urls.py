from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('showelectronics/<eid>', views.showelectronics),
    path('showfashion/<fid>', views.showfashion),
    path('search/', views.search),
    path('ShoweleproDetails/<epid>', views.ShoweleproDetails),
    path('ShowfashionproDetails/<fpid>', views.ShowfashionproDetails),
    path('signup/', views.signup),
    path('login/', views.login ),
    path('e_add-to-cart/<epid>', views.e_add_to_cart),
    path('f_add-to-cart/<fpid>', views.f_add_to_cart),
    path('show_cart/', views.show_cart),
    path('update_remove', views.update_remove),
    path('checkout/', views.checkout),
    path('profile/', views.profile, name='profile'),
    path('address', views.address, name='address'),
    path('show_address/', views.show_address),
    path('delete_address/', views.delete_address),
    path('makepayment/', views.makepayment),
    path('orderconfirm/', views.orderconfirm),
    path('orders/', views.orders),
    path('orderhistory/', views.orderhistory),
    path('changepassword/', views.change_password),
    path('logout/', views.logout ),
]
