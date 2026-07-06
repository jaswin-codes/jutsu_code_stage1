# sequence.py
from collections import deque

class SequenceDetector:
    def __init__(self, max_length=3):
        self.sequence = deque(maxlen=max_length)
        self.last_sign = None

    def update(self, stable_sign):
        """
        Only adds a sign to the sequence when it CHANGES.
        Returns current sequence as a list.
        """
        if stable_sign and stable_sign != self.last_sign:
            self.sequence.append(stable_sign)
            self.last_sign = stable_sign
        return list(self.sequence)

    def reset(self):
        self.sequence.clear()
        self.last_sign = None