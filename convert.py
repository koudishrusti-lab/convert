def converted_values(unit, value):
    if unit == "km":
        return value * 0.621371
    else :
        return value * 1.609341



if __name__ == "__main__":
    try:
        value = float(input("Enter the value: "))
        unit = input("Enter the unit (km/miles): ").lower()
    except EOFError:
        value = 5
        unit = "km"

    print("Converted value:", converted_values(unit, value))
