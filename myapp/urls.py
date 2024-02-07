from django.urls import path
from myapp import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('a_registration/',views.a_registration,name="a_registration"),
    path('save_reg/',views.save_reg,name="save_reg"),
    path('disp_apartment/',views.disp_apartment,name="disp_apartment"),
    path('edit_ap/<int:Apartmentid>/',views.edit_ap,name="edit_ap"),
    path('update_apartment/<int:Apartmentid>/',views.update_apartment,name="update_apartment"),
    path('delete_page/<int:Apartmentid>/',views.delete_page,name="delete_page"),

    path('Typ_apart/',views.Typ_apart,name="Typ_apart"),
    path('save_type/',views.save_type,name="save_type"),
    path('Type_disp/',views.Type_disp,name="Type_disp"),
    path('Edit_type/<int:Apartmentid>/',views.Edit_type,name="Edit_type"),
    path('update_Type/<int:Apartmentid>/',views.update_Type,name="update_Type"),
    path('delete_type/<int:Apartmentid>/',views.delete_type,name="delete_type"),


    path('',views.Login_Admin,name="Login_Admin"),
    path('Admin_login/',views.Admin_login,name="Admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_dis/',views.contact_dis,name="contact_dis"),
    path('delete_contact/<int:dataid>/',views.delete_contact,name="delete_contact"),
    path('displaybkpg/',views.displaybkpg,name="displaybkpg"),
    path('deleteadbk/<int:dataid>/',views.deleteadbk,name="deleteadbk"),


]