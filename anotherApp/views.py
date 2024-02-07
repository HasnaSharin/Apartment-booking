from django.shortcuts import render,redirect
from myapp.models import apartmentDb,Types_Ap,ContactDb
from anotherApp.models import RegisterDb,BookingDb
from django.contrib import messages

# Create your views here.

def index_apartment(req):
    category=apartmentDb.objects.all()
    return render(req,"Apartment.html",{'category':category})
def Apartment_page(req,Type_name):
    category = apartmentDb.objects.all()
    Type=Types_Ap.objects.filter(Category=Type_name)

    return render(req,"Detail_Apartment.html",{'category':category,'Type':Type})
def About_page(req):
    return render(req,"About_page.html")
def Reg_loginAp(req):
    return render(req,"AploginReg_page.html")
def Save_register(req):
    if req.method=="POST":
        nam=req.POST.get('name')
        emai=req.POST.get('email')
        passw=req.POST.get('pass')
        mob=req.POST.get('mobile')
        img=req.FILES['image']
        obj=RegisterDb(UserName=nam,UEmail=emai,UPassword=passw,Mobile=mob,UsImage=img)
        obj.save()
        return redirect(Reg_loginAp)

def login_page(request):
    if request.method=="POST":
        uname=request.POST.get('name')
        epass=request.POST.get('pass')

        if RegisterDb.objects.filter(UserName=uname,UPassword=epass).exists():
            request.session['name'] = uname
            request.session['pass'] = epass
            return redirect(index_apartment)
        else:
            return redirect(Reg_loginAp)
    else:
        return redirect(Reg_loginAp)
def logout_page(req):
    del req.session['name']
    del req.session['pass']
    return redirect(Reg_loginAp)


def single_ApartPage(req,dataid):
    single_Ap=Types_Ap.objects.get(id=dataid)
    return render(req,"Single_Apart.html",{'single_Ap':single_Ap})

def contact_Ap(req):

    return render(req,"Contact_Ap.html")
def Save_contact(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        sub=req.POST.get('subject')
        mes=req.POST.get('message')
        obj=ContactDb(Name=na,Email=em,Subject=sub,Message=mes)
        obj.save()
        messages.success(req,"Your Details Send Successfully")

        return redirect(contact_Ap)
def search_page(req):
    if req.method=="GET":
        query=req.GET.get('query')
        if query:
            Type = Types_Ap.objects.filter(Types__icontains=query)

            return render(req,"SearchBar.html",{'Type':Type})
        else:
            print("No information")
            return render(req,"SearchBar.html",{})
def Contact_agent(req):
    return render(req,"Contact_agent.html")
def BookPage(req):
    return render(req,"BookFlat.html")
def Book_Details(req):
    if req.method=="POST":
        name=req.POST.get('name')
        phne=req.POST.get('phone')
        email=req.POST.get('email')
        mem=req.POST.get('members')
        obj=BookingDb(BookingName=name,PhoneB=phne,Email=email,Members=mem)
        obj.save()
        messages.success(req, "Booking is successfully completed.our team will contact you")
        return redirect(BookPage)


def Payment(req):
    # messages.success(req, "Payment done successfully")

    return render(req,"Payment.html")
# def Display(req):
#     Bkpg=BookingDb.objects.filter(name=req.session['uname'])
#     return render(req,"Display_Bkpage.html",{'Bkpg':Bkpg})
def invoice(req):
    messages.success(req, "Payment done successfully")
    return render(req,"invoice.html")







