def get_thresholds():
    low_threshold = float(input("Enter the low threshold temperature (°C): "))
    high_threshold = float(input("Enter the high threshold temperature (°C): "))
    if low_threshold >= high_threshold:
        print("Low threshold should be less than high threshold. Try again.")
    else:
        return low_threshold, high_threshold
     

def check_temperature(temp, low_threshold, high_threshold):
    if temp < low_threshold:
        print(f"ALERT: Temperature is too low! Current Temperature: {temp}°C")
    elif temp > high_threshold:
        print(f"ALERT: Temperature is too high! Current Temperature: {temp}°C")
    else:
        print(f"Temperature is normal: {temp}°C")

def monitor_temperature():
    low_threshold, high_threshold = get_thresholds()
    
    while True:
        temp_input = input("Enter the current temperature (or type 'q' to quit): ")
        
        if temp_input.lower() == 'q':
            print("Monitoring stopped.")
            break
        
        try:
            temp = float(temp_input)
            check_temperature(temp, low_threshold, high_threshold)
        except ValueError:
            print("Invalid input. Please enter a valid temperature.")

monitor_temperature()