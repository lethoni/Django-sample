from django.shortcuts import render

import requests
import json

# Create your views here.
def home(request):
    api_content = requests.get('https://api.github.com/users?since=0')
    api = json.loads(api_content.content)
    return render(request, 'index.html', {"api": api})

def search(request):
    if request.method == 'POST':
        html_text = request.POST['user']
        user_content = requests.get('https://api.github.com/users/' + html_text)
        user = json.loads(user_content.content)
        return render(request, 'search.html', {'user': user})
    else:
        notfound = "notfound"
        return render(request, 'search.html', {'notfound': notfound})