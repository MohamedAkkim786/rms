function foodprice(){
   if(document.getElementById("foodlist1").value == "Curd"){
     document.getElementById("selectNumber1").value = 30;
   }
   else if(document.getElementById("foodlist1").value == "Lemon"){
    document.getElementById("selectNumber1").value = 50;
   }
   else if(document.getElementById("foodlist1").value == "Briyani"){
    document.getElementById("selectNumber1").value = 80;
   }
   else if(document.getElementById("foodlist1").value == "Diner Grill"){
    document.getElementById("selectNumber1").value = 180;
   }
   else if(document.getElementById("foodlist1").value == "Unique Meals"){
    document.getElementById("selectNumber1").value = 70;
   }
   else if(document.getElementById("foodlist1").value == "Pizza Posse"){
    document.getElementById("selectNumber1").value = 90;
   }
   else{
    document.getElementById("selectNumber1").value = 0;
   }

}
function foodprice1(){
   if(document.getElementById("foodlist2").value == "Curd"){
     document.getElementById("selectNumber2").value = 30;
   }
   else if(document.getElementById("foodlist2").value == "Lemon"){
    document.getElementById("selectNumber2").value = 50;
   }
   else if(document.getElementById("foodlist2").value == "Briyani"){
    document.getElementById("selectNumber2").value = 80;
   }
   else if(document.getElementById("foodlist2").value == "Diner Grill"){
    document.getElementById("selectNumber2").value = 180;
   }
   else if(document.getElementById("foodlist2").value == "Unique Meals"){
    document.getElementById("selectNumber2").value = 70;
   }
   else if(document.getElementById("foodlist2").value == "Pizza Posse"){
    document.getElementById("selectNumber2").value = 90;
   }
   else{
    document.getElementById("selectNumber2").value = 0;
   }

}
function foodprice2(){
   if(document.getElementById("foodlist3").value == "Curd"){
     document.getElementById("selectNumber3").value = 30;
   }
   else if(document.getElementById("foodlist3").value == "Lemon"){
    document.getElementById("selectNumber3").value = 50;
   }
   else if(document.getElementById("foodlist3").value == "Briyani"){
    document.getElementById("selectNumber3").value = 80;
   }
   else if(document.getElementById("foodlist3").value == "Diner Grill"){
    document.getElementById("selectNumber3").value = 180;
   }
   else if(document.getElementById("foodlist3").value == "Unique Meals"){
    document.getElementById("selectNumber3").value = 70;
   }
   else if(document.getElementById("foodlist3").value == "Pizza Posse"){
    document.getElementById("selectNumber3").value = 90;
   }
   else{
    document.getElementById("selectNumber3").value = 0;
   }

}
function foodprice3(){
   if(document.getElementById("foodlist4").value == "Curd"){
     document.getElementById("selectNumber4").value = 30;
   }
   else if(document.getElementById("foodlist4").value == "Lemon"){
    document.getElementById("selectNumber4").value = 50;
   }
   else if(document.getElementById("foodlist4").value == "Briyani"){
    document.getElementById("selectNumber4").value = 80;
   }
   else if(document.getElementById("foodlist4").value == "Diner Grill"){
    document.getElementById("selectNumber4").value = 180;
   }
   else if(document.getElementById("foodlist4").value == "Unique Meals"){
    document.getElementById("selectNumber4").value = 70;
   }
   else if(document.getElementById("foodlist4").value == "Pizza Posse"){
    document.getElementById("selectNumber4").value = 90;
   }
   else{
    document.getElementById("selectNumber4").value = 0;
   }

}


function newfunction(){
  var arr = []
  for (var i = 1; i <= 4; i++) {

    let qId = 'quantity' + i;
    let sId = 'selectNumber' + i;
    let tId = 'total' + i;
    document.getElementById(tId).value = (document.getElementById(qId).value)*(document.getElementById(sId).value);  
    var a = document.getElementById(tId).value;
    arr.push(a);
  }
  var tot = 0;

  for (var i = 0; i < arr.length; i++) {
    if (parseInt(arr[i]))
      tot += parseInt(arr[i]);
  }

  document.getElementById('finalamt').value = tot;
}

function gst() {
   var arr = Number(document.getElementById('finalamt').value);
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
   document.getElementById('nettol').value = tot;
 }

 function parcelFunction(){
   document.getElementById("total").value = (document.getElementById("quantity").value)*(document.getElementById("selectNumber").value); 
    
}

function parcelFunction_gst(){
   var arr = Number(document.getElementById('total').value);
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
   document.getElementById('nettol').value = Math.floor(tot);
}


