from django.http import JsonResponse
from django.shortcuts import render, render_to_response

from casetest import CaseTest
from submission.models import Submission
from .forms import SubmissionForm
from django.utils import timezone
from django.shortcuts import redirect
from multiprocessing import Process, Value, Lock
import os
import time

t = CaseTest()


def post_list(request):
    return render(request, 'submission/post_list.html', {})


def post_new(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            path = os.getcwd() + '/codes'
            name = path + '/' + 'S' + str(post.pk) + '.py'
            file = open(path + '/' + 'S' + str(post.pk) + '.py', 'w')
            file.write(post.file)
            p = Process(target=my_thread, args=(name, post,))
            p.start()
    form = SubmissionForm()
    return render(request, 'submission/post_new.html', {'form': form})

def get_submissions(request):
    submissions = Submission.objects.all().order_by('-date')
    alldata = {}
    alldata['submissions'] = []
    data = alldata['submissions']
    for submission in submissions:
        data.append({'registration': submission.registration, 'date': submission.date, 'evaluation': submission.evaluation,
                     'grade': submission.grade})
    return JsonResponse(alldata)

def submissions_table(request):
    return render_to_response('submission/submissions.html')



def my_thread(threadID, post):
    submission = Submission.objects.get(pk=post.pk)
    try:
        result = t.run(threadID)
        if 1.0 - result <= 1e-3:
            submission.evaluation = "Accepted"
            submission.grade = 100
        else:
            submission.evaluation = "Wrong Answer"
            submission.grade = result * 100
    except:
        print('erro')
        submission.evaluation = 'Runtime Error'
    submission.save()

