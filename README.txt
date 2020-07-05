THIS WILL NOT WORK BY DEFAULT
You have to
1. Install Requests module for Python
2. Install DigiUSB drivers, links can be found here https://digistump.com/wiki/digispark/tutorials/digiusb
3. Locate the send utility in the DigiUSB folder. It should be in DigisparkExamplePrograms/Python/DigiUSB/windows/send.exe. The executable source file written in Python2 should be around there somewhere
4. Insert the path to the utility in GarkoAirly.py
5. Register on Airly website, get an API key and insert it in GarkoAirly.py
6. Figure out where you are, convert your coordinates to floats and insert them in GarkoAirly.py. You are now done with the Python part.

7. I assume you already have ArduinoIDE and Digispark board data installed. You need to locate the DigiUSB library. On windows, it should be in AppData/Local/ArduinoXX/packages/digistump/hardware/avr/versionNumber/libraries/DigisparkUSB.
8. In there, you find DigiUSB.h file and change RING_BUFFER_SIZE to 64. It's 128 by default. If you don't change it, the sketch will compile, but won't work correctly.

9. Now you're ready. Compile and upload GarkoAirly.ino via ArduinoIDE, and fire up the Python script. If everything is done right, the eyes should display the same color as the Airly website or app for the same location.
Feel free to modify and expand on the idea!