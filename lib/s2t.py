from urllib import response
import requests



class convert:
    url = "https://mbaza.dev.cndp.org.rw/deepspeech/api/api/v1/stt/http"
    token  = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMywiZXhwIjoxNjQ4NDU3NDA4LjEwMTc1OX0.0MssHAzOXWiHzkCACqhddYlw_-BMpvLy8wpsKYLKm6U"
    
    def __init__(self) -> None:
        pass

    def to_text(self, audio):
        headers = {'Authorization': 'Bearer ' + self.token}
        audio = [('audio', audio)]
        response = requests.post(self.url, files=audio, headers=headers)
        return response.json()['message']