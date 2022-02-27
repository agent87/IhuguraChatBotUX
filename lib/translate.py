import requests
import json


class translator:
    api_url = "https://translate.googleapis.com/translate_a/single"
    client = "?client=gtx&dt=t&sl=rw&tl=en"
    dt = "&dt=t"

    def __init__(self) -> None:
        return None

    def to_kinyrwanda(self, text):
        sl = "&sl=rw"
        tl = "&tl=en"
        r = requests.get(self.api_url+ self.client + self.dt + sl + tl + "&q=" + text)
        return json.loads(r.text)[0][0][0]
    def to_english(self, text):
        sl = "&sl=en"
        tl = "&tl=rw"
        r = requests.get(self.api_url+ self.client + self.dt + sl + tl + "&q=" + text)
        return json.loads(r.text)[0][0][0]


if __name__ == '__main__':
    pass

    