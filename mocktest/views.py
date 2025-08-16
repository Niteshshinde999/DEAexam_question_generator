from django.shortcuts import render, redirect
import json
from . import gemini
from . import codebase
def hello(request):
    if 'results' not in request.session or 'regenerate' in request.POST:
        prompt = codebase.geminiprompt()
        rawdata = gemini.getData(prompt)
        apiresponse = codebase.question_parsed(rawdata)
        request.session['results'] = apiresponse

    results = request.session['results']
    message = None
    # show_answer = False

    if 'submit' in request.POST:
        selected = request.POST.get('choice')
        correct_answer = results[0]['Answer']
        message = 'Your Answer is Correct.' if selected == correct_answer else '❌ Your Answer is Wrong.'
        show_answer = True
        print(results[0]['Explanation'])
        res = {'Answer' : results[0]['Answer'], 'Explanation' : results[0]['Explanation']}
        return render(request,'result.html',{'message': message,'show_answer': show_answer, 'res':res})
    result = {'question':results[0]['question'], 'options':results[0]['options']}
    return render(request, 'home.html', {'r': result})

