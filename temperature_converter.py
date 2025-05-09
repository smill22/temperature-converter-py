# temperature_converter.py

class TemperatureConverter:

    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9
