import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel("Smart_Traffic_Data.xlsx")

# Convert Time column to datetime
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')

# 1. Line Graph: Average Waiting Time vs Time of Day
avg_waiting = df.groupby('Time')['Avg_Waiting_Time (sec)'].mean()

plt.figure()
plt.plot(avg_waiting.index, avg_waiting.values, marker='o')
plt.xlabel("Time of Day")
plt.ylabel("Average Waiting Time (seconds)")
plt.title("Average Waiting Time vs Time of Day")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Figure1_Avg_Waiting_Time.png")
plt.show()


# 2. Bar Chart: Throughput per Intersection
# (Using total vehicle count as throughput)
throughput = df.groupby('Intersection_ID')['Vehicle_Count'].sum()

plt.figure()
plt.bar(throughput.index, throughput.values)
plt.xlabel("Intersection ID")
plt.ylabel("Total Vehicles Passed")
plt.title("Throughput Comparison per Intersection")
plt.tight_layout()
plt.savefig("Figure2_Throughput.png")
plt.show()

# 3. Queue Length Plot: Peak Hours (07:00–08:00)
peak_data = df[df['Time'].dt.hour.isin([7, 8])]

queue_length = peak_data.groupby('Time')['Queue_Length (vehicles)'].mean()

plt.figure()
plt.plot(queue_length.index, queue_length.values, marker='o')
plt.xlabel("Time (Peak Hours)")
plt.ylabel("Average Queue Length (vehicles)")
plt.title("Queue Length Variation During Peak Hours")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Figure3_Queue_Length.png")
plt.show()

# 4. System Diagram: Sensor–Controller–Signal Model
plt.figure(figsize=(8, 4))

plt.text(0.1, 0.5, "Sensors\n• Vehicle Count\n• Queue Length",
         fontsize=10, ha='center', va='center')

plt.text(0.5, 0.5, "Traffic Controller\n(Decision Logic)",
         fontsize=10, ha='center', va='center')

plt.text(0.9, 0.5, "Traffic Lights\n(Red / Yellow / Green)",
         fontsize=10, ha='center', va='center')

plt.arrow(0.18, 0.5, 0.22, 0, head_width=0.03, length_includes_head=True)
plt.arrow(0.62, 0.5, 0.22, 0, head_width=0.03, length_includes_head=True)

plt.axis('off')
plt.title("Smart Traffic Light Control System Architecture")
plt.tight_layout()
plt.savefig("Figure4_System_Diagram.png")
plt.show()
