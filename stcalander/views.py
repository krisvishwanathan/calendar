from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Events
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.urls import reverse

def user_is_authorized(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            login_url = reverse('login')
            return HttpResponseRedirect(f"{login_url}?next={request.path}&error=unauthorized")
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', 'index'))
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        error = request.GET.get('error')
        return render(request, 'login.html', {'error': 'You are not authorized to access this page. Please login to continue.' if error else None})


@user_is_authorized
def index(request):  
    all_events = Events.objects.filter(user=request.user)
    baseURL = settings.TEMPLATE_BASE
    context = {
        "events": all_events,
        "baseURL" : baseURL,
    }
    return render(request, 'index.html', context)

@login_required
def all_events(request):
    all_events = Events.objects.filter(user=request.user)
    events_list = [{
        'title': event.name,
        'id': event.id,
        'start': event.start.strftime("%Y-%m-%d %H:%M:%S"),
        'end': event.end.strftime("%Y-%m-%d %H:%M:%S"),
        'client_name': event.client_name,
        'client_phone': event.client_phone,
        'client_address': event.client_address,
        'additional_info': event.additional_info,
    } for event in all_events]
    return JsonResponse(events_list, safe=False)

@csrf_exempt
@login_required
def add_event(request):
    if request.method == 'POST':
        event = Events(
            user=request.user,
            name=request.POST.get("title"),
            start=request.POST.get("start"),
            end=request.POST.get("end"),
            client_name=request.POST.get("client_name"),
            client_phone=request.POST.get("client_phone"),
            client_address=request.POST.get("client_address"),
            additional_info=request.POST.get("additional_info")
        )
        event.save()
        return JsonResponse({'status': 'Success', 'msg': 'Event added successfully'})

@csrf_exempt
@user_is_authorized
def update(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        title = request.POST.get("title")
        start = request.POST.get("start")
        end = request.POST.get("end")
        client_name = request.POST.get("client_name")
        client_phone = request.POST.get("client_phone")
        client_address = request.POST.get("client_address")
        additional_info = request.POST.get("additional_info")
        
        try:
            event = Events.objects.get(id=id, user=request.user)
            event.name = title
            event.start = start
            event.end = end
            event.client_name = client_name
            event.client_phone = client_phone
            event.client_address = client_address
            event.additional_info = additional_info
            event.save()
            return JsonResponse({'status': 'Success', 'msg': 'Event updated successfully'})
        except Events.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Event not found'})
    else:
        return HttpResponse("Invalid request", status=400)

@csrf_exempt
@user_is_authorized
def remove(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            event = Events.objects.get(id=id, user=request.user)
            event.delete()
            return JsonResponse({'status': 'Success', 'msg': 'Event deleted successfully'})
        except Events.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Event not found'})
    else:
        return HttpResponse("Invalid request", status=400)
    

