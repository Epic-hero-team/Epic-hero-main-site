from django.shortcuts import render
from django.http import FileResponse

def main(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')
    
def projects(request):
    return render(request, 'games.html')

def support(request):
    return render(request, 'support.html')

def download(request):
    return FileResponse(open('main/game/Prototype 0.0.8.exe', 'rb',), as_attachment=True)

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})