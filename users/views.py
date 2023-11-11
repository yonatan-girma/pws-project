from django.contrib.auth.views import LoginView, LogoutView
from users.forms import LoginForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class UserLogoutView(LogoutView):
    http_methods = ['post']
