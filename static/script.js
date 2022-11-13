function signin()
{
    var signinError = document.getElementById('errorSignin');

    //for Aadhar Number
    var aadhar = document.forms["sform"]["aadhar"].value;
    

    //for Username/Mobile
    var mobile = document.forms["sform"]["mobile"].value;
    

    //for Password
    var passwd = document.forms["sform"]["passwd"].value;
    
   var entry2={
   aadhar2:aadhar,
   mobile2:mobile,
   passwd2:passwd
   }
   fetch('/signin/check',{
    method:"POST",
    credentials:"include",
   body:JSON.stringify(entry2),
   cache:"no-cache",
   headers:{"Content-type":"application/json"}
    })
    .then(function(response)
   {
   if(response.status!==200)
   {
   window.alert("error")
   return
   }
response.json().then(function (data)
{
if(data.message=="True")
window.location.href = "/election";
else
window.alert("wrong password or username or aadhar number")
})
})
}
