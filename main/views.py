from django.shortcuts import render
from django.http import FileResponse

def main(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    
def help(request):
    return render(request, 'help.html')

def download(request):
    return FileResponse(open('main/game/Prototype 0.0.8.exe', 'rb',), as_attachment=True)