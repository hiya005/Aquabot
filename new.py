"""
Simple Automated Watering System Simulator
Author: Hiya
Description:
Simulates soil moisture monitoring and watering control.
Includes rain check, manual override, and optional user input.
"""


# ----------------------------
# Configuration
# ----------------------------

MOISTURE_THRESHOLD = 30          # Soil moisture threshold (percent)
WATERING_DURATION = 45           # Seconds pump stays on
WATERING_COOLDOWN = 15 * 60      # Cooldown after watering (15 minutes)
ALLOWED_WATERING_START = 6       # Earliest allowed watering hour (6 AM)
ALLOWED_WATERING_END = 18        # Latest allowed watering hour (6 PM)

USE_MANUAL_INPUT = True          # True = user enters soil moisture; False = simulate randomly

# ----------------------------
# Simulated states
# ----------------------------

manual_override = False          # If True, user controls the pump manually
rain_forecast = False            # Simulate rain forecast manually or randomly

# ----------------------------
# Functions
# ----------------------------

def read_soil_moisture():
    """
    Get soil moisture either from user input or simulated value.
    """
    if USE_MANUAL_INPUT:
        while True:
            try:
                moisture = int(input("Enter current soil moisture (%): "))
                if 0 <= moisture <= 100:
                    return moisture
                else:
                    print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")
    else:
        return random.randint(10, 50)

def is_raining():
    """
    Simulate rain condition or use forecast flag.
    """
    return rain_forecast or random.choice([True, False, False])

def current_hour():
    """
    Get the current hour (24-hour format).
    """
    return time.localtime().tm_hour

def turn_pump_on(duration):
    """
    Simulate turning the water pump on and off.
    """
    print(f"💧 Pump ON for {duration} seconds...")
    time.sleep(1)  # Simulate pump running (shortened for demo)
    print("🛑 Pump OFF")

def record_event(event):
    """
    Log a watering-related event.
    """
    print(f"📘 Event recorded: {event}")

# ----------------------------
# Main Logic
# ----------------------------

def main_loop():
    print("🌿 Starting Watering System Simulation...")
    while True:
        moisture = read_soil_moisture()
        print(f"📊 Soil moisture: {moisture}%")

        if manual_override:
            print("⚠️ Manual override active: pump control by user")
            record_event("Manual pump operation")
            time.sleep(10)
            continue

        hour = current_hour()

        if moisture < MOISTURE_THRESHOLD:
            if ALLOWED_WATERING_START <= hour < ALLOWED_WATERING_END:
                if is_raining():
                    print("🌧️ Rain detected or forecasted — skipping watering")
                    record_event("Skipped watering due to rain")
                else:
                    turn_pump_on(WATERING_DURATION)
                    record_event("Watered plants")
                    time.sleep(WATERING_COOLDOWN)
            else:
                print("⏰ Outside allowed watering hours, waiting...")
                time.sleep(600)  # Wait 10 minutes
        else:
            print("✅ Soil moisture sufficient, no watering needed.")
            time.sleep(600)  # Wait 10 minutes

# ----------------------------
# Run the program
# ----------------------------

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\n🛑 Simulation stopped by user.")

