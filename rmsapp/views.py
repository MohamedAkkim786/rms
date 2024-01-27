from django.shortcuts import render,redirect
from .forms import *
from rmsapp import views
from django.contrib import messages
import mysql.connector
from datetime import date
from .models import hotelbookingform as hotelbookingreport
from .models import billdetailsform as foodreport
from .models import incomeentryform as accountsreport
from .models import accountsreportForm as accountsform
from .models import expensesentryform as expensesreport
from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
     form= FormContactForm(request.POST or None)
     if form.is_valid():
          form.save()
          return redirect("hotelbooking")
     return render(request,'Login_Page.html') 

def signin(request):
       
       return render(request,'signin.html') 

def reg(request):    
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]



        if password1==password2:        
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.save()
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('Login')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('Register')
                    
    else:
        form=CreateUserForm()
        return render(request,"reg.html",{'form':form})


def registration(request):
    form=registrationform(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'registration.html')

def account(request):
    form= accountsreportForm(request.POST or None)
    if form.is_valid():
          form.save()
    try:
      account=accountsreport.objects.all()
      date1 = accountsreport.objects.values_list('date1')
      date = accountsform.objects.values_list('date')
      
      date_index = len(date)
      date1_index = len(date1)
  
      date1 = [elem for elem in date1 if elem in date]
      date = list(date)
  
      if date[date_index-1] in  date1 :
        result_list = [elem[0] for elem in date]
  
      resultindex = len(result_list)
      formatted_date = result_list[resultindex-1].strftime('%Y-%m-%d')
      date1 = result_list[resultindex-1]
      mydata = accountsreport.objects.filter(date1=formatted_date).values()
      
      for i in mydata:
         amount = i["amount1"] + i["amount2"]

    
      
    except UnboundLocalError as error:
        totalamount=0
        amount= 0
    except IndexError as index_error:
        totalamount=0
        amount= 0

    try:
        expdate = expensesreport.objects.values_list('date1')
        expensedate =[]
        for i in expdate:
            if i[0] is not None:
                expensedate.append(i)
  
        
        
        if date[date_index-1] in  expensedate :
            exp_list = date[date_index-1]
            
        formatted_date = exp_list[0].strftime('%Y-%m-%d')
        expensedata = expensesreport.objects.filter(date1=formatted_date).values()
  
        for i in expensedata:
            totalamount = i["totalamount"]
            
    except UnboundLocalError as error:
        totalamount=0
    except IndexError as index_error:
        totalamount=0
        
    cashinhand =amount-totalamount
    
    
    
    
  

    return render(request,'accountsreport.html',{'amount':amount,'totalamount':totalamount,'cashinhand':cashinhand})


def hotelbooking(request):
    form= hotelbookingform(request.POST or None)
    if form.is_valid():
        form.save()

    context= {'form': form}
    return render(request,'hotelbooking.html', context)

def hotelreport(request):
    hotel=hotelbookingreport.objects.all()

    return render(request,'hotelreport.html',{'hotel':hotel})

def Expenses_Entry(request):
    form= expensesentryform(request.POST or None)
    if form.is_valid():
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "rms"
        )
        for i in range(1, 11):
             particular_key = f'particular{i}'
             amount_key = f'amount{i}'
             particular = request.POST.get(particular_key)
             amount = request.POST.get(amount_key)
             cur = conn.cursor()
             our_list = [(particular, amount)]
             sql = "INSERT INTO rmsapp_expensesentryform (particular,amount) VALUES (%s,%s)"
             try: 
                 cur.executemany (sql,our_list) 
                 conn.commit()
             except:
                 conn.rollback()
 
        form.save()


    context= {'form': form}
    return render(request,'Expenses_Entry.html' , context)

