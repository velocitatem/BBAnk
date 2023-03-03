def extractData(webPath):
    # example web path: https://blackboard.ie.edu/ultra/courses/_42717_1/outline/assessment/_790262_1/overview/attempt/_1356930_1/review/inline-feedback?attemptId=_1356930_1&mode=inline&columnId=_193298_1&contentId=_790262_1&courseId=_42717_1
    # target url: https://blackboard.ie.edu/learn/api/v1/courses/_42717_1/gradebook/attempts/_1321632_1/assessment/answers/grades?expand=questionAttempt.question,questionAttempt.answerCorrectness
    course = webPath.split("/")[5]
    attempt = webPath.split("/")[11]
    return (course, attempt)



import base64
import requests
import json
import time


def download_assesment(link):
    course, assessment = extractData(link)
    print(course, assessment)
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

    data = json.loads(res2.content)
    return data


data = download_assesment("https://blackboard.ie.edu/ultra/courses/_42717_1/outline/assessment/_790262_1/overview/attempt/_1356930_1/review/inline-feedback?attemptId=_1356930_1&mode=inline&columnId=_193298_1&contentId=_790262_1&courseId=_42717_1")
# save data to file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
