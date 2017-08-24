from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('<!DOCTYPE html><html><head>Hello World</head><p>OMG! This is a website!</p><a href="http://www.google.com">click here to find out more!</a><html>')