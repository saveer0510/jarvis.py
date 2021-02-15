 function validate(){
    var username = document.getElementById("uname").value;
    var password = document.getElementById("psw").value;
    if (( username == "saveer" && password == "saveer12")||(username == "saveer1" && password == "saveer12"))
    {
    alert ("Login successfully");
    window.location = "success.html?user="+username  // Redirecting to other page.

    }
    else{
        alert("login failled")
    }
   
}
