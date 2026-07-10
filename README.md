# Car Monitoring System

## Description

Car Monitoring System is a Python application designed to monitor vehicle parameters in real time.

In its current version, the application uses simulated data for vehicle speed and engine RPM. In future versions, the system will be connected to an OBD-II ELM327 adapter to read real-time data directly from the vehicle's ECU.

## Functionalities

- Vehicle speed simulation
- Engine RPM simulation
- Speed limit detection
- High RPM detection
- Automatic data logging
- Modular architecture

## Project Structure

- `main.py` – application entry point
- `simulator.py` – generates simulated vehicle data
- `analyzer.py` – analyzes vehicle parameters and detects alerts
- `logger.py` – stores data in log files
- `log.txt` – recorded telemetry data

## Technologies Used

- Python
- File Handling
- Data Logging
- Modular Programming

## Future Improvements

- OBD-II ELM327 integration
- Real-time vehicle data acquisition
- Driving behavior analysis
- Driver score calculation
- Data visualization with graphs
- Web dashboard
- Anomaly detection system

## Author

Otniel Kovacs

Computer Science Student  
Politehnica University of Timișoara