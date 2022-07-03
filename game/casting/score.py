from game.casting.actor import Actor


class Score(Actor):
    """
    Attributes:
        _point (int): The score.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        """Returns the current score.
        
        Returns:
            int: The current score.
        """
        return self._points

    def add_points(self, points):
        """Updates the score to the given one.
        
        """
        self._points += points
        self.set_text(f"Score: {self._points}")
