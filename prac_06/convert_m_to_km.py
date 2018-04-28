from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Caleb Forrest'

MILES_TO_KM = 1.60934

class ConvertDistance(App):
    """ ConvertDistance is an app to change miles to kilometres"""
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def convert_miles(self):
        try:
            value = self.check_input()
            kilometres = value * MILES_TO_KM
            self.root.ids.output_label.text = str(kilometres)
        except TypeError:
            self.root.ids.output_label.text = '0'

    def check_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def do_increment(self, increment):
        try:
            value = self.check_input() + increment
            self.root.ids.input_miles.text = str(value)
            self.convert_miles()
        except ValueError:
            return 0

ConvertDistance().run()