from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from timeline.models import *


@login_required
def add(request):
	# if not request.POST['member'] or not request.POST['date']:
	# 	return redirect(reverse('index'))
	#
	# period = request.POST['period']
	# periods_obj = Period.objects.get(name__in=periods)
	team = Team.objects.get(name='Ecolemo_Puddlr')
	member = User.objects.get(username=request.POST['member'])
	period = Period.objects.get(pk=request.POST['period'])

	w = Work(
		team=team,
		member=member,
		date=request.POST['date'],
		period = period,
	)
	w.save()

	return redirect(reverse('index'))


@login_required
def editform(request, work_id):
	categories = Period.objects.filter(user=request.user)
	work = Work.objects.filter(user=request.user).get(pk=work_id)

	context = {
		'work' : work,
		'categories': categories
	}
	return render(request, 'timeline/editform.html', context)


@login_required
def edit(request):
	work_id = request.POST['work_id']
	s = Work.objects.get(pk=int(work_id))
	s.date = request.POST['date']
	s.save()

	cat_id_list = request.POST.getlist('period_id_to_edit')
	for cat_id in cat_id_list:
		cat = Period.objects.filter(user=request.user).get(id=int(cat_id))
		s.period.add(cat)
	return redirect(reverse('detail', kwargs={'work_id':work_id}))


@login_required
def delete(request):
	d_list = request.POST.getlist('item')

	for work_id in d_list:
		work = Work.objects.get(id=work_id)
		work.delete()

	return redirect(reverse('index'))


@login_required
def delete_each(request, work_id):
	s = work.objects.filter(user=request.user).get(id=work_id)
	s.delete()

	return redirect(reverse('index'))
