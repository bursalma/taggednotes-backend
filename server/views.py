from django.shortcuts import render
from django.http import FileResponse
from rest_framework.views import APIView
from .settings import CLIENT_DIR


class IndexView(APIView):
    def get(self, request):
        return render(request, 'index.html')


class ManifestView(APIView):
    def get(self, request):
        return render(request, 'manifest.json')


class Logo1View(APIView):
    def get(self, request):
        return FileResponse(open(CLIENT_DIR / 'logo192.png', 'rb'))


class Logo5View(APIView):
    def get(self, request):
        return FileResponse(open(CLIENT_DIR / 'logo512.png', 'rb'))


class IconView(APIView):
    def get(self, request):
        return FileResponse(open(CLIENT_DIR / 'favicon.ico', 'rb'))
