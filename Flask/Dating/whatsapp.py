import os
import requests

class WhatsApp:
    
    def __init__(self):
        self.url = "https://api.intobo.com/SendMessage/fc934025f14b4d7930c73fd29c978fcba01e474f/14623"
        self.headers = {'x-api-key': os.environ['x-api-key']}

    def Send(self,toNumber,msgText):
        payload = "{\"to_number\": \""+toNumber+"\",\"type\": \"text\",\"message_text\": \""+msgText+"\"}"
        response = requests.request("POST", self.url, data=payload.encode('utf-8') , headers=self.headers)
        return response.text

