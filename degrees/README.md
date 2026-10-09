# Degrees

Degrees is a beautiful, modern temperature converter with a bold split-screen interface.

## Features
- **Web App**: A modern split-screen UI that changes color dynamically based on the temperature. Includes two-way syncing, arrow key nudging, and keyboard shortcuts.
- **Console App**: A simple, error-resistant CLI utility for running conversions directly from the terminal.
- **Robust Logic**: Both versions strictly reject absolute zero violations, invalid characters (including scientific notation), missing inputs, and NaN/Infinity values.

## Tech Used
- **Web App**: HTML5, CSS3, Vanilla JavaScript (No frameworks, no build tools, no server, single file)
- **Console App**: Python 3.10+ (Standard library only)

## How to Run
- **Web App**: Open `index.html` in any modern web browser by double-clicking it.
- **Console App**: Run `python main.py` in your terminal.
- **Python Tests**: Run `python -m unittest -v test_converter.py` in your terminal.

## Project Mapping (Cognifyz Requirements)

| Step | Requirement | Implementation Details |
|------|-------------|------------------------|
| 1 | Accept temperature input | `main.py`: `input()` loop. `index.html`: Typed `<input>` with huge typography. |
| 2 | Logic for temperature conversion | `converter.py`: `celsius_to_fahrenheit()`, `fahrenheit_to_celsius()`. `index.html`: JS functions mirroring the precise logic. |
| 3 | Choose conversion direction | `main.py`: Interactive menu choices. `index.html`: Top pill segmented toggle and explicit center swap button. |
| 4 | Test with different values | `test_converter.py` covers all edge cases. `index.html` has a native `<dialog>` JS test runner showing expected vs actual. |

## Test Cases

| Case | Input | Expected Output | Status |
|------|-------|-----------------|--------|
| Normal C -> F | 0 C | 32.0 F | Passing |
| Normal C -> F | 100 C | 212.0 F | Passing |
| Cross-over | -40 C | -40.0 F | Passing |
| Normal F -> C | 32 F | 0.0 C | Passing |
| Decimals | 37 C | 98.6 F | Passing |
| Absolute Zero C | -273.15 C | -459.67 F | Passing |
| Below Abs Zero | -274 C | ValueError | Passing |
| Scientific | 1e5 | ValueError | Passing |

## Sample Console Output
```
Welcome to Degrees Console App

Menu:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice (1-3): 1
Enter temperature in Celsius: 36.6
36.6 C = 97.88 F
```

## What I learned
Building Degrees refined my knowledge of layout techniques like split screens (CSS flexbox columns/rows) and interactive animations, such as the rotating center swap button and dynamic background transitions via `@property`. I also learned to map identical parsing constraints to both Python and JS logic.

## Screenshots
*(Insert screenshots of the web app here)*
