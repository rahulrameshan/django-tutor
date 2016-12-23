//alert("welcome to my seond page");
//var signup=document.getElementById("signup")
function signup_redirect()
{
var user=document.getElementById('username').value();
alert(user);
location.href="/sinup";
}

function back_to_login()
{

location.href="/login";
}

function home_redirect()
{
alert("redirecting to home");
location.href="/home";
}