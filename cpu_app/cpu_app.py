import ctypes
import os
import wmi
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def display_cpu_chart():
    # Connect to WMI
    c = wmi.WMI()

    # Get CPU usage data for each process
    process_data = {}
    for process in c.Win32_PerfFormattedData_PerfProc_Process():
        try:
            name = process.Name
            cpu_usage = int(process.PercentProcessorTime)
            if name != "_Total" and name != "Idle":
                process_data[name] = cpu_usage
        except (AttributeError, ValueError):
            # Handle cases where process information is not available or invalid
            pass

    # Sort the process data by CPU usage (descending order)
    sorted_processes = sorted(process_data.items(), key=lambda x: x[1], reverse=True)

    # Get the top five processes
    top_five_processes = sorted_processes[:5]

    # Extract process names and CPU usages
    labels = [process[0] for process in top_five_processes]
    sizes = [process[1] for process in top_five_processes]

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(8, 6))  # Adjust figure size for better label spacing
    _, _, autopcts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # Adjust label formatting to avoid overlapping
    for autopct in autopcts:
        autopct.set_horizontalalignment('center')
        autopct.set_verticalalignment('center')
        autopct.set_rotation(90)

    # Move the legend (color key) to the right side of the GUI
    ax.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))

    # Set the title for the pie chart
    ax.set_title('Top Five Processes by CPU Usage')

    # Convert the pie chart to a Tkinter-compatible object
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

def hide_console_window():
    # Hide the console window
    console_window = ctypes.windll.kernel32.GetConsoleWindow()
    if console_window != 0:
        ctypes.windll.user32.ShowWindow(console_window, 0)
        ctypes.windll.kernel32.CloseHandle(console_window)

# Create the GUI window
window = Tk()
window.title('CPU Usage App')

# Set the size of the window
window.geometry("800x600")

# Add a label
label = Label(window, text='Click the button to display CPU usage')
label.pack()

# Add a button to trigger the CPU chart display
button = Button(window, text='Display Chart', command=display_cpu_chart)
button.pack()

# Hide the console window after a delay
window.after(0, hide_console_window)

# Start the GUI event loop
window.mainloop()
