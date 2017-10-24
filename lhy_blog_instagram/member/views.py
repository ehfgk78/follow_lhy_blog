from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.shortcuts import render, redirect

from member.forms import LoginForm, SignupForm


def login(request):
    if request.method == 'POST':
        # Data bounded form 인스턴스 생성
        login_form = LoginForm(request.POST)
        # form형식에 맞는지 여부: 유효성 검증
        if login_form.is_valid():
            # 입력값에 해당하는 User의 존부: 인증 절차
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
            )
            # 인증 성공할 경우
            if user:
                # 세션 유지 : Django auth앱에서 제공하는 login함수
                django_login(request, user)
                return redirect('post:post_list')
            # 인증 실패한 경우  error 메세지
            login_form.add_error(None, '아이디 또는 비밀번호가 다릅니다.')
    else:
        login_form = LoginForm()
    return render(
        request,
        'member/login.html',
        context={
            'login_form': login_form,
        }
    )

def logout(request):
    django_logout(request)
    return redirect('post:post_list')

def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        # 유효성 검증 (username중복, password 재입력 동일성)
        if signup_form.is_valid():
            signup_form.signup()
            return redirect('post:post_list')
    else:
        signup_form = SignupForm()
    return render(
        request,
        'member/signup.html',
        context={
            'signup_form': signup_form,
        }
    )


