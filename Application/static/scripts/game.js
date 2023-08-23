const chatWindow = document.getElementById("chatWindow");
window.setInterval(function () {
  chatWindow.scrollTop = chatWindow.scrollHeight;
}, 500);

const sendMessage = (sender, sender_name, content) => {
  data = {
    method: "POST",
    headers: {
      "Content-type": "application/json; charrset=UTF-8",
    },
    body: JSON.stringify({
      sender,
      sender_name,
      content,
    }),
  };
  fetch("/add/message/", data);
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

// Event listener
$(document).ready(() => {
  var socket = io();

  socket.on("connect", () => {
    socket.emit("introduce", { data: "Guess who just connected!" });
  });

  socket.on("response", (message) => {
    console.log("Just received a message from the server!");
    console.log(message["data"]);
  });
});
