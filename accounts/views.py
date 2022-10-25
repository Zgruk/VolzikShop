from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/registration.html', {'register_form': form})
