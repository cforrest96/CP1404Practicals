
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty
NAMELIST = ["Jake", "Lachlan", "Grant"]

class DynamicKivyWidgets(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def build(self):

        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_kivy_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list entries"""

        for name in NAMELIST:
            temp_label = Label(text=name, id=name)
            # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_label)


DynamicKivyWidgets().run()
