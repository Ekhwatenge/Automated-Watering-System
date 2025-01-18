# Automated-Watering-System

To program this on your Raspberry Pi:
1. Connect to your Raspberry Pi via SSH or use the desktop interface.
Open a text editor (e.g., Nano or Thonny) and create a new file:
(nano automated_watering.py)
2. Copy and paste the code in (automated_watering.py) into the file.
3. Save the file and exit the editor.
4. Run the program using Python: (python3 automated_watering.py)
This code assumes you're using a Raspberry Pi with a soil moisture sensor connected to an MCP3008 analog-to-digital converter and a water pump connected to GPIO pin 17. You may need to adjust the pin numbers and thresholds based on your specific setup1413.
5. Make sure you have the necessary libraries installed (RPi.GPIO and gpiozero) before running the code. You can install them using pip: (pip3 install RPi.GPIO gpiozero)
Remember to connect your hardware correctly and ensure your Raspberry Pi has internet access if you plan to expand the system with weather API integration in the future
