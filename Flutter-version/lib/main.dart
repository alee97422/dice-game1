import 'package:flutter/material.dart';
import 'dart:math';

void main() {
  runApp(SexDiceGameApp());
}

class SexDiceGameApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Erotic Dice Game',
      home: SexDiceGameScreen(),
    );
  }
}

class SexDiceGameScreen extends StatefulWidget {
  @override
  _SexDiceGameScreenState createState() => _SexDiceGameScreenState();
}

class _SexDiceGameScreenState extends State<SexDiceGameScreen> {
  String _resultText = 'Press the roll button to start the game!';
  TextEditingController _playersController = TextEditingController();
  TextEditingController _namesController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Erotic Dice Game'),
      ),
      body: Padding(
        padding: EdgeInsets.all(32.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              _resultText,
              style: TextStyle(
                fontSize: 20.0,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 16.0),
            TextField(
              controller: _playersController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                hintText: 'Enter number of players',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 16.0),
            TextField(
              controller: _namesController,
              decoration: InputDecoration(
                hintText: 'Enter player names separated by commas',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 16.0),
            ElevatedButton(
              child: Text('Roll the dice!'),
              onPressed: _onRollButtonPressed,
            ),
          ],
        ),
      ),
    );
  }

  void _onRollButtonPressed() {
    int numPlayers = int.tryParse(_playersController.text) ?? 0;
    List<String> players = _namesController.text.split(',').map((name) => name.trim()).toList();
    players = players.take(numPlayers).toList();
    if (players.length < 2) {
      setState(() {
        _resultText = 'Error: need at least 2 players';
      });
      return;
    }

    String bodyPart = BodyParts[Random().nextInt(BodyParts.length)];
    String act = Acts[Random().nextInt(Acts.length)];
    players.shuffle();
    String result = '${players[0]} $act ${players[1]} on the $bodyPart';
    setState(() {
      _resultText = result;
    });
  }
}

const List<String> BodyParts = ['lips', 'genitals', 'thigh', 'neck', 'chest', 'foot'];
const List<String> Acts = ['suck', 'lick', 'nibble', 'caress', 'kiss', 'massage'];
