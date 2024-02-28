
document.title = "Mon Profil Simplon";


// add chat-msg-user = questionEl
const chatAddEl = document.getElementById("chat-add");
let questionEl = document.createElement("p");
questionEl.textContent = "Votre conversation";
questionEl.classList.add("chat-msg-user");
chatAddEl.appendChild(questionEl);

// add chat-msg-assist = answerEl
let answerEl = document.createElement("p");
answerEl.textContent = "";
answerEl.classList.add("chat-msg-assist");
chatAddEl.appendChild(answerEl);


// add chat function and connect with API
function addNewQuestion(){
    let prompt = window.prompt("Quelle est ta question?");

    let chatBoxEl = document.getElementById("chat-add");

    let msgEl = document.createElement("p");
    msgEl.innerText = prompt;
    chatBoxEl.appendChild(msgEl);
    msgEl.classList.add("chat-msg");
    msgEl.classList.add("chat-msg-quest");
    
    let answerEl= document.createElement("p");
    answerEl.innerText = "...";
    chatBoxEl.appendChild(answerEl);
    answerEl.classList.add("chat-msg");
    answerEl.classList.add("chat-msg-answ");

    fetch('http://localhost:8000/'+ prompt, {method: "POST"})
        .then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data);
            answerEl.innerText = data;
        });
}

