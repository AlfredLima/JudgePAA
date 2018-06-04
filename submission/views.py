from django.shortcuts import render

from casetest import CaseTest
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
			file = open( path + '/' + 'S' + str(post.pk) + '.py' , 'w' )
			file.write(post.file)
			p = Process(target=my_thread, args=(name,post,))
			p.start()
	form = SubmissionForm()
	return render(request, 'submission/post_new.html', {'form': form})


def my_thread(threadID,post):
	value = t.run( threadID )
	print("Resposta:", value)


