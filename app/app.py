from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class My_First_Kivy_App(App):
  def build(self):
    # define the window
    self.window = GridLayout(cols=1)

    # define the widgets

    # add the widgets

    return self.window

if __name__ == "__main__":
  My_First_Kivy_App().run()

