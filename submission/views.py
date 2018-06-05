import uuid

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from casetest import CaseTest
from submission.models import Submission
from .forms import SubmissionForm
from multiprocessing import Process
import os

t = CaseTest()


def post_list(request):
    return render(request, 'submission/post_list.html', {})


def post_new(request):
    sle = False
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            if Submission.objects.filter(registration=request.POST['registration']).count() >= 10:
                sle = True
            else:
                post = form.save()
                print(post.file.name)
                p = Process(target=my_thread, args=(post.file.name, post,))
                p.start()
                return HttpResponseRedirect('/submissions/')
    else:
        form = SubmissionForm()
    return render(request, 'submission/post_new.html', {'form': form, 'submission_limit_exceeded': sle})


def get_submissions(request):
    submissions = Submission.objects.all().order_by('-date')
    alldata = {'submissions': []}
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
        if (result['status'] == 'ok'):
            if 1.0 - result['grade'] <= 1e-3:
                submission.evaluation = "Aceita"
                submission.grade = 100
            else:
                submission.evaluation = "Resposta Errada"
                submission.grade = result['grade'] * 100
        else:
            submission.evaluation = "Tempo excedido"
            submission.grade = 0
    except:
        submission.evaluation = 'Erro de execução'
        submission.grade = 0
    submission.save()

