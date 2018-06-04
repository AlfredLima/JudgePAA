from django.shortcuts import render
from .forms import SubmissionForm
from django.utils import timezone
from django.shortcuts import redirect
import os

def post_list(request):
    return render(request, 'submission/post_list.html', {})

def post_new(request):
	if request.method == "POST":
		form = SubmissionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			date = (str(post.date)[11:19]).replace(':','_')
			path = os.getcwd() + '/codes'
			file = open( path + '/' + 'S' + str(post.pk) + '.py' , 'w' )
			file.write(post.file)
			
			
	form = SubmissionForm()
	return render(request, 'submission/post_new.html', {'form': form})