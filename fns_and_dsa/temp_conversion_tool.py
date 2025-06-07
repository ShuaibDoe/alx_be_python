def FAHRENHEIT_TO_CELSIUS_FACTOR(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def CELSIUS_TO_FAHRENHEIT_FACTOR(celsius):
    return (celsius * 9 / 5)  + 32
C_TO_F = CELSIUS_TO_FAHRENHEIT_FACTOR
F_TO_C = FAHRENHEIT_TO_CELSIUS_FACTOR 
def convert_temp(temp, scale):
    """Convert between Celsius and Fahrenheit"""
    if scale == 'C':
        return temp * C_TO_F + 32
    elif scale == 'F':
        return (temp - 32) * F_TO_C
    else:
        raise ValueError("Invalid scale. Use 'C' or 'F'")

def main():
    print("Temperature Converter")
    while True:
        try:
            temp = float(input("Enter temperature: "))
            scale = input("Celsius or Fahrenheit? (C/F): ").upper()
            result = convert_temp(temp, scale)
            print(f"{temp}°{scale} = {result:.1f}°{'F' if scale == 'C' else 'C'}")
            if input("Convert another? (y/n): ").lower() != 'y':
                break
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
if __name__ == "__main__":
    main()