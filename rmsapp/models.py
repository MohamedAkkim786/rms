from django.db import models

class ContactForm(models.Model):
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    department= models.CharField(max_length=100)

class accountsreportForm(models.Model):
    date =  models.DateField(max_length=50)

class hotelbookingform(models.Model):
    customername= models.CharField(max_length=100)
    dob= models.DateField(max_length=50)
    age= models.IntegerField()
    gender= models.CharField(max_length=50)
    address= models.CharField(max_length=200)
    proof= models.CharField(max_length=100)
    children= models.IntegerField()
    adult= models.IntegerField()
    aged= models.IntegerField()
    phone= models.IntegerField()
    dateofbooking= models.DateField(max_length=200)
    dateofvacate= models.DateField(max_length=200)
    totaldays= models.IntegerField()
    total= models.IntegerField()
    gstvalue= models.IntegerField()
    nettotal= models.IntegerField()

class billdetailsform(models.Model):
    bill_no = models.IntegerField(null=True,blank=True)
    foodlist= models.CharField(max_length=50)
    quantity= models.IntegerField()
    selectNumber= models.IntegerField()
    total= models.IntegerField()
    finalamt=models.IntegerField(null=True,blank=True)
    gstval=models.IntegerField(null=True,blank=True)
    nettol=models.IntegerField(null=True,blank=True)
    payment=models.CharField(max_length=50,null=True,blank=True)

class GroceriesEntryform(models.Model):
    date1= models.DateField(max_length=50,null=True,blank=True)
    groceryname= models.CharField(max_length=50)
    quantity= models.IntegerField()
    price= models.IntegerField()
    total= models.IntegerField()
    subtotal=models.IntegerField(null=True,blank=True)
    gstval=models.IntegerField(null=True,blank=True)
    grandtotal=models.IntegerField(null=True,blank=True)


    
class gasmaintenanceform(models.Model):
    gasnumber= models.IntegerField()
    cpyname= models.CharField(max_length=50)
    cpycontact= models.IntegerField()


    gastaken= models.IntegerField()
    takendate= models.DateField(max_length=200)
    gasempty= models.IntegerField()

    emptydate=models.DateField(max_length=200)
    gasavailable= models.IntegerField()
    gasamount= models.IntegerField()

class expensesentryform(models.Model):
    date1= models.DateField(max_length=50,null=True,blank=True)
    particular= models.CharField(max_length=50)
    amount= models.IntegerField()
    totalamount = models.IntegerField(null=True,blank=True)


class advertisementform(models.Model):
    date1= models.DateField(max_length=50)
    socialmedia= models.IntegerField()
    notices= models.IntegerField()
    brochures = models.IntegerField()   
    posters= models.IntegerField()
    newspaper= models.IntegerField()
    vehicle= models.IntegerField()
    television = models.IntegerField()   
    radio= models.IntegerField()
    adtotal = models.IntegerField()   

class incomeentryform(models.Model):
    hotelroombooking= models.IntegerField()
    date1= models.DateField(max_length=50)
    amount1= models.IntegerField()
    restaurantbill = models.IntegerField()   
    date2= models.DateField(max_length=50)
    amount2= models.IntegerField()
    
class diningform(models.Model):
    tableno= models.CharField(max_length=50)
    waiter= models.CharField(max_length=50)
    status= models.CharField(max_length=50)
    food= models.CharField(max_length=50)   
    quantity= models.IntegerField()
    waiterallocation= models.CharField(max_length=50)

class parcelform(models.Model):
    billno= models.IntegerField()
    foodlist= models.CharField(max_length=50)
    quantity= models.IntegerField()
    price = models.IntegerField()   
    total= models.IntegerField()
    gstval= models.IntegerField()
    nettol= models.IntegerField()
    waiter = models.CharField(max_length=50)   
    customername= models.CharField(max_length=50)

class onlineform(models.Model):
    billno = models.IntegerField() 
    platform= models.CharField(max_length=50)
    customername= models.CharField(max_length=50)
    mobileno= models.IntegerField()
    mail = models.CharField(max_length=50)   
    datetime= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    foodlist= models.CharField(max_length=50)
    quantity = models.IntegerField()   
    price= models.IntegerField()
    total= models.IntegerField()
    gstval = models.IntegerField()   
    nettol= models.IntegerField()
    paymentmode= models.CharField(max_length=50)
    deliverperson= models.CharField(max_length=50)
    delivercontactno= models.IntegerField()

class registrationform(models.Model):
    hotelname= models.CharField(max_length=100)
    gstno= models.IntegerField() 
    address=  models.CharField(max_length=200)
    email= models.CharField(max_length=50)  
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    category = models.CharField(max_length=200)

class barform(models.Model):
    bill_no = models.IntegerField(null=True,blank=True)
    foodlist= models.CharField(max_length=50)
    quantity= models.IntegerField()
    selectNumber= models.IntegerField()
    total= models.IntegerField()
    finalamt=models.IntegerField(null=True,blank=True)
    gstval=models.IntegerField(null=True,blank=True)
    nettol=models.IntegerField(null=True,blank=True)
    payment=models.CharField(max_length=50,null=True,blank=True)

class roommaintenanceform(models.Model):
    roomtype = models.CharField(max_length=50)
    bed = models.CharField(max_length=50)
    roomno = models.IntegerField()
    pillow = models.IntegerField()
    bedsheet = models.IntegerField()
    restroomcleaning = models.CharField(max_length=50)
    wateravailability = models.CharField(max_length=50)
    tvavailability = models.CharField(max_length=50)
    acchecking = models.CharField(max_length=50)
    furniturechecking = models.CharField(max_length=50)

class receptionform(models.Model):
    customervisitperday = models.IntegerField()
    phonecallsfromroom = models.IntegerField()
    requirements = models.CharField(max_length=50)
    allocate = models.CharField(max_length=50)
    roomchanginginformation = models.IntegerField()
    roomchanginginformation = models.IntegerField()
    phonecallsfromoutside = models.IntegerField()
    dailyreporttomanager = models.CharField(max_length=200)

class roomcancellationform(models.Model):
    customername = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    roomno = models.IntegerField()
    phonenumber = models.IntegerField()
    email = models.CharField(max_length=50)
    fromdate = models.DateField(max_length=200)
    todate = models.DateField(max_length=200)

