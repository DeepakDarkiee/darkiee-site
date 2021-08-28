from django.shortcuts import render
from django.views.generic import CreateView, View


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
