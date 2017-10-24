from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    # 처음 비밀번호 입력
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    # 비밀번호 확인
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    # 아이디 유일성 검사
    def clean_username(self):
        # 사용자가 입력한 username
        input_username = self.cleaned_data['username']
        # 기존 username 중 동일한 것들이 있는지 여부
        if User.objects.filter(username=input_username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다.')
        return self.cleaned_data['username']

    # 재입력한 password가 처음 입력한 것과 일치하는지 여부
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다. ')
        return self.cleaned_data['password2']

    # signup 완료 : username과 password를 가진 유저 생성
    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2']
            )