def bill(request):
     form= billdetailsform(request.POST or None)
     if form.is_valid():
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "rms"
        )
        for i in range(1,4):
             foodstr = f'foodlist{i}'
             quantitystr = f'quantity{i}'
             numberstr = f'selectNumber{i}'
             totalstr = f'total{i}'
             foodlist = request.POST.get(foodstr)
             quantity = request.POST.get(quantitystr)
             selectNumber = request.POST.get(numberstr)
             total = request.POST.get(totalstr)
             cur = conn.cursor()
             our_list = [(foodlist, quantity,selectNumber,total)]
             sql = "INSERT INTO rmsapp_billdetailsform (foodlist,quantity,selectNumber,total) VALUES (%s,%s,%s,%s)"
             try: 
                 cur.executemany (sql,our_list) 
                 conn.commit()
             except:
                 conn.rollback()
 
        form.save()
     context= {'form': form}
     return render(request,'bill.html' , context)

def food(request):
    food=foodreport.objects.all()

    return render(request,'foodreport.html',{'food':food})


def Groceries_Entry(request):
    form= GroceriesEntryform(request.POST or None)
    if form.is_valid():
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "rms"
        )
        for i in range(1,10):
             grocerynamestr = f'groceryname{i}'
             quantitystr = f'quantity{i}'
             pricestr = f'price{i}'
             totalstr = f'total{i}'
             groceryname = request.POST.get(grocerynamestr)
             quantity = request.POST.get(quantitystr)
             price = request.POST.get(pricestr)
             total = request.POST.get(totalstr)
             cur = conn.cursor()
             our_list = [(groceryname,quantity,price,total)]
             sql = "INSERT INTO rmsapp_groceriesentryform (groceryname,quantity,price,total) VALUES (%s,%s,%s,%s)"
             try: 
                 cur.executemany (sql,our_list) 
                 conn.commit()
             except:
                 conn.rollback()
 
        form.save()
    context= {'form': form}
    return render(request,'Groceries_Entry.html' , context)

def bar(request):
    form= barform(request.POST or None)
    if form.is_valid():
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "rms"
        )
        for i in range(1,2):
             foodstr = f'foodlist{i}'
             quantitystr = f'quantity{i}'
             numberstr = f'selectNumber{i}'
             totalstr = f'total{i}'
             foodlist = request.POST.get(foodstr)
             quantity = request.POST.get(quantitystr)
             selectNumber = request.POST.get(numberstr)
             total = request.POST.get(totalstr)
             cur = conn.cursor()
             our_list = [(foodlist, quantity,selectNumber,total)]
             sql = "INSERT INTO rmsapp_barform (foodlist,quantity,selectNumber,total) VALUES (%s,%s,%s,%s)"
             try: 
                 cur.executemany (sql,our_list) 
                 conn.commit()
             except:
                 conn.rollback()
 
        form.save()
    context= {'form': form}
    return render(request,'bar.html' , context)
    
   

def Gas_Maintenance(request):
    form= gasmaintenanceform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'Gas_Maintenance.html', context)

def Advertisement(request):
    form= advertisementform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'Advertisement.html', context)

def Income_Entry(request):
    form= incomeentryform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'Income_Entry.html', context)

def dining(request):
    form= diningform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'dining.html', context)

def parcel(request):
    form= parcelform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'parcel.html', context)

def online(request):
    form= onlineform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'online.html', context)


def roommaintenance(request):
    form= roommaintenanceform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'roommaintenance.html', context)
def roomcancellation(request):
    form= roomcancellationform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'roomcancellation.html', context)
def reception(request):
    form= receptionform(request.POST or None)
    if form.is_valid():
        form.save()
    
    context= {'form': form}
    return render(request,'reception.html', context)
def Food_Mastry(request):
    return render(request,'Food_Mastry.html')







def workersapplication(request):
    return render(request,'workersapplication.html')
def veseelmaintenance(request):
    return render(request,'veseelmaintenance.html')
def workersattendance(request):
    return render(request,'workersattendance.html')
def workerssalary(request):
    return render(request,'workerssalary.html')
def stockentry(request):
    return render(request,'stockentry.html')
def Parking(request):
    return render(request,'Parking.html')


