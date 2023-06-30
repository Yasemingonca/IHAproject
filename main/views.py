from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from main.models import IHA


# Create your views here.
def index(request):
    return render(request, 'index.html')


def iha_list(request):
    ihalar = IHA.objects.all()
    cont = {'ihalar': ihalar}
    return render(request, 'iha-list.html', cont)


def auth_login(request, user):
    pass


def login(request):
    # Kullanıcı giriş yapmışsa anasayfaya yönlendir
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            # Doğrulama başarılı ise kullanıcıyı oturum açtır ve anasayfaya yönlendir
            auth_login(request, user)
            return redirect("/")

        # Doğrulama başarısız ise hata mesajı göster ve giriş sayfasına yönlendir
        messages.error(request, "Kullanıcı adı veya Şifre Yanlış")
        return redirect(login)

    # GET isteği ise giriş sayfasını görüntüle
    return render(request, "login.html")


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password != password_confirm:
            messages.error(request, "Şifreler eşleşmiyor")
            return redirect("signup")

        # Kullanıcı adının daha önce varlığını kontrol et
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu kullanıcı adı zaten kullanımda, lütfen farklı bir kullanıcı adı seçin")
            return redirect("signup")
        # Yeni kullanıcı oluştur
        user = User.objects.create_user(username=username, password=password)

        # Oturum aç ve anasayfaya yönlendir
        login(request, user)
        return redirect("/")

    return render(request, "signup.html")
