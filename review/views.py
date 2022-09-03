from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from users.models import Profile
from django.contrib.auth.decorators import login_required
from users.forms import UserProfileForm
from django.db.models import Avg

def index(request):
	return render(request, 'review/index.html')

@login_required
def review(request):
	# accessing the profile object for the current user
	user = request.user
	prim_k = user.pk # why is user.id and user.pk acting the same?
	profile = Profile.objects.get(pk=prim_k)
	#generates the applicable topics by course
	context = profile.create_review_list()
	# increments the user's streak if last login was yesterday
	profile.update_streak()
	return render(request, 'review/review.html', context)
	
@login_required
def stats(request):
	return render(request, 'review/stats.html', {'title': 'My Stats'})

def profile(request):
	user = request.user
	prim_k = user.pk
	profile = Profile.objects.get(pk=prim_k)
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=profile)
		form.save()
		messages.success(request, f'Profile updated!')
		return redirect('profile')

	#to handle request.method == 'GET'	
	else:
		#this populates the form with the current user's data
		form = UserProfileForm(instance=profile)
		return render(request, 'users/profile.html', {'form': form, 'title': 'Profile'})
	
def class_stats(request):

    user = request.user
    profile = user.profile

    if request.method != 'POST':
        
        students = Profile.objects.all().filter(teacher__exact=request.user.profile.teacher, course__exact=request.user.profile.course)
        form = UserProfileForm(instance=profile)

        average_streak = round(students.aggregate(Avg('streak')).get('streak__avg'), 1)
        average_login_count = round(students.aggregate(Avg('login_count')).get('login_count__avg'), 1)

        context = {
            'students': students,
            'title': 'Class Stats',
            'form': form,
            'average_streak': average_streak,
            'average_login_count': average_login_count,
        }

        if request.user.is_staff:
            return render(request, 'review/class_stats.html', context)
        else:
            return redirect('profile')
    
    else:
        form = UserProfileForm(request.POST, instance=profile)
        form.save()
        messages.success(request, f'Class updated!')
        return redirect('class_stats')