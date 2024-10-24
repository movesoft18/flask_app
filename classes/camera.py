from time import time

class Camera(object):
    def __init__(self) -> None:
        self.frames = [open('./images/'+f+'.jpg', 'rb').read() for f in ['1','2','3','4','5']]

    def get_frame(self):
        return self.frames[int(time()) % 5]