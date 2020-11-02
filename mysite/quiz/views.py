from django.shortcuts import render
from quiz.models import Quiz
# Create your views here.

def home(request):
	quiz = Quiz.objects.all()
	return render(request,'index.html',{'quiz':quiz})