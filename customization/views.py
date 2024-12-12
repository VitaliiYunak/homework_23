from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UpperTextForm, RegistrationForm
from .models import UpperTextModel


def upper_text(request):
    data = {}
    if request.method == "POST":
        form = UpperTextForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            for field_name, value in cleaned_data.items():
                data['text_value'] = value
            obj = form.save()
            stats = obj.text_statistics()
            data['stats'] = stats
    else:
        form = UpperTextForm()
    objects = UpperTextModel.objects.all()
    data['all_count_word'] = count_s_letters()[0]
    data['objects'] = objects
    data['form'] = form
    return render (request, 'customization/upper_text.html',context=data)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Зберігаємо нового користувача
            login(request, user)  # Автоматичний вхід після реєстрації
            return redirect('upper_text')  # Перенаправлення після успішної реєстрації
    else:
        form = RegistrationForm()
    return render(request, 'customization/register.html', {'form': form})


def count_s_letters():
    # Виконуємо кастомний SQL-запит через raw
    with connection.cursor() as cursor:
        sql = """
        SELECT COUNT(id)
        FROM customization_uppertextmodel;
        """
        cursor.execute(sql)
        result = cursor.fetchone()
    return result