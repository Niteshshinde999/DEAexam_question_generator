from django.shortcuts import render, redirect
import json
from . import gemini

def question_parsed(raw_data):
    parsed = json.loads(raw_data)
    message = parsed.get('message', '')
    blocks = [q.strip() for q in message.split(';') if q.strip()]
    questions = []

    for block in blocks:
        lines = block.strip().split('\n')
        data = {'question': '', 'options': {}, 'Answer': '', 'Explanation': ''}
        for line in lines:
            line = line.strip()
            if line.startswith('Q:'):
                data['question'] = line[2:].strip()
            elif line.startswith('A:'):
                data['options']['A'] = line[2:].strip()
            elif line.startswith('B:'):
                data['options']['B'] = line[2:].strip()
            elif line.startswith('C:'):
                data['options']['C'] = line[2:].strip()
            elif line.startswith('D:'):
                data['options']['D'] = line[2:].strip()
            elif line.startswith('Answer:'):
                data['Answer'] = line[len('Answer:'):].strip()
            elif line.startswith('Explanation:'):
                data['Explanation'] = line[len('Explanation:'):].strip()
        questions.append(data)
    return questions

def hello(request):
    prompt = """
    Generate one AWS DEA-C01 original exam high-level question for data engineer with:
    - A scenario-based question
    - Four options (A to D)
    - Correct answer
    - A brief explanation
    separate each question by ';'
    Format:
    Q: ...
    A: ...
    B: ...
    C: ...
    D: ...
    Answer: ...
    Explanation: ...
    """

    if 'results' not in request.session or 'regenerate' in request.POST:
        rawdata = gemini.getData(prompt)
        apiresponse = question_parsed(rawdata)
        request.session['results'] = apiresponse

    results = request.session['results']
    message = None
    # show_answer = False

    if 'submit' in request.POST:
        selected = request.POST.get('choice')
        correct_answer = results[0]['Answer']
        message = 'Your Answer is Correct.' if selected == correct_answer else '❌ Your Answer is Wrong.'
        show_answer = True
        res = {'Answer' : results[0]['Answer'], 'Explanation' : results[0]['Explanation']}
        return render(request,'result.html',{'message': message,'show_answer': show_answer, 'res':res})
    result = {'question':results[0]['question'], 'options':results[0]['options']}
    return render(request, 'home.html', {'r': result})

