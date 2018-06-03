from django.shortcuts import render
from .forms import SubmissionForm
from django.utils import timezone
from django.shortcuts import redirect

def post_list(request):
    return render(request, 'submission/post_list.html', {})

def post_new(request):
	print("Inicio")
	if request.method == "POST":
		print("Post")
		form = SubmissionForm(request.POST)
		if form.is_valid():
			print("Post valido")
			post = form.save(commit=False)
			post.save()
	form = SubmissionForm()
	return render(request, 'submission/post_new.html', {'form': form})

def save(request):
	pass


# registration = models.CharField(max_length=8)
# password = models.CharField(max_length=8)
# date = models.DateTimeField(default=timezone.now)
# file = models.FileField()