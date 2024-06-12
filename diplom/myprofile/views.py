from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.http import JsonResponse


def my_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user, defaults={
        'surname': user.last_name,
        'name': user.first_name,
        'patronymic': '',
        'email': user.email,
        'avatar': '',
        'birth_date': None,
        'phone': '',
        'city': '',
        'street': '',
        'house_number': '',
        'apartment_number': ''
    })

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile')  # Redirect после сохранения
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'main/myprofile.html', {'form': form})


def get_user_id(request):
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    return JsonResponse({'user_id': user_id})
