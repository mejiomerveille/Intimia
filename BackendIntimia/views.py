from django.shortcuts import render, redirect
from codes.models import Code
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from codes.forms import CodeForm

from users.envoi import send_mail

@login_required
def home_view(request):
    return render(request, 'users/main.html', {})

def auth_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['pk'] = user.pk
                code_user = f"{user.username}: {user.code}"
                # TODO envoi du mail par la nouvelle methode
                # send_mail(code_user, user.email)
                return redirect('verify-view')
            
            
    form = AuthenticationForm()
    return render(request, 'users/auth.html', {'form': form})
@csrf_exempt
def verify_view(request):
    if request.method == "GET":
        form = CodeForm()
        return render(request, 'users/verify.html',{'form': form})
    if request.method == "POST":    
        form = CodeForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data.get('input1')+form.cleaned_data.get('input2')+form.cleaned_data.get('input3')+form.cleaned_data.get('input4')+form.cleaned_data.get('input5')
            pk= request.session.get('pk') or None
            code = Code.objects.get(pk=pk,number=num)
            if code is not None:
                return redirect('home-view')
    return redirect('login-view')