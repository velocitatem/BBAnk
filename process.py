import json
import os
import sys


# first argument is the path to the json file
# load the file with a stringified json
with open(sys.argv[1], 'r') as f:
    # parse the stringified json
    data = json.loads(f.read())
    data = json.loads(data)



import genanki


qList = []
for question in data['body']['results']:
    att = question['questionAttempt']
    qType = att['questionType']
    q = att['question']
    qText = q['questionText']['displayText']
    answers = [] # list of answers [answer, correct]
    for ans in q['answers']:
        answers.append([ans['answerText']['displayText'], ans['correctAnswer']])
    qList.append([qType, qText, answers])



# create an anki deck
my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': "Options"},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}\n\n<br>Options:{{Options}}\n<br><br>',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'
        },
    ])

my_deck = genanki.Deck(
    2059400110,
    sys.argv[2])


import re
def cleanHTML(text):
    # remove html comments from text also the inside of the comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # remove html tags
    text = re.sub(r'<.*?>', '', text)
    text = text.strip()
    return text

# add questions to deck
for q in qList:
    q = [cleanHTML(x) for x in q[:2]] + q[2:]
    q[2] = [[cleanHTML(x[0]), x[1] ]for x in q[2]]
    print(q)
    options = [x[0] for x in q[2]]
    # ennumerate options with html
    options = [f"{i+1}. {x}" for i, x in enumerate(options)]
    # join by br
    options = '<br>'.join(options)
    # add br at start
    options = f'<br>{options}'
    answer = [x[0] for x in q[2] if x[1] == True][0]
    my_note = genanki.Note(
        model=my_model,
        fields=[q[1], options, answer])
    my_deck.add_note(my_note)

# generate apkg file
genanki.Package(my_deck).write_to_file(sys.argv[1] + '.apkg')
