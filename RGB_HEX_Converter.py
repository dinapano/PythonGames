"""In this project, we’ll use Bitwise operators to build a calculator that can convert RGB values to
Hexadecimal (hex) values, and vice-versa.

We’ll add three methods to the project:

A method to convert RGB to Hex
A method to convert Hex to RGB
A method that starts the prompt cycle
The program should do the following:

Prompt the user for the type of conversion they want
Ask the user to input the RGB or Hex value
Use Bitwise operators and shifting in order to convert the value
Print the converted value to the user
It’s useful to know some background on RGB and hex values, so we recommend reading the resources we linked to."""


def rgb_hex():
    invalid_msg = "Invalid values were entered. Please enter values within the according boundaries: [0,255]"

    red = int(input("Enter a value for red: "))
    if red < 0 or red > 255:
        print(invalid_msg)
        return None

    green = int(input("Enter a value for green: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return None

    blue = int(input("Enter a value for blue: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return None

    val = (red << 16) + (green << 8) + blue
    value = hex(val)[2:].upper()
    print(value)

def hex_rgb():
    hex_val = input("Enter hexadecimal value: ")
    if len(hex_val) != 6:
        invalid_msg = "An invalid value was entered. Please enter a hexadecimal value six characters long: ]"
    else:
        hex_val = int(hex_val, 16)

    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print(f"{red} + {green} + {blue}")

def convert():
    while True:
        option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")

        if option == "1":
            print("RGB to HEX...")
            rgb_hex()
        elif option == "2":
            print("HEX to RGB...")
            hex_rgb()
        elif option == "X":
            break
        else:
            print("Error.")

convert()
