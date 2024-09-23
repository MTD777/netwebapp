from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from logging_automation import setup_logging, log_message

# Set up logging
logger = setup_logging()

def run_script(request):
    log_message(logger, f"Request method: {request.method}")
    log_message(logger, f"Form data: {request.POST}")
    
    script_name = request.POST.get('script_name')
    log_message(logger, f"Received script name: {script_name}")
    
    if not script_name:
        return HttpResponse("No script name provided.")
    
    script_path = f'/netwebapp/scripts/{script_name}.py'
    log_message(logger, f"Attempting to run script: {script_path}")
    
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)
        log_message(logger, f"Script output: {result.stdout}")
        log_message(logger, f"Script error (if any): {result.stderr}")
        
        output = f"<pre>Script output:\n{result.stdout}\nScript error (if any):\n{result.stderr}</pre>"
        return HttpResponse(output)
    except Exception as e:
        log_message(logger, f"Error running script: {e}")
        return HttpResponse(f"<pre>Error: {e}</pre>")

def script_runner(request):
    return render(request, 'script_runner.html')




## Working Version

# from django.shortcuts import render
# from django.http import HttpResponse
# import subprocess
# from logging_automation import setup_logging, log_message

# # Set up logging
# logger = setup_logging()

# def run_script(request):
#     log_message(logger, f"Request method: {request.method}")
#     log_message(logger, f"Form data: {request.POST}")
    
#     script_name = request.POST.get('script_name')  # Corrected to get the script name from the form
#     log_message(logger, f"Received script name: {script_name}")
    
#     if not script_name:
#         return HttpResponse("No script name provided.")
    
#     script_path = f'/netwebapp/scripts/{script_name}.py' # change to absolute path if running in Virtual environment
#     log_message(logger, f"Attempting to run script: {script_path}")
    
#     try:
#         result = subprocess.run(['python3', script_path], capture_output=True, text=True)
#         log_message(logger, f"Script output: {result.stdout}")
#         log_message(logger, f"Script error (if any): {result.stderr}")
#         return HttpResponse(f"Script output: {result.stdout}<br>Script error (if any): {result.stderr}")
#     except Exception as e:
#         log_message(logger, f"Error running script: {e}")
#         return HttpResponse(f"Error: {e}")

# def script_runner(request):
#     return render(request, 'script_runner.html')




# Very simple version - Access the app and automatically runs the job

# from django.shortcuts import render
# from django.http import HttpResponse
# import subprocess

# def run_script(request):
#     try:
#         result = subprocess.run(['python3', '/<your_path>/backup.py'], capture_output=True, text=True)
#         return HttpResponse(f"Script output: {result.stdout}")
#     except Exception as e:
#         return HttpResponse(f"Error: {e}")
