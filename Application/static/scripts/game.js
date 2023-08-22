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
  sendMessage("system", "system", content);
};

const doJob = () => {
  sendPlayerMessage("I want to do a job!");
  sendSystemMessage("Oh you want to do a job I see. Bet!");
};
