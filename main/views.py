import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect

from main.forms import IHAForm, RentalForm
from main.models import IHA, Category, RentalRecord


# Create your views here.
@login_required(login_url='user_login')
def index(request):
    return render(request, 'index.html')


def iha_list(request):
    ihalar = IHA.objects.all()
    category = Category.objects.all()
    cont = {'ihalar': ihalar,
            'category': category}
    return render(request, 'iha-list.html', cont)


def user_login(request):
    # Kullanıcı giriş yapmışsa anasayfaya yönlendir
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            # Doğrulama başarılı ise kullanıcıyı oturum açtır ve anasayfaya yönlendir
            login(request, user)
            return redirect("/")

        # Doğrulama başarısız ise hata mesajı göster ve giriş sayfasına yönlendir
        messages.error(request, "Kullanıcı adı veya Şifre Yanlış")
        return redirect('user_login')

    # GET isteği ise giriş sayfasını görüntüle
    return render(request, "login.html")


from django.contrib import messages
from django.contrib.auth import authenticate, login


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


def iha_add(request):
    if request.method == 'POST':
        form = IHAForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "IHA başarıyla eklendi")
            return redirect("main:IHA_listeleme")
    else:
        form = IHAForm()
    return render(request, 'IHA_ekleme.html', {'form': form})


@login_required(login_url='user_login')
def iha_rent(request, iha_id):
    rental_record = RentalRecord.objects.filter(drone=iha_id, end_date__gte=datetime.date.today())
    drone = IHA.objects.get(pk=iha_id, is_rented=False)
    # iha kiralanmışsa hata mesajı göster


    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            start_date = cleaned_data['start_date']
            end_date = cleaned_data['end_date']

            rental = RentalRecord.objects.create(
                drone=drone,
                user=request.user,
                start_date=start_date,
                end_date=end_date
            )

            drone.is_rented = True
            drone.save()

            messages.success(request, "İHA başarıyla kiralandı")
            return redirect('main:IHA_listeleme')
    else:
        form = RentalForm()
    return render(request, 'iha_rent.html', {'form': form, 'drone': drone})



@login_required(login_url='user_login')
#Kiraladığım ihaları listeleme
def my_rental(request):
    my_rental = RentalRecord.objects.filter(user=request.user, drone__is_rented=True)
    rental = RentalRecord.objects.filter(user=request.user, drone__is_rented=True)
    my_rental = [rental.drone for rental in my_rental]
    return render(request, 'my_rental.html', {'ihalar': my_rental, 'rental': rental})

@login_required(login_url='user_login')
def iha_remove(request, iha_id):
    iha = get_object_or_404(IHA, pk=iha_id)
    my_rental = RentalRecord.objects.filter(user=request.user, drone=iha, drone__is_rented=True)
    if my_rental.exists():
        for rental in my_rental:
            rental.drone.is_rented = False
            rental.drone.save()
    messages.success(request, "Kiraladığınız İHA başarıyla iptal edildi")
    return redirect('main:IHA_listeleme')

def iha_sil(request, iha_id):
    iha = IHA.objects.get(pk=iha_id)
    iha.delete()
    messages.success(request, "İHA başarıyla silindi")
    return redirect('main:IHA_listeleme')


def iha_edit(request, iha_id):
    iha = IHA.objects.get(pk=iha_id)
    if request.method == 'POST':
        form = IHAForm(request.POST, instance=iha)
        if form.is_valid():
            form.save()
            messages.success(request, "İHA başarıyla güncellendi")
            return redirect("main:IHA_listeleme")
    else:
        form = IHAForm(instance=iha)
    return render(request, 'iha_edit.html', {'form': form, 'iha': iha})