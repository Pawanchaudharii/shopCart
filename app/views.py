from django import http
from django.shortcuts import render,redirect
from AdminApp.models import Electronics, Fashion, ElectronicsProduct, FashionProduct
from app.models import MyCart1, UserInfo,MyCart,Profile,Payment,Order
from datetime import datetime
from django.contrib import messages

def home(request):
    # fetch all electronics,fashion,ElectronicsProduct, FashionProduct
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    electronicsproducts =  ElectronicsProduct.objects.all()
    fashionproducts =  FashionProduct.objects.all()
    return render(request, 'home.html', {"ele":ele ,"fashion":fashion, "electronicsproducts":electronicsproducts, "fashionproducts":fashionproducts })

def showelectronics(request,eid):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    ele_name = Electronics.objects.get(id=eid)
    electronicsproducts =  ElectronicsProduct.objects.filter(electronics=eid)
    return render (request, 'electronics.html',{"ele":ele , "fashion":fashion, "electronicsproducts":electronicsproducts, "ele_name":ele_name.ele_name })

def showfashion(request,fid):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    fashion_name = Fashion.objects.get(id=fid)
    fashionproducts =  FashionProduct.objects.filter(fashion=fid)
    return render(request, 'fashion.html', {"ele":ele, "fashion":fashion,  "fashionproducts":fashionproducts, "fashion_name":fashion_name.fashion_name })

def search(request):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    query = request.GET['query']
    empty = "hello"
    if len(query)>78 or len(query)<1:
        electronicsproducts = ElectronicsProduct.objects.none()
        fashionproducts = FashionProduct.objects.none()
    else:
        electronicsproductsname =  ElectronicsProduct.objects.filter(electronicsproductname__icontains=query)
        electronicsproductsdes =  ElectronicsProduct.objects.filter(description__icontains=query)
        electronicsproductsprice =  ElectronicsProduct.objects.filter(price__icontains=query)
        electronicsproducts = electronicsproductsname.union(electronicsproductsdes,electronicsproductsprice)

        fashionproductname =  FashionProduct.objects.filter(fashionproductname__icontains=query)
        fashionproductdes =  FashionProduct.objects.filter(description__icontains=query)
        fashionproductprice =  FashionProduct.objects.filter(price__icontains=query)
        fashionproducts = fashionproductname.union(fashionproductdes, fashionproductprice)

    if electronicsproducts.count() == 0 and fashionproducts.count() == 0:
        messages.info(request, 'no search result found')
        
    return render(request, 'search.html', {"ele":ele ,"fashion":fashion, "electronicsproducts":electronicsproducts, "fashionproducts":fashionproducts, "query":query})

def ShoweleproDetails(request, epid):
    if(request.method == "GET"):
        ele = Electronics.objects.all()
        fashion = Fashion.objects.all()
        electronicsproduct =  ElectronicsProduct.objects.get(id=epid)
        data = electronicsproduct.description.split("|")
        return render(request, 'eleproductdetail.html', {"ele":ele , "fashion":fashion, "electronicsproduct":electronicsproduct, "data":data})

def ShowfashionproDetails(request, fpid):
    if(request.method == "GET"):
        ele = Electronics.objects.all()
        fashion = Fashion.objects.all()
        fashionproduct =  FashionProduct.objects.get(id=fpid)
        data1 = fashionproduct.description.split("|")
        return render(request, 'fashionproductdetail.html', {"ele":ele, "fashion":fashion,  "fashionproduct":fashionproduct ,"data1":data1})

def signup(request):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    if(request.method=="GET"):
        return render (request, 'signup.html',{"ele":ele , "fashion":fashion})
    else:
        uname = request.POST["uname"]
        pwd1 = request.POST["pwd"]
        # check if user alredy present
        try:
            u1 = UserInfo.objects.get(username=uname)
        except:
            # User doesnt exists
            u1 = UserInfo(uname,pwd1,'inactive')
            u1.save()
            return redirect(login)
        else:
            messages.info(request, 'User already exists!!!')
            return redirect(signup)

