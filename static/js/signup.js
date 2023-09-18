let password=document.getElementById("passwo");
let is_show=false;
var notshow=document.getElementById('eyenot');
var show=document.getElementById('eye');
let check=false;
show.style.display='none';
show.style.position='sticky';
notshow.style.position='sticky';
notshow.addEventListener('click',function(){
if(is_show==false){
    notshow.style.display='none';
    show.style.display='inline';
    password.setAttribute('type','text');
    is_show=true;
}
});
show.addEventListener('click',function(){
if(is_show){
    notshow.style.display='inline';
    show.style.display='none';
    password.setAttribute('type','password');
    is_show=false;
}
});
mychata=document.getElementById('chata')


const first_input = document.getElementById('first');
const last_input = document.getElementById('last');
const _email = document.getElementById('email');
const _password = document.getElementById('passwo');
const submitbutton = document.getElementById('submit');
submitbutton.style.display='inline';  
var first_try=true;

submitbutton.addEventListener('mouseover',()=>{
if(first_input.value==='' || last_input.value==="" || _email.value==='' || _password.value==='' ){
  if(first_try){
    submitbutton.style.transform="translateX(-405px)";
    first_try = false;
  }
  else{
    submitbutton.style.transform="translateX(0px)";
    first_try = true;
  }
  submitbutton.style.transition = '0.05s';
}
});


  