request = {
    "url": "https://blackboard.ie.edu/learn/api/v1/courses/_42717_1/gradebook/attempts/_1321632_1/assessment/answers/grades?expand=questionAttempt.question,questionAttempt.answerCorrectness",
    "method": "GET"
}

course = "_42717_1"
assessments = ["_1285450_1", "_1321632_1", "_1334891_1", "_1357133_1"]

import base64
import requests
import json
import time


def download_assesment(course, assessment):
    request = {
        "url": "https://blackboard.ie.edu/learn/api/v1/courses/" + course + "/gradebook/attempts/" + assessment + "/assessment/answers/grades?expand=questionAttempt.question,questionAttempt.answerCorrectness",
        "method": "GET"
    }

    data = base64.b64encode(json.dumps(request).encode('utf-8')).decode('utf-8')
    data = data.replace('+', '%2B').replace('/', '%2F').replace('=', '%3D')
    url = "http://localhost:3020/send/" + data
    res = requests.get(url)

    # wait for 5 seconds
    time.sleep(5)

    url2 = "http://localhost:3020/get/stack"
    res2 = requests.get(url2)

    data = json.loads(res2.content)[-1]
    return data

for assessment in assessments:
    data = download_assesment(course, assessment)
    # save data to file with assesment name
    with open(assessment + ".json", "w") as f:
        f.write(json.dumps(data))
