const chatWindow = document.getElementById("chatWindow");
window.setInterval(function () {
  chatWindow.scrollTop = chatWindow.scrollHeight;
}, 500);

const chatBody = document.getElementById("chatBody");

// Event listener
var socket = io();

socket.on("connect", () => {
  socket.emit("introduce", { data: "Guess who just connected!" });
});

const messages = [];

socket.on("message", (data) => {
  let length = messages.length + 1;
  messages.push(data["body"]);

  setTimeout(() => {
    let messageElement = document.createElement("div");
    chatBody.appendChild(messageElement);
    messageElement.outerHTML = data["body"];
    messages.splice(0, 1);
  }, 1000 * length);
});

const sendMessage = (sender, sender_name, content) => {
  data = JSON.stringify({
    sender,
    sender_name,
    content,
  });

  socket.emit("message", data);
};

const sendPlayerMessage = (content) => {
  sendMessage("player", "Timmy", content);
};

const sendSystemMessage = (content) => {
  sendMessage("other", "system", content);
};

// Gaming Buttons
const doJob = () => {
  sendPlayerMessage("I want to do a job!");
  sendSystemMessage("Let's see what we have available.");
  fetch("/get/job/")
    .then((response) => response.json())
    .then((desc) => {
      sendSystemMessage(desc["RESPONSE"]);
    });
};

const doQuest = () => {
  sendPlayerMessage("I'm making a reQUEST");
  sendSystemMessage("Comedy... Alright, here's what I have for you.");
};

const doTraining = () => {
  sendPlayerMessage("TIME TO TRAIN!");
  sendSystemMessage("That's the spirit!");
};
