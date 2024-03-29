from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password, make_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required':'사용자 이름을 입력하세요.'
        },
        max_length=34, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.') # 특정 필드에 에러를 넣어주는 메소드
            else:
                self.user_id = fcuser.id
