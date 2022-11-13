function vote(){
    var flag=false;
    var val;
    var sError = document.getElementById("error");
    if(document.getElementById("radio1").checked){
      flag = true;
val=document.getElementById("radio1").value;
      document.write(val);
      return true;
    }
    else if(document.getElementById("radio2").checked){
      flag = true;
      val=document.getElementById("radio2").value;
      document.write(val);
      return true;
    }
    else if(document.getElementById("radio3").checked){
      flag = true;
      val=document.getElementById("radio3").value;
            document.write(val);
      return true;
    }
    else if(document.getElementById("radio4").checked){
      flag = true;
      val=document.getElementById("radio4").value;
            document.write(val);
      return true;
    }
    else if(document.getElementById("radio5").checked){
        flag = true;
        val=document.getElementById("radio5").value;
              document.write(val);
        return true;
      }
    else{
      document.getElementById("error").innerHTML="Select the Party you want to Vote!";
      sError.style.display="block";
      return false;
    }


  }