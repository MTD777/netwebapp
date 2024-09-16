from django.urls import path
from .views import run_script, script_runner

urlpatterns = [
    path('run-script/', run_script, name='run_script'),
    path('', script_runner, name='script_runner'),
]
