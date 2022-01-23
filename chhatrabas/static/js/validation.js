function validateRegistrationForm($event){
    let customer_username=document.getElementById('customer_username');
    let customer_address=document.getElementById('customer_address');
    let customer_phone=document.getElementById('customer_phone');
    let customer_email=document.getElementById('customer_email');
    let customer_password=document.getElementById('customer_password');
    let customer_cpassword=document.getElementById('customer_confirm-password');

    if (customer_username.value=="" | customer_email.value=="" | customer_password.value==""| customer_cpassword.value==""|customer_address.value=="" | customer_phone==""){
        alert("empty field")
        $event.preventDefault();
    }
    else if(customer_password.value!=customer_cpassword.value){
        alert("password and confirm password doesnt match")
        $event.preventDefault();
    }
    
    return false;
}
function validateLoginForm($event){
    let customer_username=document.getElementById('customer_username');
    let customer_password=document.getElementById('customer_password');
    

    if (customer_username.value=="" |  customer_password.value==""){
        alert("empty field")
        $event.preventDefault();
    }
    
    return false;
}