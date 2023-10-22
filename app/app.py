from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class ClickButtons(App):
  def build(self):
    # define the window
    Window.clearcolor = '#34495e'
    Window.size = (150, 300)
    self.window = GridLayout(cols=1)
    self.window.size_hint = (0.8, 0.95)
    self.window.pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}

    # define the widgets
    title = Label(text='Click a Button',
                  font_size = 18,
                  bold = True,
                  color = '#ecf0f1')
    self.count = 0
    self.count_label = Label(text=str(self.count),
                             font_size = 24,
                             bold = True,
                             color = '#ecf0f1')
    self.add_button = Button(text='+',
                             font_size = 24,
                             bold = True,
                             background_normal = '',
                             background_color = '#27ae60')
    self.subtract_button = Button(text='-',
                                  font_size = 24,
                                  bold = True,
                                  background_normal = '',
                                  background_color = '#c0392b')

    # add widgets
    self.window.add_widget(title)
    self.window.add_widget(self.add_button)
    self.window.add_widget(self.count_label)
    self.window.add_widget(self.subtract_button)

    self.add_button.bind(on_press=self.add_callback)
    self.subtract_button.bind(on_press=self.subtract_callback)

    return self.window

  def add_callback(self, instance):
    self.count += 1
    self.count_label.text = str(self.count)

  def subtract_callback(self, instance):
    self.count -= 1
    self.count_label.text = str(self.count)

if __name__ == "__main__":
  ClickButtons().run()
