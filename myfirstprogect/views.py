from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	home_text = request.GET['usertext']

	arr = home_text.split()

	len_arr = len(arr) 


	reverse_text = home_text[::-1]

	return render(request, 'rev.html', {'usertext':home_text, "revtext":reverse_text, "count":len_arr})

	