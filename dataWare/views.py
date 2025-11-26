from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
# Create your views here.
import requests
def data(request):
    headers_h = {
        "content-type": "application/json",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = requests.get("https://api.github.com/gists/public", headers=headers_h).json()
    print("below is the response method")
    print(HttpResponse.status_code)
    return JsonResponse(data=data, safe=False)



def index(request):
    return render(request, "index.html")