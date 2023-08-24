const chatWindow = document.getElementById("chatWindow");

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
    chatWindow.scrollTop = chatWindow.scrollHeight;
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
  sendMessage("system", "system", content);
};

// Action Buttons
const restoreActions = () => {
  const container = document.getElementById("actionButtonsContainer");
  fetch("/get/buttons/action/")
    .then((resp) => resp.text())
    .then((data) => {
      container.innerHTML = data;
      htmx.process(container);
    });
};

const doJob = () => {
  sendPlayerMessage("I want to do a job!");
  sendSystemMessage("Let's see what we have available.");
  fetch("/get/job/")
    .then((response) => response.json())
    .then((data) => {
      if ("ERROR" in data) {
        sendSystemMessage(data["ERROR"]);
        return;
      }
      sendSystemMessage(data["DESCRIPTION"]);
      sendSystemMessage("<b>You " + data["STATUS"] + "</b>");
      sendSystemMessage("<i>" + data["RESPONSE"] + "</i>");
    });

  setTimeout(restoreActions, 5000);
};

const doQuest = () => {
  sendPlayerMessage("I'm making a reQUEST");
  sendSystemMessage("Comedy... Alright, here's what I have for you.");
  setTimeout(restoreActions, 5000);
};

const doTraining = () => {
  sendPlayerMessage("TIME TO TRAIN!");
  sendSystemMessage("That's the spirit!");
  sendSystemMessage("What would you like to train? Select from below!");
  setTimeout(restoreActions, 5000);
};
