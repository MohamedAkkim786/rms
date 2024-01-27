from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    username = forms.CharField(help_text=False)
    password1 = forms.CharField(help_text=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class registrationform(forms.ModelForm):
    class Meta:
        model= registrationform
        fields= ["hotelname","gstno","address","email","username","password","category"]

class FormContactForm(forms.ModelForm):
    class Meta:
        model= ContactForm
        fields= ["username", "password", "department"]

class accountsreportForm(forms.ModelForm):
    class Meta:
        model= accountsreportForm
        fields= ["date"]

class hotelbookingform(forms.ModelForm):
    class Meta:
        model= hotelbookingform
        fields= ["customername", "dob", "age","gender", "address", "proof","children", "adult", "aged","phone", "dateofbooking", "dateofvacate","totaldays", "total", "gstvalue","nettotal"]


class billdetailsform(forms.ModelForm):
    class Meta:
        model= billdetailsform
        fields= ["bill_no", "foodlist", "quantity", "selectNumber","total","finalamt","gstval","nettol","payment"]


class gasmaintenanceform(forms.ModelForm):
    class Meta:
        model= gasmaintenanceform
        fields= ["gasnumber","cpyname","cpycontact","gastaken","takendate","gasempty","emptydate","gasavailable","gasamount"]

class expensesentryform(forms.ModelForm):
    class Meta:
        model= expensesentryform
        fields= ["date1","particular","amount","totalamount"]

class advertisementform(forms.ModelForm):
    class Meta:
        model= advertisementform
        fields= ["date1","socialmedia","notices","brochures","posters","newspaper","vehicle","television","radio","adtotal"]

class incomeentryform(forms.ModelForm):
    class Meta:
        model= incomeentryform
        fields= ["hotelroombooking","date1","amount1","restaurantbill","date2","amount2"]

class diningform(forms.ModelForm):
    class Meta:
        model= diningform
        fields= ["tableno","waiter","status","food","quantity","waiterallocation"]

class parcelform(forms.ModelForm):
    class Meta:
        model= parcelform
        fields= ["billno","foodlist","quantity","price","total","gstval","nettol","waiter","customername"]

class onlineform(forms.ModelForm):
    class Meta:
        model= onlineform
        fields= ["billno","platform","customername","mobileno","mail","datetime","location","foodlist","quantity","price","total","gstval","nettol","paymentmode","deliverperson","delivercontactno"]

class GroceriesEntryform(forms.ModelForm):
    class Meta:
        model= GroceriesEntryform
        fields= ["date1","groceryname","quantity","price","total","subtotal","gstval","grandtotal"]

class barform(forms.ModelForm):
    class Meta:
        model= barform
        fields= ["bill_no", "foodlist", "quantity", "selectNumber","total","finalamt","gstval","nettol","payment"]

class roommaintenanceform(forms.ModelForm):
    class Meta:
        model= roommaintenanceform
        fields= ["roomtype", "bed", "roomno", "pillow","bedsheet","restroomcleaning","wateravailability","tvavailability","acchecking","furniturechecking"]

class roomcancellationform(forms.ModelForm):
    class Meta:
        model= roomcancellationform
        fields= ["customername", "age", "gender", "roomno","phonenumber","email","fromdate","todate"]

class receptionform(forms.ModelForm):
    class Meta:
        model= receptionform
        fields= ["customervisitperday", "phonecallsfromroom", "requirements", "allocate","roomchanginginformation","roomchanginginformation","phonecallsfromoutside","dailyreporttomanager"]
