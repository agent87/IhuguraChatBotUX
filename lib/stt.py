from urllib import response
import requests



class convert:
    url = "https://kws.mbaza.dev.cndp.org.rw/kinyarwanda/api/v1/stt/http"
    token  = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJleHAiOjE2NjU4NDU4NDAuMDIwNzg3fQ.FIoVFEK9QNuQl5s3VjmFvtXVW_vmPdJczXOWtY3Tq8Q"
    

    def to_text(audio):
        headers = {'Authorization': 'Bearer ' + convert.token}
        audio = [('audio', audio)]
        response = requests.post(convert.url, files=audio, headers=headers)
        return response.json()['message']