function validate()
{
    //alert('hello')
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if(email.indexOf("@")==-1 || email.lastIndexOf(".")==-1)
    {
        alert("Invalid Email Id");
        return false;
    }
    else if(password.length<6)
    {
        alert("Password length should be above six");
        return false;
    }
    else
    {
        alert("Successful");
        return false;
    }

    }