def login(request):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    if(request.method=="GET"):
        return render(request, 'login.html', {"ele":ele , "fashion":fashion})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
    try:
        u1 = UserInfo.objects.get(username=uname, password=pwd)
    except:
        messages.info(request, 'Incorrect Usename or password!!!')
        return redirect(login)
    else:
        request.session["uname"] = uname
        u1.status = 'active'
        u1.save()
    return redirect(home)

def e_add_to_cart(request ,epid):
    if("uname" in request.session):
        user = UserInfo.objects.get(username = request.session["uname"])
        eleproduct_id = request.GET.get("eleprod_id")
        eleproduct = ElectronicsProduct.objects.get(id=eleproduct_id)
        qty = request.GET.get("qty")   
        try:
            cart = MyCart.objects.get(user=user, eleproduct=eleproduct)
        except:
            # Add to cart
            cart = MyCart()
            cart.user = user
            cart.eleproduct = eleproduct
            cart.qty = qty
            cart.save()
            return redirect(show_cart)
        else:
            messages.info(request, 'Item already in cart!!!')
            ele = Electronics.objects.all()
            fashion = Fashion.objects.all()
            electronicsproduct =  ElectronicsProduct.objects.get(id=epid)
            data = electronicsproduct.description.split("|")
            return render(request, 'eleproductdetail.html', {"ele":ele , "fashion":fashion, "electronicsproduct":electronicsproduct, "data":data})
    else:
        return redirect(login)

def f_add_to_cart(request, fpid):
    if("uname" in request.session):
        user = UserInfo.objects.get(username = request.session["uname"])
        fashionproduct_id = request.GET.get("fashionprod_id")
        fashionproduct = FashionProduct.objects.get(id=fashionproduct_id)
        qty = request.GET.get("qty")
        try:
            cart1 = MyCart1.objects.get(user=user, fashionproduct=fashionproduct)
        except:
            cart1 = MyCart1()
            cart1.user = user
            cart1.fashionproduct = fashionproduct
            cart1.qty = qty
            cart1.save()
            return redirect(show_cart)
        else:
            messages.info(request, 'Item already in cart!!!')
            ele = Electronics.objects.all()
            fashion = Fashion.objects.all()
            fashionproduct =  FashionProduct.objects.get(id=fpid)
            data1 = fashionproduct.description.split("|")
            return render(request, 'fashionproductdetail.html', {"ele":ele, "fashion":fashion,  "fashionproduct":fashionproduct ,"data1":data1})
    else:
        # user has not logged in so ask him to login
        return redirect(login)

def show_cart(request):
    if(request.method == "GET"):
        ele = Electronics.objects.all()
        fashion = Fashion.objects.all()
        user = UserInfo.objects.get(username = request.session["uname"])
        cart_items = MyCart.objects.filter(user = user)  
        cart1_items = MyCart1.objects.filter(user = user)  
        total=0
        for item in cart_items:
            total += item.eleproduct.price*item.qty      
        total1=0
        for item1 in cart1_items:
            total1 += item1.fashionproduct.price*item1.qty
        request.session["tot"] = total+total1
        if(request.session["tot"]>0):
            return render(request, "showcart.html", {"ele":ele, "fashion":fashion, "cart_items":cart_items, "cart1_items":cart1_items})
        else:
            return render(request, "emptycart.html", {"ele":ele, "fashion":fashion})
    else:
        action = request.POST["action"]
        id = request.POST["item_id"]
        item = MyCart.objects.get(id = id)
        if(action=="update"):
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        else:
            item.delete()
        return redirect(show_cart)

def update_remove(request):
    action = request.POST["action"]
    id = request.POST["item1_id"]
    item = MyCart1.objects.get(id = id)
    if(action=="update"):
        qty = request.POST["qty1"]
        item.qty = qty
        item.save()
    else:
        item.delete()
    return redirect(show_cart)

def checkout(request):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    user = UserInfo.objects.get(username = request.session["uname"])
    cart_items = MyCart.objects.filter(user = user)  
    cart1_items = MyCart1.objects.filter(user = user)
    add = Profile.objects.filter(user = user) 
    total=0
    for item in cart_items:
        total += item.eleproduct.price*item.qty
    total1=0
    for item1 in cart1_items:
        total1 += item1.fashionproduct.price*item1.qty
    request.session["tot"] = total+total1
    return render(request, 'checkout.html',{"ele":ele, "fashion":fashion, "cart_items":cart_items, "cart1_items":cart1_items, "add":add})

