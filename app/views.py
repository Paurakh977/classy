from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
from app.models import MyCustomUser,Contacts,Todo
from django.conf import settings
from django.http import JsonResponse

lobuche = [
    24003, 24006, 24007,24012, 24023, 24025, 24027, 24030, 24031, 
    24032, 24038, 24040, 24042, 24043, 24045, 24051, 24054, 
    24057, 24058, 24062, 24065, 24067, 24076, 24078, 24079, 
    24084, 24088, 24089,123 
]

khumbila = [
    24002, 24004, 24005, 24013, 24015, 24016, 24017, 24024, 
    24026, 24036, 24037, 24039, 24044, 24047, 24048, 24055, 
    24056, 24059, 24066, 24070, 24071, 24075, 24080, 24082,24083,
    24085,24087, 24092
]

yala = [
    24001, 24008, 24009, 24010, 24011, 24018, 24019, 24020, 
    24021, 24022, 24028, 24035, 24041, 24046, 24049, 24050, 
    24052, 24053, 24061, 24063, 24064, 24068, 24069, 24072, 
    24073, 24077, 24081, 24086, 24090, 24091
]

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')
    
def bio_up(request):    
    return render(request,'bio_update.html')

def bio(request,id):
    if request.method=='POST':
        bio_=request.POST['bio']
        myuser=MyCustomUser.objects.get(id=id)
        myuser.bio=bio_
        myuser.save()
        return redirect('profile')
    return render('update.html')

def signup_page(request):
    return render(request,'signup.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        tick = request.POST.get('tick', False)
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome', extra_tags='login')
                if tick == 'on':
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                else:
                    request.session.set_expiry(0)  # Set session to expire when browser is closed
                return redirect('home')
            else:
                try:
                    user = MyCustomUser.objects.get(roll=username)
                    user = authenticate(request, username=user.username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Welcome', extra_tags='login')
                        if tick == 'on':
                            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                        else:
                            request.session.set_expiry(0)  # Set session to expire when browser is closed
                        return redirect('home')
                    else:
                        return HttpResponse("Invalid username or password")
                except MyCustomUser.DoesNotExist:
                    return HttpResponse("Invalid username or password")
        except:
            return HttpResponse("Invalid username or password")
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'login.html')
    
def logout_page(request):
    logout(request)
    return redirect('login')



def registration(request):
    if request.method == "POST":
        first_name = request.POST['fn']
        last_name = request.POST['ln']
        roll = int(request.POST['roll'])

        if roll in lobuche or roll in khumbila or roll in yala:
            email = request.POST['email']
            password = request.POST['password']
            username = first_name + ' ' + last_name
            try:
                existing_user = MyCustomUser.objects.get(roll=roll)
                return HttpResponse('A user with this roll already exists.')
            except MyCustomUser.DoesNotExist:
                pass
            myuser = MyCustomUser(username=username, email=email)
            myuser.set_password(password)
            myuser.roll = roll
            myuser.save()

            return redirect('login')
        else:
            return HttpResponse('Invalid roll')

    return render(request, 'registration.html')
            
        
        
def contact(request):
    if request.method=="POST":
        Username=request.user
        email=request.POST['email']
        desc=request.POST['desc']
        email_validator = EmailValidator(message='Invalid email format.')
        try:
            email_validator(email)
        except ValidationError:
            messages.error(request,'The email you have chosen is invalid',extra_tags='signup')
            return redirect('contact')
        ins=Contacts(roll=request.user.roll,user=Username,email=email,desc=desc)
        ins.save()
        messages.success(request,'Your query hs been submited')
        return redirect('home')


def routine(request):

    user_code=int(request.user.roll)
    if user_code in lobuche:
        context={'section':'lobuche'}
        return render(request,'routine.html',context)
    elif user_code in khumbila:
        context={'section':'khumbila'}
        return render(request,'routine.html',context)
    elif user_code in yala:
        context={'section':'yala'}
        return render(request,'routine.html',context)
    else:
        messages.error(request,'Your Roll number doesn\'t matches with any section')
        return redirect('home')
    

def profile(request):
    objects = Todo.objects.filter(user=request.user)    
    objs_count = objects.count()
    if objs_count:
        messages.success(request, f'You have {objs_count} tasks to do.', extra_tags='taskis')
    else:
        messages.success(request, 'You have no tasks to do. Would you like to set your tasks?', extra_tags='notask')
    return render(request, 'profile.html')

def about(request):
    return render(request,'about.html')

def task(request):
    return render(request,'tasks.html')

def todo(request):
    if request.method=='POST':
        user=request.user
        task=request.POST['task']
        desc=request.POST['desc']
        ins=Todo(user=user,task=task,desc=desc)
        ins.save()
        return redirect('todo')
    obj=Todo.objects.filter(user=request.user)
    context={'obj':obj}
    return render(request,'todo.html',context)

def add(request):
    if request.method=="POST":
        user=request.user
        task=request.POST['task']
        desc=request.POST['desc']
        ins=Todo(user=user,task=task,desc=desc)
        ins.save()
        return redirect('todo')

    return render(request,'add.html') 

def update_todo(request,task_id):
    if request.method=="POST":
        new_task=request.POST['task']
        new_desc=request.POST['desc']
        if new_task and new_desc:
            ins=Todo.objects.get(id=task_id)
            ins.task=new_task
            ins.desc=new_desc
            ins.save()
            return redirect('todo')
    obj=Todo.objects.get(id=task_id)
    task=obj.task
    desc=obj.desc
    context={'obj':obj}
    return render(request,'todoupdate.html',context)

def delete_todo(request,id):
    obj=Todo.objects.get(id=id)
    obj.delete()
    return redirect("todo")

def get_copy_content(request):
    user_roll = request.user.roll
    return JsonResponse({'content': user_roll})

def get_email_content(request):

    user_email = request.user.email
    return JsonResponse({'content': user_email})

def upload_notes(request):
    return render(request,"uploadnotes.html")

def view_notes(request):
    return render(request,'viewnotes.html')