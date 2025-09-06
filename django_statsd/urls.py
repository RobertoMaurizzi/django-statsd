from django.urls import path

import django_statsd.views

urlpatterns = [
    path('record', django_statsd.views.record, name='django_statsd.record'),
]