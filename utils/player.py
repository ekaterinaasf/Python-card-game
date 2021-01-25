import Card from card.py

class Player:
```python
  A class `Player` that contains these attributes:
    :param cards: A list of `Card`. In a real card game, this is equivalent to the cards that the player has in his hands.
    :param number_of_cards: An int starting a 0.
    :param turn_count: An int starting a 0.
    :param history: A list of `Card` that will contain all the cards played by the player
    :return: A
```

  def __init__(self, cards, turn_count, number_of_cards, history):
    self.cards=cards
    self.turn_count=turn_count
    self.number_of_cards=number_of_cards

And some methods:

- `play()` that will:
  - **randomly** pick a `Card` in `cards`.
  - Add the `Card` to the `Player`'s `history`.
  - Print: `{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}`.
  - return the `Card`.
