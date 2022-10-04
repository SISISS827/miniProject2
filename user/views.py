from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/Join.html')
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')
        

        if password != password2:
            return render(request, 'user/Join.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if email == '' or password == '':
                # 사용자 저장을 위한 email과 password가 필수라는 것을 얘기 해 줍니다.
                return render(request, 'user/Join.html', {'error': '이메일과 패스워드는 필수 값 입니다'})
            
            exist_user = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'user/Join.html', {'error':'사용자가 존재합니다.'}) # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(email=email, bio=bio, password=password, username=username)
                return redirect('/Log_in')

def sign_in_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', "")
        password = request.POST.get('password', "")
        me = auth.authenticate(request, email=email, password=password)
        
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/Log_in.html', {'error':'이메일 혹은 패스워드를 확인 해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/Log_in.html')

@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("/")      
