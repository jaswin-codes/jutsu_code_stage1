# stabilizer.py
from collections import deque

class SignStabilizer:
    def __init__(self, buffer_size=10, confirm_threshold=7):
        """
        buffer_size      : how many recent frames to track
        confirm_threshold: how many of those frames must agree to confirm
        
        At 30fps, 10 frames = ~0.33 seconds
        7/10 frames agreeing = sign must be consistent 70% of the time
        """
        self.buffer = deque(maxlen=buffer_size)
        self.confirm_threshold = confirm_threshold
        self.confirmed_sign = None

    def update(self, raw_sign):
        """
        Feed in the raw sign detected this frame.
        Returns the stabilized/confirmed sign (or None).
        """
        self.buffer.append(raw_sign)

        if len(self.buffer) < self.buffer.maxlen:
            return None   # not enough frames yet

        # Count how many frames in the buffer agree on each sign
        counts = {}
        for sign in self.buffer:
            if sign is None:
                continue
            counts[sign] = counts.get(sign, 0) + 1

        # Find the most common sign
        if not counts:
            self.confirmed_sign = None
            return None

        best_sign, best_count = max(counts.items(), key=lambda x: x[1])

        if best_count >= self.confirm_threshold:
            self.confirmed_sign = best_sign
        else:
            self.confirmed_sign = None

        return self.confirmed_sign

    def reset(self):
        self.buffer.clear()
        self.confirmed_sign = None