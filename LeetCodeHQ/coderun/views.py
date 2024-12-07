
import os
import uuid
from django.shortcuts import render, redirect
from .processingpc import ScriptRunner

# View to render the page
def indexc(request):
    return render(request, 'indexc.html')

# View to handle code execution
def run_code(request):
    
    output = ""

    if request.method == 'POST':
        
        if 'clear' in request.POST:
            output = ""
        
        else:
            language = request.POST.get('language')
            code = request.POST.get('code')

            unique_id = str(uuid.uuid4())

            runner = ScriptRunner(unique_id, code, language)
            
            runner.create_file()
            runner.run()

            try:
                with open(f"temp/{unique_id}.txt", "r") as file:
                    output = file.read()
            except FileNotFoundError:
                output = "Error reading output file."
            
            runner.clean()

    return render(request, 'indexc.html', {'output': output})