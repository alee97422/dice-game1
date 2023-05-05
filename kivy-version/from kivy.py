from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import random

class SexDiceGameApp(App):
    def build(self):
        # Define the widgets
        layout = BoxLayout(orientation='vertical')
        self.result_label = Label(text='Press the roll button to start the game!', font_size='30sp', halign='center', valign='middle')
        roll_button = RollButton(text='Roll the dice!', on_roll=self.on_roll, size_hint=(1, .2))
        layout.add_widget(self.result_label)
        layout.add_widget(roll_button)
        return layout

    def on_roll(self, button):
        # Roll the dice and display the result
        body_part = random.choice(Body_Parts)
        act = random.choice(Acts)
        players = random.sample(Players, 2)
        result = f'{players[0]} {act} {players[1]}' + ' ' + 'on the' + ' ' + body_part
        self.result_label.text = result

class RollButton(Label):
    def __init__(self, text='', on_roll=None, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.on_roll = on_roll

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.on_roll:
                self.on_roll(self)
            return True

# Define the game data
Body_Parts = ["lips", "genitals","thigh","neck", "chest","foot"]
Acts = ["suck", "lick", "nibble","caress","kiss","massage"]
Players = ["Player1", "Player2", "Player3"]

# Run the app
if __name__ == '__main__':
    SexDiceGameApp().run()
