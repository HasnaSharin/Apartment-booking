from django.shortcuts import render,redirect
from myapp.models import apartmentDb,Types_Ap,ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from anotherApp.models import BookingDb


# Create your views here.
def index_page(req):
    return render(req,"index.html")
def a_registration(req):
    return render(req,"AprtmntRegistration.html")

def save_reg(req):
    if req.method=="POST":
        na=req.POST.get('name')
        ow=req.POST.get('owner')
        cat=req.POST.get('category')
        img=req.FILES['image']
        disc=req.POST.get('description')
        obj=apartmentDb(Aname=na,Oname=ow,Category=cat,Image=img,Description=disc)
        obj.save()
        messages.success(req,"Category saved successfully")
        return redirect(a_registration)
def disp_apartment(req):
    data=apartmentDb.objects.all()
    return render(req,"Displayproduct.html",{'data':data})
def edit_ap(req,Apartmentid):
    data=apartmentDb.objects.get(id=Apartmentid)
    return render(req,"EditAprtmnt.html",{'data':data})
def update_apartment(req,Apartmentid):
    if req.method=="POST":
        na = req.POST.get('name')
        ow = req.POST.get('owner')
        cat = req.POST.get('category')


        disc = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs=FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=apartmentDb.objects.get(id=Apartmentid).Image
        apartmentDb.objects.filter(id=Apartmentid).update(Aname=na,Oname=ow,Category=cat,Description=disc,Image=file)
        return redirect(disp_apartment)
def delete_page(req,Apartmentid):
    data = apartmentDb.objects.filter(id=Apartmentid)
    data.delete()
    return redirect(disp_apartment)
def Typ_apart(req):
    data=apartmentDb.objects.all()
    return render(req,"TypesAprt.html",{'data':data})
def save_type(req):
    if req.method=="POST":
        cat=req.POST.get('category')
        cname=req.POST.get('cmpn_name')
        cprice=req.POST.get('price')
        typ=req.POST.get('type')
        carea=req.POST.get('area')

        img=req.FILES['imagg']
        cdescr = req.POST.get('descr')
        obj=Types_Ap(Category=cat,Company_Name=cname,Price=cprice,Types=typ,Area=carea,Type_Image=img,Description=cdescr)
        obj.save()
        return redirect(Typ_apart)
def Type_disp(req):
    Types=Types_Ap.objects.all()
    return render(req,"DisplayTypes.html",{'Types':Types})
def Edit_type(req,Apartmentid):
    data = apartmentDb.objects.all()

    Types=Types_Ap.objects.get(id=Apartmentid)
    return render(req,"Edit_type.html",{'data':data,'Types':Types})
def update_Type(req,Apartmentid):
    if req.method=="POST":
        cat = req.POST.get('category')
        cname = req.POST.get('cmpn_name')
        cprice = req.POST.get('price')
        typ = req.POST.get('type')
        carea = req.POST.get('area')
        cdescr = req.POST.get('descr')
        try:
            img = req.FILES['imagg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Types_Ap.objects.get(id=Apartmentid).Type_Image
        Types_Ap.objects.filter(id=Apartmentid).update(Category=cat,Company_Name=cname,Price=cprice,Types=typ,Area=carea,Description=cdescr,Type_Image=file)
        return redirect(Type_disp)
def delete_type(req,Apartmentid):
    Types = Types_Ap.objects.filter(id=Apartmentid)
    Types.delete()
    return redirect(Type_disp)

def Login_Admin(request):
    return render(request,"Login_pageAdmin.html")
def Admin_login(request):
    if request.method=="POST":
        uName=request.POST.get('username')
        PWD=request.POST.get('pass')
        if User.objects.filter(username__contains=uName).exists():
            user=authenticate(username=uName,password=PWD)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully ")



                request.session['username']=uName
                request.session['pass']=PWD
                return redirect(index_page)
            else:
                messages.error(request,"invalid username or password")

                return redirect(Login_Admin)
        else:
            messages.error(request, "invalid username or password")

            return redirect(Login_Admin)
def admin_logout(request):
    del request.session['username']
    del request.session['pass']
    return redirect(Login_Admin)




def contact_dis(req):
    cont = ContactDb.objects.all()
    return render(req,"Contact_Display.html",{'cont':cont})


def delete_contact(req, dataid):
    contact = ContactDb.objects.filter(id=dataid)
    contact.delete()
    return redirect(contact_dis)
def displaybkpg(req):
    dis=BookingDb.objects.all()
    return render(req,"displayadbk.html",{'dis':dis})
def deleteadbk(req,dataid):
    dis=BookingDb.objects.filter(id=dataid)
    dis.delete()
    return redirect(displaybkpg)











