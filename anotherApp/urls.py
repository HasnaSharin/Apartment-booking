from django.urls import path
from anotherApp import views

urlpatterns=[
    path('index_apartment/',views.index_apartment,name="index_apartment"),
    path('Apartment_page/<Type_name>',views.Apartment_page,name="Apartment_page"),
    path('About_page/',views.About_page,name="About_page"),
    path('Reg_loginAp/',views.Reg_loginAp,name="Reg_loginAp"),
    path('Save_register/',views.Save_register,name="Save_register"),
    path('login_page/',views.login_page,name="login_page"),
    path('logout_page/',views.logout_page,name="logout_page"),
    path('single_ApartPage/<int:dataid>/',views.single_ApartPage,name="single_ApartPage"),
    path('contact_Ap/',views.contact_Ap,name="contact_Ap"),
    path('Save_contact/',views.Save_contact,name="Save_contact"),
    path('search_page/',views.search_page,name="search_page"),
    path('Contact_agent/',views.Contact_agent,name="Contact_agent"),
    path('BookPage/',views.BookPage,name="BookPage"),
    path('Book_Details/',views.Book_Details,name="Book_Details"),
    path('Payment/',views.Payment,name="Payment"),
    path('invoice/',views.invoice,name="invoice"),
    # path('Display/',views.Display,name="Display"),
]