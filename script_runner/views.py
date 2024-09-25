from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import subprocess
from logging_automation import setup_logging, log_message

# Initialize logging
logger = setup_logging()

def run_script(request):
    # Log the request method (GET, POST, etc.)
    log_message(logger, f"Request method: {request.method}")
    # Log the form data received in the request
    log_message(logger, f"Form data: {request.POST}")
    
    # Extract the script name from the form data
    script_name = request.POST.get('script_name')
    log_message(logger, f"Received script name: {script_name}")
    
    # If no script name is provided, return an error response
    if not script_name:
        return HttpResponse("No script name provided.")
    
    # Construct the full path to the script
    script_path = f'/netwebapp/scripts/{script_name}.py'
    log_message(logger, f"Attempting to run script: {script_path}")
    
    try:
        # Run the script using subprocess and capture the output
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)
        # Log the script's standard output
        log_message(logger, f"Script output: {result.stdout}")
        # Log any errors from the script
        log_message(logger, f"Script error (if any): {result.stderr}")
        
        # Format the output and return it in the HTTP response
        output = f"<pre>Script output:\n{result.stdout}\nScript error (if any):\n{result.stderr}</pre>"
        return HttpResponse(output)
    except Exception as e:
        # Log any exceptions that occur while running the script
        log_message(logger, f"Error running script: {e}")
        return HttpResponse(f"<pre>Error: {e}</pre>")

def script_runner(request):
    # Render the script runner HTML page
    return render(request, 'script_runner.html')


