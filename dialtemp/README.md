# DialTemp

DialTemp is a modern temperature converter program featuring an interactive, physics-inspired dial interface.

## Features
- **Web App**: A modern neumorphic UI with an interactive SVG dial. The dial's accent color dynamically shifts smoothly based on the temperature. Includes two-way syncing between the dial and exact text input.
- **Console App**: A straightforward CLI utility to run conversions directly from the terminal.
- **Robust Logic**: Both versions reject absolute zero violations, invalid characters (including scientific notation), missing inputs, and NaN/Infinity values with clear errors.

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
| 1 | Accept temperature input | `main.py`: `input()` in loop. `index.html`: Typed `<input>` and interactive SVG dial slider (two-way sync). |
| 2 | Logic for temperature conversion | `converter.py`: `celsius_to_fahrenheit()`, `fahrenheit_to_celsius()`. `index.html`: JS functions mirroring the logic. |
| 3 | Choose conversion direction | `main.py`: Interactive menu choices. `index.html`: Segmented toggle and explicit swap button. |
| 4 | Test with different values | `test_converter.py` covers all edge cases. `index.html` has a collapsible JS test runner showing expected vs actual. |

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
Welcome to DialTemp Console App

Menu:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice (1-3): 1
Enter temperature in Celsius: 36.6
36.6 C = 97.88 F
```

## What I learned
Building DialTemp enhanced my understanding of SVG mathematics for circular interactive UI components, state synchronization between multiple input modalities, and enforcing identical robust error-handling constraints across Python and JavaScript.

## Screenshots
*(Insert screenshots of the web app here)*
