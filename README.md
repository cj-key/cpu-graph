# cpu_graph
A desktop app that shows a pie chart of your CPU usage.
# ReadMe for CPU Usage App

## Table of Contents
1. [Introduction](#introduction)
2. [Tech Stack](#tech-stack)
3. [Setup](#setup)
4. [How to Use](#how-to-use)
5. [Features](#features)
6. [License](#license)
7. [Contact](#contact)

## Introduction
The CPU Usage App is a lightweight desktop application that provides users with a visual representation of the top five processes consuming CPU resources on their system. The app creates a pie chart to display the CPU usage of these processes, allowing users to monitor their system's performance easily.

## Tech Stack
- Python (including libraries such as ctypes, os, wmi, matplotlib.pyplot, tkinter)
- Tkinter (for GUI)
- Matplotlib (for chart visualization)

## Setup
1. Make sure you have Python 3.x installed on your system.
2. Clone or download the repository containing the code files.
3. Navigate to the directory where the code files are located.
4. Run the Python script `cpu_usage_app.py` to launch the application.

   Example:
   ```sh
   $ cd /path/to/directory
   $ python cpu_usage_app.py
## How to Use
1. Launch the CPU Usage App by running the Python script.
2. A graphical user interface (GUI) window will appear.
3. Click the "Display Chart" button to generate a pie chart displaying the top five processes by CPU usage.
4. The pie chart will be shown within the GUI window.
5. You can interact with the chart by hovering over the slices to view process names and CPU usage percentages.

## Features
- Displays the top five processes by CPU usage on a pie chart.
- Provides real-time visualization of CPU usage.
- Sorts processes in descending order based on CPU usage.
- Excludes the "_Total" and "Idle" processes from the chart.
- Resizes the chart to ensure proper label spacing.
- Adjusts label formatting to avoid overlapping.
- Hides the console window automatically after launching the GUI.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
For any inquiries or feedback, please contact the project maintainer:
[C.J. Key](https://www.linkedin.com/in/cj-key-8a386915a/)
