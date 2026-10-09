# ThermoSwitch

ThermoSwitch is a complete, production-quality temperature converter program that allows users to seamlessly switch between Celsius and Fahrenheit.

## Features
- **Web App**: A modern UI with live conversion.
- **Console App**: A straightforward CLI utility to run conversions directly from the terminal.
- **Robust Logic**: Both versions reject absolute zero violations, invalid characters, missing inputs, and NaN/Infinity values with user-friendly errors.

## How to Run
- **Web App**: Open `index.html` in any modern web browser.
- **Console App**: Run `python main.py` in your terminal.
- **Python Tests**: Run `python -m unittest -v test_converter.py` in your terminal.

## Project Mapping (Cognifyz Requirements)

| Step | Requirement | Implementation Files and Functions |
|------|-------------|------------------------------------|
| 1 | Accept temperature input | `index.html` input + `main.py` input prompts |
| 2 | Logic for temperature conversion | `converter.py` logic and the JS `convert` function |
| 3 | Choose conversion direction | Toggle in `index.html`, menu in `main.py` |
| 4 | Test with different values | `test_converter.py` and the in-page Run tests |

## Screenshots
*(Insert screenshots of the web app here)*
