from django.shortcuts import render

def email(request):
	return render(request,'customer/email.html')