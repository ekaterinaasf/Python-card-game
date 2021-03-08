class Symbol:
```python
def __init__(color: str, icon: int) -> str:
    """
    Function that will initialize the class with 2 attributes.

    :param color: A string that can have 2 values: black and red.
    :param icon: A single character out of this list `[♥, ♦, ♣, ♠]`.
    :return: An string that is the result of the two params being added to each other.
    """
    result = number_one + number_two
    return result
```
    def __init__(self, color, icon):
        self.color=color
        self.icon=icon


class Card(Symbol):
```python
    This class s inherits from class `Symbol` and have an additional attribute
    `value` which is a string (one of  `['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']`)
```
    def __init__(self, color: str, icon: int, value: str):
        self.value=value
        
        
    
