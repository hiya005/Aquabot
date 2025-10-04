 Aquabot
📋 Description

This is a Python-based simulation of an automated plant watering system.
It monitors soil moisture, simulates rain detection, and controls a virtual water pump based on defined rules.

It includes:

Soil moisture threshold logic

Rain forecast/rain check simulation

Time window for allowed watering

Manual override for pump control

Option to simulate moisture or enter it manually

🚀 Features

💧 Automated pump control based on moisture level

🌧️ Rain detection and forecast simulation

🕒 Allowed watering time window (default: 6 AM – 6 PM)

👨‍🌾 Manual override mode

🧪 User-selectable manual input or random simulation of soil moisture

📘 Event logging for every watering action or skip

⚙️ Configuration

Inside the script, you can change key settings:

MOISTURE_THRESHOLD = 30          # Moisture % below which watering occurs
WATERING_DURATION = 45           # Pump ON time in seconds
WATERING_COOLDOWN = 15 * 60      # Cooldown period after watering
ALLOWED_WATERING_START = 6       # 6 AM
ALLOWED_WATERING_END = 18        # 6 PM
USE_MANUAL_INPUT = True          # If True, asks user for soil moisture input

🧪 How to Run

Make sure Python is installed (python3 --version)

Run the script:

python watering_simulator.py


If USE_MANUAL_INPUT = True, you'll be prompted to enter soil moisture percentage.

Press Ctrl + C to stop the simulation anytime.

🛠 Requirements

Python 3.x
(No external libraries needed — uses only built-in modules like random and time)

📝 Example Output
🌿 Starting Watering System Simulation...
📊 Soil moisture: 25%
💧 Pump ON for 45 seconds...
🛑 Pump OFF
📘 Event recorded: Watered plants

🔧 Future Improvements (Optional Ideas)

Integrate with real sensors (e.g., using Raspberry Pi)

Web dashboard or GUI interface

Save logs to a file

Control via smartphone or IoT platform
