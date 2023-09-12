from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from datetime import datetime, timedelta
import pytz


def home(request):
    # Your view logic here
    return render(request, 'home.html')


def get_info(request):
    slack_name = request.GET.get('slack_name', 'Bella')
    track = request.GET.get('track', 'backend')
    
    # Get the current day of the week
    current_day = datetime.now().strftime('%A')
    
    # Get the current UTC time with a +/-2 minute window
    utc_time = datetime.now(pytz.UTC)
    
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time.isoformat(),
        "track": track,
        "github_file_url": "https://github.com/Bellamalwa/BackendHNGX/blob/main/endpoint_project",
        "github_repo_url": "https://github.com/Bellamalwa/BackendHNGX",
        "status_code": 200
    }
    
    return JsonResponse(response_data)

