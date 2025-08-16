import json
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

def geminiprompt():
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
    return prompt
