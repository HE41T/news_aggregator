# import requests
# from django.shortcuts import render

# def news_list(request):
#     API_KEY = "12c8f59b487a4deb8c15191dd410b26b"
#     URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
#     response = requests.get(URL)
#     articles = response.json().get("articles", [])

#     return render(request, "news/news_list.html", {"articles": articles})

import requests
from django.shortcuts import render

def news_list(request):
    API_KEY = "12c8f59b487a4deb8c15191dd410b26b"  # ใส่ API Key ใหม่ที่สร้างมา
    URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}" # Now you can use the URL globally throughout the script

    response = requests.get(URL)
    articles = response.json().get("articles", [])

    return render(request, "news/news_list.html", {"articles": articles})
