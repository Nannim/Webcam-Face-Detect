import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.camera import Camera

class MainApp(App):
    def build(self):
        return Camera(play=True,resolution = [0,0])


if __name__ == "__main__":
    MainApp().run()