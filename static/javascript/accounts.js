/* Expenses Entry */

function findTotal() {
  var arr = []
  

  for (var i = 1; i <= 10; i++) {
    let aId = 'amount' + i;
    let a = document.getElementById(aId).value;
    arr.push(a);
  }

  var tot = 0;

  for (var i = 0; i < arr.length; i++) {
    if (parseInt(arr[i]))
      tot += parseInt(arr[i]);
  }

  document.getElementById('totalamount').value = tot;
}
/* Expenses Entry-end */


/* Groceries Entry */ 

function findsubtotal(){
    
    var total1=document.getElementById("quantity1").value * document.getElementById("price1").value
    document.getElementById("total1").value = total1

    var total2=document.getElementById("quantity2").value * document.getElementById("price2").value
    document.getElementById("total2").value = total2

    var total3=document.getElementById("quantity3").value * document.getElementById("price3").value
    document.getElementById("total3").value = total3

    var total4=document.getElementById("quantity4").value * document.getElementById("price4").value
    document.getElementById("total4").value = total4

    var total5=document.getElementById("quantity5").value * document.getElementById("price5").value
    document.getElementById("total5").value = total5

    var total6=document.getElementById("quantity6").value * document.getElementById("price6").value
    document.getElementById("total6").value = total6

    var total7=document.getElementById("quantity7").value * document.getElementById("price7").value
    document.getElementById("total7").value = total7

    var total8=document.getElementById("quantity8").value * document.getElementById("price8").value
    document.getElementById("total8").value = total8

    var total9=document.getElementById("quantity9").value * document.getElementById("price9").value
    document.getElementById("total9").value = total9

    var total10=document.getElementById("quantity10").value * document.getElementById("price10").value
    document.getElementById("total10").value = total10
 

   var arr = document.getElementsByClassName('total');
   var tot = 0;
 
   for (var i = 0; i < arr.length; i++) {
     if (parseInt(arr[i].value))
       tot += parseInt(arr[i].value);
   }
 
   document.getElementById('subtotal').value = tot;
}

function gst() {
  var arr = Number(document.getElementById('subtotal').value);
  var gst = document.getElementById('gstval').value;
  if (gst == 5){
     var tot = arr + arr*5/100;
  }
  else if(gst == 12){
     var tot = arr + arr*12/100;
  }
  else if(gst == 18){
     var tot = arr + arr*18/100;
  }
  else{
     document.getElementById('gstval').value = 0;
  }
  document.getElementById('grandtotal').value =Math.floor(tot) ;
}

/* Groceries Entry - End */ 


/* Advertisement */ 

function adTotal() {
    var array = document.getElementsByClassName('advertisement');
    var total = 0;
  
    for (var i = 0; i < array.length; i++) {
      if (parseInt(array[i].value))
        total += parseInt(array[i].value);
    }
  
    document.getElementById('adtotal').value = total;
  }

/* Advertisement-end */











