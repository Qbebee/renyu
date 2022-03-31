# Create your views here.
from django.shortcuts import render,redirect,reverse
from .models import Fanduier, GondanNote
from .forms import FanduierForm, GondanNoteForm,LoginModelForm

from django.contrib.auth import  login, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt,csrf_protect


# Create your views here.
@csrf_protect
def home(request):
    return render(request,'home.html')
@csrf_exempt
def index(request):
    return  render(request,'index.html')  

def test(request):
    return render(request,'test.html')   

@csrf_protect
def rack(request):
    FanduierList = Fanduier.objects.all().order_by('-fadriq')
    if request.method == "POST":
        fanduierForm = FanduierForm(data=request.POST,files = request.FILES)
        if fanduierForm.is_valid():
            fanduierForm.save()
            return redirect('success')
    else :
        fanduierForm = FanduierForm()
        return render(request,'rack.html',{'fanduierForm':fanduierForm,'FanduierList':FanduierList})


@csrf_protect
def gdnote(request):
    GondanNoteList = GondanNote.objects.all().order_by('-cgdate')
    if request.method =="POST":
        gondanNoteForm = GondanNoteForm(data=request.POST,files = request.FILES)
        if gondanNoteForm.is_valid():
            gondanNoteForm.save()
            return redirect('ok')
    else:
        gondanNoteForm = GondanNoteForm()
        return render(request,'gdnote.html',{'gondanNoteForm':gondanNoteForm,'GondanNoteList':GondanNoteList})

@csrf_protect
def success(request):
    return render(request,'success.html')  

@csrf_protect
def ok(request):
    return render(request,'ok.html')          


@csrf_protect        
def loginView(request):
    title = '用户登录'
    classContent = 'logins'
    if request.method == 'POST':
        infos = LoginModelForm(data=request.POST)
        if infos.is_valid():
            data = infos.data
            username = data['username']
            password = data['password']
            if User.objects.filter(username=username):
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return redirect(reverse('renyu:renyu'))
                else:
                    state = '注册成功'
                    d = dict(username=username,password=password,is_staff=1,is_active=1)
                    user = User.objects.create_user(**d)
                    user.save()
            else:
                error_msg = infos.errors.as_json()
                print(error_msg)
        else:
            infos = LoginModelForm()
        return render(request,'login.html',locals())
        
