from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

class SexDiceGameApp(App):
    def build(self):
        # Define the widgets
        layout = BoxLayout(orientation='vertical')
        self.result_label = Label(text='Press the roll button to start the game!', font_size='15sp', halign='center', valign='middle')
        self.players_input = TextInput(multiline=False, hint_text='Enter number of players', size_hint_x=0.5)
        self.names_input = TextInput(multiline=False, hint_text='Enter player names separated by commas', size_hint_x=0.5)
        roll_button = RollButton(text='Roll the dice!', on_roll=self.on_roll, size_hint=(1, .2))
        layout.add_widget(self.result_label)
        layout.add_widget(self.players_input)
        layout.add_widget(self.names_input)
        layout.add_widget(roll_button)
        return layout

    def on_roll(self, button):
        # Get the number of players and their names
        num_players = int(self.players_input.text)
        players = self.names_input.text.split(',')
        players = [player.strip() for player in players][:num_players]
        if len(players) < 2:
            self.result_label.text = 'Error: need at least 2 players'
            return

        # Roll the dice and display the result
        body_part = random.choice(Body_Parts)
        act = random.choice(Acts)
        players = random.sample(players, 2)
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

# Run the app
if __name__ == '__main__':
    SexDiceGameApp().run()




import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.cyan,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
