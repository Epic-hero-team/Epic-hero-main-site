from django.shortcuts import render
from django.http import FileResponse

def main(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')
    
def games(request):
    return render(request, 'games.html')

def support(request):
    return render(request, 'support.html')

def download(request):
    return FileResponse(open('main/game/Prototype 0.0.8.exe', 'rb',), as_attachment=True)