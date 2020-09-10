from user.forms import UserSignupForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class SignupView(CreateView):
    model = get_user_model()
    form_class = UserSignupForm
    success_url = '/signin/'

    def form_invalid(self, form):
        messages.success(self.request, '회원가입을 축하합니다.', extra_tags='success')
        return super().form_invalid(form)


class SigninView(LoginView):
    template_name = 'Signin.html'
    login_view = LoginView

    def form_invalid(self, form):
        messages.error(self.request, '아이디 또는 비밀번호를 확인하세요!',
                       extra_tags='danger')
        return super().form_invalid(form)


class SignoutView(LogoutView):
    template_name = 'Signout.html'

    def post(self, request, *args, **kwargs):
        del request.session['is_logined']
        return super().get(request, *args, **kwargs)