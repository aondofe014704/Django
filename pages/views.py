from django.http import HttpResponse
from django.views.generic import TemplateView


def homePageView(request):
    return HttpResponse('Hello Jack Songu...Keep Moving please...')


class HomePageView(TemplateView):
    template_name = 'home.html'
