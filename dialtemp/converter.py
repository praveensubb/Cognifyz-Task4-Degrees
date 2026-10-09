import math

def parse_temperature(text, unit):
    try:
        if isinstance(text, str):
            if not text.strip():
                raise ValueError("Input cannot be empty.")
            if 'e' in text.lower():
                raise ValueError("Scientific notation not allowed.")
            val = float(text.strip())
        else:
            if text is None:
                raise ValueError("Input cannot be empty.")
            val = float(text)
    except (ValueError, TypeError):
        raise ValueError("Invalid input: Please enter a numeric value.")
    
    if math.isnan(val) or math.isinf(val):
        raise ValueError("Invalid input: Please enter a finite numeric value.")

    if unit == 'C':
        if val < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15 C).")
    elif unit == 'F':
        if val < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67 F).")
    else:
        raise ValueError("Invalid unit.")

    return val

def celsius_to_fahrenheit(c):
    c_val = parse_temperature(c, 'C')
    f = c_val * 9/5 + 32
    f = round(f, 2)
    return 0.0 if f == -0.0 else f

def fahrenheit_to_celsius(f):
    f_val = parse_temperature(f, 'F')
    c = (f_val - 32) * 5/9
    c = round(c, 2)
    return 0.0 if c == -0.0 else c
