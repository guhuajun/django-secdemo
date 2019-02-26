# -*- coding: utf-8 -*-
# pylint: disable=

import os

from django.template.loader import render_to_string
from django.http.response import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    '''
    首页
    '''

    template_name = 'frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hostname'] = os.environ.get('HOSTNAME', 'None')
        context['option_a'] = os.environ.get('OPTION_A', 'Cat')
        context['option_b'] = os.environ.get('OPTION_B', 'Dog')
        
        return context

    def post(self, request, **kwargs):

        context = self.get_context_data()
        context['vote'] = request.POST.get('vote', 'a')
        response = render_to_string('frontend/index.html', context, request)

        return HttpResponse(response)
