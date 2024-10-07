def choose_input_unit():
    print("Available units: meters (m), feet (ft), kilometers (km), miles (mi)")
    return input("Choose input unit: ").lower()

def enter_input_value():
    return float(input("Enter input value: "))

def select_output_unit():
    print("Available units: meters (m), feet (ft), kilometers (km), miles (mi)")
    return input("Select output unit: ").lower()

def perform_conversion(input_unit, input_value, output_unit):
    # Conversion factors to meters
    to_meters = {
        "m": 1,
        "ft": 0.3048,
        "km": 1000,
        "mi": 1609.34
    }
    
    # Convert input to meters
    meters = input_value * to_meters[input_unit]
    
    # Convert meters to output unit
    return meters / to_meters[output_unit]

def display_output_value(result):
    print(f"Converted value: {result:.4f}")

def main():
    print("Unit Converter")
    
    # Input
    input_unit = choose_input_unit()
    input_value = enter_input_value()
    output_unit = select_output_unit()
    
    # Conversion
    result = perform_conversion(input_unit, input_value, output_unit)
    
    # Output
    display_output_value(result)

if __name__ == "__main__":
    main()