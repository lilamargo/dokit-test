from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Doctor, Office
from .forms.forms import DoctorSignupForm, OfficeCreationForm, OfficeUpdateForm


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            # doctor.set_password(form.cleaned_data['password'])
            doctor.save()
            login(request, doctor)
            return redirect('dashboard')
    else:
        form = DoctorSignupForm()
    return render(request, 'signup.html', {'form': form})

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    doctor.delete()
    return redirect('dashboard')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        doctor = authenticate(request, email=email, password=password)

        if doctor is not None:
            login(request, doctor)
            return redirect('dashboard')
        else:
            error_message = 'Email or password does not exist or is incorrect.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def dashboard(request):
    doctors = Doctor.objects.all()
    offices = Office.objects.filter(is_deleted=False)
    return render(request, 'dashboard.html', {'offices': offices, 'doctors': doctors})

def create_office(request):
    if request.method == 'POST':
        form = OfficeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = OfficeCreationForm()
    return render(request, 'office_create_form.html', {'form': form})

def update_office(request, id):
    office = Office.objects.get(pk=id)
    if request.method == 'POST':
        form = OfficeUpdateForm(request.POST, instance=office)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = OfficeUpdateForm(instance=office)
    return render(request, 'office_update_form.html', {'form': form})

def office_list(request):
    offices = Office.objects.all()
    return render(request, 'office_list.html', {'offices': offices})

def delete_office(request, id):
    office = get_object_or_404(Office, pk=id)
    office.is_deleted = True
    office.save()
    return redirect('dashboard')
