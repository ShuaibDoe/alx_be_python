FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET

def get_temperature_input():
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            return temp
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_temperature_scale():
    while True:
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if scale in ('C', 'F'):
            return scale
        print("Invalid scale. Please enter 'C' or 'F'.")

def display_conversion(temp, scale):
    if scale == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"\n{temp}°C = {converted}°F")
    else:
        converted = convert_to_celsius(temp)
        print(f"\n{temp}°F = {converted}°C")

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    while True:
        try:
            temperature = get_temperature_input()
            scale = get_temperature_scale()
            display_conversion(temperature, scale)
            
            if input("\nConvert another temperature? (y/n): ").lower() != 'y':
                print("Goodbye!")
                break
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break

if __name__ == "__main__":
    main()
