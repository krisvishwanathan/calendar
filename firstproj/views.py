from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import AgentForm
from .models import Events

def incall_form(request):
    if request.method == 'POST':
        form = AgentForm(request.POST, request.FILES)
        if form.is_valid():  # Corrected syntax error here
            form.save()
            return redirect('success_page')
    else:
        form = AgentForm()
    return render(request, 'incall_form.html', {'form': form})

def hello(request):
    return HttpResponse("Hello, World!")

def index(request):  
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }
    return render(request, 'index.html', context)

def all_events(request):
    all_events = Events.objects.all()
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
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        start = request.POST.get("start")
        end = request.POST.get("end")
        client_name = request.POST.get("client_name")
        client_phone = request.POST.get("client_phone")
        client_address = request.POST.get("client_address")
        additional_info = request.POST.get("additional_info")

        event = Events(name=title, start=start, end=end, client_name=client_name, client_phone=client_phone, client_address=client_address, additional_info=additional_info)
        event.save()
        return JsonResponse({'status': 'Success', 'msg': 'Event added successfully'})
    else:
        return HttpResponse("Invalid request", status=400)

@csrf_exempt
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
            event = Events.objects.get(id=id)
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
def remove(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            event = Events.objects.get(id=id)
            event.delete()
            return JsonResponse({'status': 'Success', 'msg': 'Event deleted successfully'})
        except Events.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Event not found'})
    else:
        return HttpResponse("Invalid request", status=400)
