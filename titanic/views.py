import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import TitanicPassenger
from .serializers import TitanicSerializer
from .forms import UploadFileForm, TitanicPassengerForm


class TitanicViewSet(viewsets.ModelViewSet):
    queryset = TitanicPassenger.objects.all()
    serializer_class = TitanicSerializer

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # پردازش فایل اکسل
            df = pd.read_excel(request.FILES['file'])
            
            passenger_list = []
            for _, row in df.iterrows():
                passenger_list.append(TitanicPassenger(
                    passenger_id=row['PassengerId'],
                    survived=row['Survived'],
                    pclass=row['Pclass'],
                    name=row['Name'],
                    sex=row['Sex'],
                    age=row.get('Age', None),
                    sibsp=row['SibSp'],
                    parch=row['Parch'],
                    ticket=row['Ticket'],
                    fare=row['Fare'],
                    cabin=row.get('Cabin', ''),
                    embarked=row['Embarked']
                ))

            TitanicPassenger.objects.bulk_create(passenger_list, ignore_conflicts=True)
            return redirect('titanic_list')
    else:
        form = UploadFileForm()
    return render(request, 'titanic/upload.html', {'form': form})

def titanic_list(request):
    passengers = TitanicPassenger.objects.all()
    return render(request, 'titanic/titanic_list.html', {'passengers': passengers})

def titanic_detail(request, passenger_id):
    passenger = get_object_or_404(TitanicPassenger, passenger_id=passenger_id)
    return render(request, 'titanic/titanic_detail.html', {'passenger': passenger})

def titanic_create(request):
    if request.method == 'POST':
        form = TitanicPassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('titanic_list')
    else:
        form = TitanicPassengerForm()
    return render(request, 'titanic/titanic_form.html', {'form': form})

def titanic_update(request, passenger_id):
    passenger = get_object_or_404(TitanicPassenger, passenger_id=passenger_id)
    if request.method == 'POST':
        form = TitanicPassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('titanic_detail', passenger_id=passenger.passenger_id)
    else:
        form = TitanicPassengerForm(instance=passenger)
    return render(request, 'titanic/titanic_form.html', {'form': form})

def titanic_delete(request, passenger_id):
    passenger = get_object_or_404(TitanicPassenger, passenger_id=passenger_id)
    if request.method == 'POST':
        passenger.delete()
        return redirect('titanic_list')
    return render(request, 'titanic/titanic_confirm_delete.html', {'passenger': passenger})
