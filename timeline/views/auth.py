from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
# from .models import Member, Team


def log_in(request):
	if request.user.is_authenticated():
		return redirect(reverse('index'))
	return render(request, 'timeline/login.html')



def authenticate(request):
	user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
	if not user:
		return redirect(reverse('log_in'))

	auth.login(request, user)

    # member = Member.objects.filter(user=user)
    # if member:
    #     return redirect('/'+member.get().team.name)
    # else :
	return redirect(reverse('index'))


@login_required
def logout(request):
	auth.logout(request)
	return redirect(reverse('log_in'))
