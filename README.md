# Jutsu Code

Real-time hand-sign recognition with jutsu combo detection and visual effects, built with Python, MediaPipe, and OpenCV.

## Features

- Live webcam hand tracking (21 MediaPipe landmarks)
- Finger-state extraction for 5 fingers
- Rule-based sign recognition (no model training)
- Temporal stabilization to reduce flicker
- Sequence detection for combo matching
- Visual jutsu effect overlays with fade timing

## Current Sign Set

- Tora = index + middle up
- Ushi = open hand
- Ne = index only
- Inu = fist
- Tori = index + pinky up

## Current Combos

- Ne -> Tora -> Inu: KATON - FIREBALL JUTSU
- Ushi -> Ne -> Tora: SHADOW CLONE JUTSU
- Tori -> Inu -> Ushi: CHIDORI

## Project Structure

- main.py: App entry point and render loop
- hand_detector.py: Hand landmark detection + finger state extraction
- signs.py: Sign definitions and matching
- stabilizer.py: Temporal smoothing for stable sign confirmation
- sequence.py: Sign change sequence tracking
- combos.py: Combo definitions and lookup
- JUTSU_GUIDE.md: End-user guide for sign execution
- PROJECT_OVERVIEW.md: Detailed build notes and stage progression

## Requirements

- Python 3.11
- Webcam

Python packages:

- opencv-python
- mediapipe

## Quick Start (Windows PowerShell)

1. Create and activate virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install opencv-python mediapipe
```

3. Run the app:

```powershell
python main.py
```

4. Quit by pressing Q in the OpenCV window.

## How Detection Works

1. Capture frame from webcam.
2. Detect hand landmarks.
3. Convert landmarks to [thumb, index, middle, ring, pinky] states.
4. Match finger states to a known sign pattern.
5. Stabilize sign over recent frames.
6. Append only sign changes to a short sequence buffer.
7. Match sequence against combo table and trigger effect.

## Troubleshooting

- No camera feed:
  - Change camera index in main.py from VideoCapture(0) to VideoCapture(1).
- Signs flicker:
  - Improve lighting, reduce motion, and keep hand centered.
- Combo not triggering:
  - Hold each sign long enough to stabilize before changing.
- Startup import errors:
  - Ensure the virtual environment is active and dependencies are installed.

## Safety for GitHub Push

This repository now includes .gitignore entries for:

- venv and other local environments
- __pycache__ and Python bytecode
- local .env files
- common editor/OS artifacts
