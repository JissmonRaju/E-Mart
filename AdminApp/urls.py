from django.urls import path
from AdminApp import views


urlpatterns = [
    path('Index/',views.index,name='Index'),
    path('AddCategory/',views.add_category,name='AddCategory'),
    path('SaveCategory/', views.save_category, name='SaveCategory'),
    path('DisplayCategory/',views.display_category,name='DisplayCategory'),
    path('EditCategory/<int:c_id>/',views.edit_category,name='EditCategory'),
    path('UpdateCategory/<int:c_id>/', views.update_category,name='UpdateCategory'),
    path('DeleteCategory/<int:c_id>/', views.del_category,name='DeleteCategory'),

    path('AddProduct/',views.add_product,name='AddProduct'),
    path('SaveProduct/',views.save_product,name='SaveProduct'),
    path('DisplayProduct/',views.display_product,name='DisplayProduct'),
    path('EditProduct/<int:p_id>/',views.edit_product,name='EditProduct'),
    path('UpdateProduct/<int:p_id>/', views.update_product, name='UpdateProduct'),
    path('DeleteProduct/<int:p_id>/', views.delete_product, name='DeleteProduct'),

    path('AdminLoginPage/',views.admin_login_page,name='AdminLoginPage'),
    path('AdminLogin/',views.admin_login,name='AdminLogin'),
    path('AdminLogout/',views.admin_logout,name='AdminLogout'),

    path('ContactDetails/',views.display_contact,name='ContactDetails'),
    path('DeleteContact/<int:cont_id>/',views.del_contact,name='DeleteContact'),

    path('UserRegDetails/',views.display_reg_details,name='UserRegDetails'),
    path('DeleteRegDetails/<int:reg_id>/',views.delete_reg_details,name='DeleteRegDetails'),

]