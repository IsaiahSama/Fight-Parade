"""This file is used to manage the 'Message' class"""

message_html = {
    "system": """
    <div class="systemMessage" id={sender_name}>
        <p>{content}</p>
    </div>""",
    "player": """
    <div class="playerMessage">
        <div class="playerMessageHeader">
            <img
            src="https://avatars.dicebear.com/api/human/{sender_name}.svg"
            alt=""
            />
            <p>{sender_name}</p>
        </div>
        <div class="playerMessageBody">
            <p>{content}</p>
        </div>
    </div>""",
    "other": """
    <div class="playerMessage fighter">
        <div class="playerMessageHeader">
            <img
            src="https://avatars.dicebear.com/api/human/{sender_name}.svg"
            alt=""
            />
            <p>{sender_name}</p>
        </div>
        <div class="playerMessageBody">
            <p>{content}</p>
        </div>
    </div>"""
}

class Message:
    def __init__(self, channel_id:int, sender:str, sender_name:str, content:str):
        self.channel_id = channel_id
        self.sender = sender
        self.sender_name = sender_name
        self.content = content

    def get_html(self):
        return message_html[self.sender].format(content=self.content, sender_name=self.sender_name)