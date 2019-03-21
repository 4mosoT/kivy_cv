from kivy.app import App
from custom_camera.custom_camera import CameraWidget, CustomCamera

from kivy.base import Builder

Builder.load_file("custom_camera/custom_camera.kv")


class TestCamera(App):

    def build(self):
        camera = CameraWidget()
        return camera


TestCamera().run()
