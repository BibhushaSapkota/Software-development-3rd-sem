function validateRegistrationForm($event){
    let customer_username=document.getElementById('customer_username');
    let customer_address=document.getElementById('customer_address');
    let customer_phone=document.getElementById('customer_phone');
    let customer_email=document.getElementById('customer_email');
    let customer_password=document.getElementById('customer_password');
    let customer_cpassword=document.getElementById('customer_confirm-password');
    let messages=[]
    let errorElement=document.getElementById('messages')

    if (customer_username.value=="" | customer_email.value=="" | customer_password.value==""| customer_cpassword.value==""|customer_address.value=="" | customer_phone==""){
        messages.push('All fields are required')
        $event.preventDefault();
    }
    else if(customer_password.value!=customer_cpassword.value){
        messages.push("password and confirm password doesnt match")
    
    }
    if(messages.length>0){
        $event.preventDefault();
        errorElement.innerText=messages.join(',')
    }
    
}
function validateLoginForm($event){
    let customer_username=document.getElementById('username');
    let customer_password=document.getElementById('input_password');
    let messages=[]
    let errorElement=document.getElementById('error')

    if (customer_username.value=="" |  customer_password.value==""){
        messages.push('All fields are required')
        $event.preventDefault();
    }
    if(messages.length>0){
        $event.preventDefault();
        errorElement.innerText=messages.join(',')
    }
    
}