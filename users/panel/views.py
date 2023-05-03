from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import View


def PanelView(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'registration/login.html')


class LoginView(View):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('user_panel')
        message = 'Your email or password is incorrect'
        return render(request, self.template_name, context={'form': form, 'message': message})
