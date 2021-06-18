from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .services import get_data

statusList = 'US'


class Get_API_Data(TemplateView):
    template_name = 'yahooData.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'yahooData': get_data(statusList),
        }
        return context
