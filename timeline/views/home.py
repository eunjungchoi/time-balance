from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, timedelta, date
from timeline.models import *


@login_required
def index(request):
	user = request.user
	team = Team.objects.get(name='Puddlr')

	try:
		member = Member.objects.filter(team=team).get(user=user)
	except Member.DoesNotExist:
		return redirect(reverse('index_for_viewer'))

	works = Work.objects.filter(team=team).order_by("-date")
	periods = Period.objects.filter(team=team)
	context = {
		'user': user,
		'team': team,
		'member': member,
		'works': works,
		'periods': periods,
		}
	return render(request, 'timeline/index.html', context)


@login_required
def index_for_viewer(request):
	user = request.user
	team = Team.objects.get(name='Puddlr')
	works = Work.objects.filter(team=team).order_by("-date")
	periods = Period.objects.filter(team=team)

	context = {
		'user': user,
		'team': team,
		'works': works,
		'periods': periods,
		}
	return render(request, 'timeline/index_for_viewer.html', context)


@login_required
def balance(request):
	team = Team.objects.get(name='Puddlr')
	members = Member.objects.filter(team=team)
	periods = Period.objects.filter(team=team)

	today = date.today()
	this_month = today.month

	# 전체 팀 통계
	all_works_this_month = Work.objects.filter(team=team).filter(date__month=this_month)
	# 멤버별 통계
	for member in members:
		monthly_work_list_per_member = all_works_this_month.filter(member=member.user)
		member.monthly_works = 0
		for work in monthly_work_list_per_member:
			member.monthly_works += work.period.unit
		member.monthly_paycheck = member.user.paycheck * member.monthly_works

	years = [2016]
	months = [8, 9]

	context = {
		'members': members,
		'periods': periods,
		'today': today,
		'years': years,
		'months': months,
	}

	return render(request, 'timeline/balance.html', context)


@login_required
def balance_past(request):
	team = Team.objects.get(name='Puddlr')
	members = Member.objects.filter(team=team)
	periods = Period.objects.filter(team=team)

	selected_year = request.POST['year']
	selected_month = request.POST['month']

	years = [2016]
	months = [8, 9]

	all_works_this_month = Work.objects.filter(team=team).filter(date__year=selected_year, date__month=selected_month)

	for member in members:
		monthly_work_list_per_member = all_works_this_month.filter(member=member.user)
		member.monthly_works = 0
		for work in monthly_work_list_per_member:
			member.monthly_works += work.period.unit
		member.monthly_paycheck = member.user.paycheck * member.monthly_works

	context = {
		'members': members,
		'periods': periods,
		'selected_year': selected_year,
		'selected_month': selected_month,
		'years':years,
		'months':months
	}

	return render(request, 'timeline/balance_past.html', context)
