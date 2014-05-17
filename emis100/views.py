from django.http import HttpResponse
def home(request):
	return HttpResponse('hello how are you!')
