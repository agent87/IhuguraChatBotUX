from urllib import response
import requests



class convert:
    url = "https://kws.mbaza.dev.cndp.org.rw/kinyarwanda/api/v1/stt/http"
    token  = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJleHAiOjE2NjU4NDU4NDAuMDIwNzg3fQ.FIoVFEK9QNuQl5s3VjmFvtXVW_vmPdJczXOWtY3Tq8Q"
    
    def __init__(self) -> None:
        pass

    def to_text(self, audio):
        headers = {'Authorization': 'Bearer ' + self.token}
        audio = [('audio', audio)]
        response = requests.post(self.url, files=audio, headers=headers)
        return response.json()['message']