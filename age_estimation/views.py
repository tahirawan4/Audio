from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from age_estimation.forms import UserSignUpForm
from age_estimation.models import Learn
from age_estimation.utils import estimate_age, save_user_info

from django.contrib import messages


def index(request):
    images = Learn.objects.all()
    return render(request, 'index.html', {'images': images})


def signup(request):
    signup_form = UserSignUpForm()
    if request.POST:
        signup_form = UserSignUpForm(request.POST)
        if signup_form.is_valid():
            if request.POST.get('validation'):
                user = signup_form.save()
                save_user_info(user, int(request.POST.get('age')), float(request.POST.get('frequency1')),
                               float(request.POST.get('frequency2')), float(request.POST.get('average')),
                               request.POST.get('country'))
                messages.add_message(request, messages.ERROR, 'User Successfully Created')
                return redirect(reverse('login'))
            else:
                messages.add_message(request, messages.ERROR, 'Please verify Your age.')

    return render(request, 'signup.html', {'form': signup_form})


def login(request):
    return render(request, 'signin.html', {})


@csrf_exempt
def submit_time(request):
    test_time1, test_time2 = request.POST.getlist('data[]')
    lowfreq = 20
    highfreq = 20000
    sample_freq = 44100  # sampling rate, Hz, must be integer
    duration = 20

    sound_time = duration
    testfreq1 = lowfreq + (float(test_time1) / sound_time * (highfreq - lowfreq))
    # calculate_freq = ((float(test_time2) - sound_time) / sound_time * (highfreq - lowfreq))
    testfreq2 = highfreq - (float(test_time2) / sound_time * (highfreq - lowfreq))
    aver_freq = (testfreq1 + testfreq2) / 2
    para = estimate_age(aver_freq)
    estimated_age = para[1]
    data = str(testfreq1) + "," + str(testfreq2) + "," + str(aver_freq) + "," + str(estimated_age)
    return HttpResponse(data)
