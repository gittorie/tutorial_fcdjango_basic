from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# 홈
def home (request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('Home!')

# 로그인
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form' : form})

    # if request.method == 'GET':
    #     return render(request, 'login.html')
    
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력하세요.'
    #     else:
    #         fcuser = Fcuser.objects.get(username = username)
    #         if check_password(password, fcuser.password):
    #             request.session['user'] = fcuser.id
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 일치하지 않습니다.'
    #     return render(request, 'login.html', res_data)\
    
# 로그아웃
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

# 회원가입
def register(request):
    # url을 직접 입력하는 경우
    if request.method == 'GET':
        return render(request, 'register.html')
    
    # 등록 버튼 클릭하는 경우
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {} # 빈 dict 변수 만듬
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
        # 사용할 클래스 >>> from .models import Fcuser
        # 클래스 변수 만들고 객체 생성하기
            fcuser = Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
            fcuser.save()

        return render(request, 'register.html', res_data)
    
