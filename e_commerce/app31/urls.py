from django.urls import path
from app31 import views
urlpatterns=[
    path('',views.index,name='index'),
    path('product',views.product,name='product'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
    path('customer',views.customer,name='customer'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('userpending',views.userpending,name='userpending'),
    path('userapprove/<int:reg_id>/',views.user_approve,name='userapprove'),
    path('userreject/<int:reg_id>/',views.user_reject,name='userreject'),
    path('approveduser',views.approveduser,name='approveduser'),
    path('userdelete/<int:reg_id>/',views.user_delete,name='userdelete'),
    path('addcart/<int:reg_id>/',views.add_cart,name='addcart'),
    path('cart',views.cart,name='cart'),
    path('pay',views.pay,name='pay'),
    path('buynow/<int:reg_id>/',views.buy_now,name='buynow'),
]