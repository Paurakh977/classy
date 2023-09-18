let password=document.getElementById("password");
let is_show=false;
var notshow=document.getElementById('eyenot');
var show=document.getElementById('eye');
let check=false;
show.style.display='none';
show.style.position='sticky';
notshow.style.position='sticky';
notshow.addEventListener('click',function(){
    if (is_show==false) {
        password.setAttribute('type','text');
        notshow.style.display='none';
        show.style.display='inline';
        is_show=true;
        
    }
    
});
show.addEventListener('click',function(){
if(is_show){
    password.setAttribute('type','password');
    show.style.display='none';
    notshow.style.display='inline';
    is_show=false;
}
});

var mew=true;
var _email=document.getElementById('username');
var login=document.getElementById('buttu');

login.addEventListener('mouseover', () => {
    if (_email.value === '' || password.value==="") {
      if (mew) {
        login.style.transform = 'translateX(-290px)';
        mew= false;
      } else {
        login.style.transform = 'translateX(0px)';
        mew= true;
      }
      login.style.transition = '0.05s';
    }
  });
  