from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages

from django.http import JsonResponse, HttpResponse

from .models import Services
from django.contrib.auth.models import User
from django.utils import timezone
import json


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def loging(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("loging")
    else:
        return render(request, "main/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


def registr_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    return render(request, "main/registr.html", {"form": form})


def save_data(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        tariff = request.POST.get('tariff')
        meter_reading = request.POST.get('meter_reading')
        total_cost = request.POST.get('total_cost')
        utility_type = request.POST.get('utility_type')
        user_id = request.POST.get('user_id')
        print(utility_type)

        # Проверка, что tariff и meter_reading являются числами
        try:
            tariff = float(tariff)
            meter_reading = float(meter_reading)
        except ValueError:
            return JsonResponse(
                {'error': 'Tariff and meter reading must be numeric'},
                status=400)

        # логика для сохранения данных в базу данных
        Services.objects.create(
            account_number=account_number,
            tariff=tariff,
            meter_reading=meter_reading,
            total_cost=total_cost,
            utility_type=utility_type,
            user_id=user_id)

        return JsonResponse({'message': 'Data saved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def gaz(request):
    # Получаем user_id, например, из запроса
    user_id = request.user.id

    # Уточняем тип услуги (в вашем случае, 'gaz')
    utility_type = 'gas'

    # Получение последних 12 записей из таблицы Services для данного пользователя и данной услуги
    last_12_services = Services.objects.filter(user_id=user_id,
                                               utility_type=utility_type).order_by(
        '-id')[:12]

    # Получение последнего показания газа из базы данных 
    last_meter_reading = Services.objects.filter(user_id=user_id,
                                                 utility_type=utility_type).order_by(
        '-id').first().meter_reading if Services.objects.filter(
        user_id=user_id, utility_type=utility_type).exists() else 0

    last_meter_reading = float(last_meter_reading)
    # Сумма к оплате
    last_total_cost = Services.objects.filter(user_id=user_id,
                                                 utility_type=utility_type).order_by(
        '-id').first().total_cost if Services.objects.filter(
        user_id=user_id, utility_type=utility_type).exists() else 0

    last_total_cost = float(last_total_cost)

    # Подготавливаем контекст для передачи данных на страницу
    context = {
        'last_meter_reading': json.dumps(
            last_meter_reading) if last_meter_reading is not None else None,
        'last_12_services': last_12_services,
        'utility_type': utility_type,
        'last_total_cost': last_total_cost,
        'user_id': user_id,
        # Другие данные, которые вы хотите передать на страницу
    }

    # Рендерим страницу gaz.html с передачей контекста
    return render(request, 'main/gaz.html', context)


def svet(request):
    # Получаем user_id, например, из запроса
    user_id = request.user.id

    # Уточняем тип услуги (в вашем случае, 'svet')
    utility_type = 'svet'

    # Получение последних 12 записей из таблицы Services для данного пользователя и данной услуги
    last_12_services = Services.objects.filter(user_id=user_id,
                                               utility_type=utility_type).order_by(
        '-id')[:12]

    # Получение последнего показания газа из базы данных
    last_meter_reading = Services.objects.filter(user_id=user_id,
                                                 utility_type=utility_type).order_by(
        '-id').first().meter_reading if Services.objects.filter(
        user_id=user_id, utility_type=utility_type).exists() else 0

    last_meter_reading = float(last_meter_reading)

    # Подготавливаем контекст для передачи данных на страницу
    context = {
        'last_meter_reading': json.dumps(
            last_meter_reading) if last_meter_reading is not None else None,
        'last_12_services': last_12_services,
        'utility_type': utility_type,
        'user_id': user_id,
        # Другие данные, которые вы хотите передать на страницу
    }

    # Рендерим страницу gaz.html с передачей контекста
    return render(request, 'main/svet.html', context)


def voda(request):
    # Получаем user_id, например, из запроса
    user_id = request.user.id

    # Уточняем тип услуги (в вашем случае, 'svet')
    utility_type = 'voda'

    # Получение последних 12 записей из таблицы Services для данного пользователя и данной услуги
    last_12_services = Services.objects.filter(user_id=user_id,
                                               utility_type=utility_type).order_by(
        '-id')[:12]

    # Получение последнего показания газа из базы данных
    last_meter_reading = Services.objects.filter(user_id=user_id,
                                                 utility_type=utility_type).order_by(
        '-id').first().meter_reading if Services.objects.filter(
        user_id=user_id, utility_type=utility_type).exists() else 0

    last_meter_reading = float(last_meter_reading)

    # Подготавливаем контекст для передачи данных на страницу
    context = {
        'last_meter_reading': json.dumps(
            last_meter_reading) if last_meter_reading is not None else None,
        'last_12_services': last_12_services,
        'utility_type': utility_type,
        'user_id': user_id,
        # Другие данные, которые вы хотите передать на страницу
    }

    # Рендерим страницу gaz.html с передачей контекста
    return render(request, 'main/voda.html', context)
