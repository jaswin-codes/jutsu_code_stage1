import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_styles = mp.solutions.drawing_styles

        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

    def find_hands(self, frame, draw=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)
        all_hands_landmarks = []

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_styles.get_default_hand_landmarks_style(),
                        self.mp_styles.get_default_hand_connections_style()
                    )
                all_hands_landmarks.append(hand_landmarks)

        return frame, all_hands_landmarks

    def get_landmark_list(self, hand_landmarks, frame_shape):
        h, w, _ = frame_shape
        landmark_list = []

        for lm in hand_landmarks.landmark:
            cx, cy = int(lm.x * w), int(lm.y * h)
            landmark_list.append((cx, cy))

        return landmark_list

    def get_finger_states(self, landmark_list):
        """
        Returns [thumb, index, middle, ring, pinky]
        1 = up, 0 = down
        """
        if len(landmark_list) < 21:
            return [0, 0, 0, 0, 0]

        fingers = []

        # --- Thumb ---
        # Compare tip (4) vs base of index finger (5) using x axis
        # This accounts for which side the thumb is on relative to the palm
        thumb_tip_x  = landmark_list[4][0]
        palm_anchor_x = landmark_list[5][0]   # base of index finger

        # Also check wrist (0) to determine hand orientation
        wrist_x = landmark_list[0][0]

        # If wrist is to the LEFT of index base → right hand in mirror view
        # Thumb is UP if tip is further LEFT than the palm anchor
        if wrist_x < palm_anchor_x:
            fingers.append(1 if thumb_tip_x > palm_anchor_x else 0)
        else:
            fingers.append(1 if thumb_tip_x < palm_anchor_x else 0)

        # --- Four fingers (y-axis comparison) ---
        tip_ids   = [8, 12, 16, 20]
        joint_ids = [6, 10, 14, 18]

        for tip, joint in zip(tip_ids, joint_ids):
            tip_y   = landmark_list[tip][1]
            joint_y = landmark_list[joint][1]
            fingers.append(1 if tip_y < joint_y else 0)

        return fingers