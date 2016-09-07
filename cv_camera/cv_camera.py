from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty

import cv2


class Cv_Camera(Image):
    cap = cv2.VideoCapture(0)
    width = NumericProperty(640)
    height = NumericProperty(480)
    image_function = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Cv_Camera, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / 30.)

        self.texture = Texture.create(size=(self.width, self.height))


    def update(self, *args):
        # Take a frame
        image = self.read()[1]

        # Where magic takes place
        image = self.image_function(image)
        if self.texture.size != image.shape[1::-1]:
            self.texture = Texture.create(size=image.shape[1::-1])

        # Numpy array to texture
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, -1)
        numpy_data = image.tostring()
        self.texture.blit_buffer(numpy_data, bufferfmt="ubyte", colorfmt="rgb")
        self.canvas.ask_update()

    def read(self):
        return self.cap.read()
