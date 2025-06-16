# Terrafirmacraft Automation and Python Toolset

This repository contains a collection of Python-based projects ranging from Minecraft automation to OpenCV computer vision and algorithmic scripting. It includes fully-automated gameplay mechanics for the Terrafirmacraft Minecraft mod, experimental object tracking systems, facial recognition pipelines, and educational utilities in mathematics and parallel execution.

---

## Terrafirmacraft Automation Tools

### Anvil Minigame Automation

This project automates and assists with the Terrafirmacraft Anvil Minigame: a precision-based smithing mechanic in the Minecraft mod Terrafirmacraft. The minigame requires players to perform exact sequences of deformation actions (e.g., BEND, DRAW, PUNCH) on heated metal ingots to forge tools.

This codebase analyzes the required action sequence, calculates positional offsets, and executes optimal input patterns using image recognition and simulated mouse events. It supports vanilla and modded tool recipes, user-defined items, and includes a GUI for managing smithing actions and rule sets.

### Knapping and Clay Molding Automation

This project automates the knapping and clay molding interfaces in Terrafirmacraft by simulating grid-based crafting actions. These interfaces use a 5x5 grid where specific tiles must be selected to form item patterns such as tools or containers.

The script uses Python and `pyautogui` to replicate these patterns by clicking mapped screen coordinates corresponding to each item\u2019s shape. Users specify the item and quantity, and the program performs the full interaction loop: opening the interface, executing the pattern, and repeating as needed.

It supports a wide range of knapped tools (e.g., axe, knife, hammer) and clay molds (e.g., pickaxe, pot, bowl), with all pattern data defined and selectable in-script. This eliminates the need for manual input and allows for fast, repeatable crafting operations.

---

## OpenCV Computer Vision Scripts

### `openCV-18.py`

Uses OpenCV and a webcam to detect objects based on HSV color thresholds controlled by interactive trackbars. It applies a binary mask to isolate regions of interest and draws bounding rectangles around detected contours. Useful for calibrating color-based object tracking in real time.

### `openCV-19.py`

An extension of `openCV-18.py`, this script detects multiple HSV ranges using two independent hue ranges and combines the masks. It dynamically moves the OpenCV window based on the tracked object\u2019s position, allowing the video feed to follow the detected object on-screen.

### `openCV-26.py`

Performs batch face encoding and dataset generation. Loads images from a folder (`demoImages`), computes facial encodings using `face_recognition`, and serializes both names and encodings into `train.pkl` using `pickle`. This prepares a dataset for later recognition.

### `openCV-27.py`

Performs live face recognition using a webcam and the encodings from `train.pkl`. Detects faces in real time, compares them to known encodings, and labels them in-frame. Displays frame rate and identity annotations.

### `openCV-default.py`

Minimal script for initializing and displaying a webcam feed at a specified resolution and frame rate. Serves as a base for testing camera functionality or integrating custom vision tasks.

---

## Algorithmic and Utility Scripts

### `growbinary.py`

Prints an incrementing binary counter to the console using Python\u2019s formatting. Demonstrates real-time binary progression.

### `hex table to binary.py`

Reads hexadecimal values from `hexfile.txt`, converts them to zero-padded binary strings, and writes them to `binaryfile.txt` as a continuous bitstream.

### `concurrent futures.py`

Demonstrates parallel execution using Python\u2019s `concurrent.futures.ThreadPoolExecutor`. Runs multiple sleep tasks concurrently and measures total runtime. A basic threading demonstration.

### `fortest.py`

Defines a class `exObject` with an overloaded `__len__` method that returns the cube of its internal value. Illustrates operator overloading and custom object behavior.

### `python factorization.py`

Interactively prompts the user for integers and prints their factors. Loops until the user declines. Demonstrates loops and modular arithmetic.

### `random factors.py`

Automatically generates random integers under 100 and prints their factors with a delay. Similar to `python factorization.py`, but automated and non-interactive.

### `random numbers keyboard.py`

Generates random numbers, computes their factors, and uses `pyautogui` to type them into the active window as Markdown code blocks. Includes randomized delays and hotkeys for demo scripting.

### `testing quadratics.py`

Brute-forces integer coefficient pairs to find quadratic equations where the product of the roots is smaller in magnitude than their sum. Explores algebraic relationships and factor behavior.

---

## Requirements

- Python 3.x
- `pyautogui`
- `opencv-python`
- `face_recognition`
- `numpy`
- `pickle`

Install all dependencies via:

```bash
pip install -r requirements.txt
```

