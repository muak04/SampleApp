from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('index'))

        return render(request, self.template_name, {})


class LogOutView(View):
    template_name = 'login.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name, {})