def profile(request):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    return render (request, 'profile.html', {"ele":ele, "fashion":fashion})

def address(request):
    user = UserInfo.objects.get(username = request.session["uname"])
    name = request.POST["inputName"]
    address = request.POST["inputAddress"]
    address2 = request.POST["inputAddress2"]
    city = request.POST["inputCity"]
    state = request.POST["inputState"]
    zip = request.POST["inputZip"]
    try:
        p1 = Profile.objects.get(user=user)
    except:
        p1 = Profile()
        p1.user = user
        p1.name = name
        p1.address = address
        p1.address2 = address2
        p1.city = city
        p1.state = state
        p1.zip = zip
        p1.save()
        return redirect(show_address)
    else:
        messages.info(request, 'Already adderss is present!!!')
        return redirect(profile)

def show_address(request):  
    if(request.method == "GET"):
        ele = Electronics.objects.all()
        fashion = Fashion.objects.all()
        user = UserInfo.objects.get(username = request.session["uname"])
        add = Profile.objects.filter(user = user) 
        return render (request, "address.html", {"ele":ele, "fashion":fashion, "add":add, "user":user})

def delete_address(request):
    user = UserInfo.objects.get(username = request.session["uname"])
    add = Profile.objects.filter(user = user) 
    add.delete()
    return redirect(profile)

def makepayment(request):
    if(request.method == "GET"):
        return render(request, 'makepayment.html', {})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)            
        except:
            messages.info(request, 'Invalid card details!!!')
            return redirect(makepayment)

        else:
            owner = Payment.objects.get(card_no='1234 1234 1234 1234',cvv='123',expiry='12/2025')
            if(buyer.balance < request.session["tot"]):
                messages.info(request, 'Your balance is too low for this transaction, please use another card!!!')
                return redirect(makepayment)

            else:
                buyer.balance -= request.session["tot"]
                owner.balance += request.session["tot"]
                buyer.save()
                owner.save()
                #Make Entry into Order Master
                user = UserInfo.objects.get(username = request.session["uname"])

                details = ""

                cart_items = MyCart.objects.filter(user=user)
                for item in cart_items:
                    details += item.eleproduct.electronicsproductname+" "
                    item.delete()

                cart1_items = MyCart1.objects.filter(user=user)
                for item1 in cart1_items:
                    details += item1.fashionproduct.fashionproductname+" "
                    item1.delete()

                order = Order()
                order.user = user
                order.order_date = datetime.now()
                order.amount = request.session["tot"]
                order.order_details = details
                order.save()
            return redirect(orderconfirm)

def orderconfirm(request):
    user = UserInfo.objects.get(username = request.session["uname"])
    add = Profile.objects.filter(user = user) 
    return render (request, 'orderconfirm.html', {"add":add})

def orders(request):
    ele = Electronics.objects.all()
    fashion = Fashion.objects.all()
    user = UserInfo.objects.get(username = request.session["uname"])
    orderdetail = Order.objects.filter(user = user)  
    return render(request, 'orders.html',{"ele":ele, "fashion":fashion, "orderdetail":orderdetail})

def orderhistory(request):
    ord = Order.objects.all()
    ord.delete()
    return redirect(orders)

def change_password(request):
    if(request.method == "GET"):
        ele = Electronics.objects.all()
        fashion = Fashion.objects.all()
        return render(request, 'changepassword.html', {"ele":ele , "fashion":fashion})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["oldpassword"]
        if(request.session["uname"] == uname):
            try:
                u1 = UserInfo.objects.get(username=uname, password=pwd)
            except:
                messages.info(request, 'Invalid old Password!!!')
                return redirect(change_password)
            else:
                newpass = request.POST["newpassword"]
                u1 = UserInfo(uname,newpass,'active')
                u1.save()
                messages.info(request, 'Password Change Successful!!!')
                return redirect(change_password)
        else:
            messages.info(request, 'Invalid Username!!!')
            return redirect(change_password)

def logout(request):
    u1 = UserInfo.objects.get(username=request.session["uname"])
    u1.status = 'Inactive'
    u1.save()       
    request.session.clear()
    return redirect(home)


    
   