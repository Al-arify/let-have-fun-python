def heat_advisory(temperature, threshold, unit = "c"):
    unit = unit.lower()

    if unit == "f":
        temperature = (temperature - 32) * 5 / 9
        threshold = (threshold - 32) * 5 / 9
    elif unit != "c":
        raise ValueError("Unit must be 'c' or 'f'.")

    if temperature >= threshold:
        return True
    else:
        return False

print(heat_advisory(35, 30))
print('Fahrenheit: ', heat_advisory(95, 90, "f"))

def check_temperature(temperature, threshold, unit="c"):
    unit = unit.lower()

    if unit == "c":
        converted_temperature = (temperature * 9 / 5) + 32
        converted_unit = "F"
    elif unit == "f":
        converted_temperature = (temperature - 32) * 5 / 9
        converted_unit = "C"
else:
        raise ValueError("Unit must be 'c' or 'f'.")

    if converted_temperature >= threshold:
        return f"{converted_temperature:.1f}°{converted_unit} is at or above the threshold."
    