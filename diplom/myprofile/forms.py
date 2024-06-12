from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'email': 'Эл. почта',
            'avatar': 'Аватар',
            'birth_date': 'Дата рождения',
            'phone': 'Телефон',
            'city': 'Город',
            'street': 'Улица',
            'house_number': 'Дом',
            'apartment_number': 'Квартира',
        }