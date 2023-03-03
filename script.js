let path = window.location.pathname;
let course = path.split("/")[3],
    assessment = path.split("/")[9];
let request = {
    "url": "https://blackboard.ie.edu/learn/api/v1/courses/" + course + "/gradebook/attempts/" + assessment + "/assessment/answers/grades?expand=questionAttempt.question,questionAttempt.answerCorrectness",
    "method": "GET"
}
async function provide(response) {
    let reader = response.body.getReader();
    let decoder = new TextDecoder('utf-8');
    let data = "";
    await reader.read().then(function processText({ done, value }) {
        if (done) {
            return data;
        }
        data += decoder.decode(value, { stream: true });
        return reader.read().then(processText);
    });
    response = JSON.parse(data);
    console.log(response);
    // download the json as a file
    let blob = new Blob([JSON.stringify(response)], {type: "application/json"});
    let url = URL.createObjectURL(blob);
    // open a new window with the json file
    window.open(url);
}


fetch(request.url, (res)=>{
    return res.json();
}).then((data)=>{
    provide(data);
});
