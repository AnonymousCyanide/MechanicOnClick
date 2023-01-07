from django.shortcuts import render , redirect
from .models import Customer , User , Employee
from .forms import CustomerForm
# Create your views here.
def customer_register(request):
    context ={}
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        location = request.POST['location']
        try :
            if password1 == password2:
                user = User.objects.create_user(username=username ,role = User.Role.CUSTOMER, password = password1 , phone = phone , first_name = first_name , last_name = last_name)
                user.save()
                print("done")
                #location = "Bhopal"
                customer = Customer.objects.create(user = user , location = location)
                customer.save()
            return render(request, 'account/register.html' , context=context)
        except :
            return render(request, 'account/register.html' , context=context)
    else :
        return render(request , 'account/register.html' , context=context)