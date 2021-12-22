from django.shortcuts import render
from location.models import Location
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def view_location(request):
    return render(request, 'location\\view_location.html')

@csrf_exempt
def save_location(request):
    repsonse = {}
    try:
        body = request.body
        request_json = json.loads(body)
        locations = request_json['data']
        for location in locations:
            location_obj = Location()
            location_obj.latitude = location['latitude']
            location_obj.longitude = location['longitude']
            location_obj.current_datetime = location['current_datetime']
            location_obj.save()
        response = {
            'status': True,
            'message': 'Locations saved successfully',
            'code': 200,
        }

    except Exception as e:
        print('Exception at save_location in location: ', e)
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)
    

def fetch_location(request):
    pass

