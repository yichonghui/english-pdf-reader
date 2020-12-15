import threading
import time
from reader.controller import con
from reader.translate import MyTranslator


class WatchClip(threading.Thread):
    def __init__(self):
        super(WatchClip, self).__init__()
        self.translator = MyTranslator()
        self.name = ""
        self.expire = False
        self.text = ''

    def run(self):
        recent_text = self.text
        while True and not self.expire:
            cur_text = self.text
            if cur_text == recent_text:
                time.sleep(0.1)
            else:
                recent_text = cur_text
                self.update(cur_text)

    def setTranslateText(self, inputText):
        self.text = inputText

    def update(self, cur_text):
        con.translationChanged.emit(
            self.translator.get_translation_by_google(cur_text))

    def expired(self):
        self.expire = True
