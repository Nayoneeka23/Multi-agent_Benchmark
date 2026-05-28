import pandas as pd
import matplotlib.pyplot as plt

# 1. Put your exact CSV file name here
csv_file = '/home/jovyan/multi_agent_benchmark/benchmarks/results/benchmark_advanced_20260521_211803.csv'

print(f"Reading data from: {csv_file}")

# 2. Load the data
df = pd.read_csv(csv_file)

# 3. Calculate the average time (rtt_ms) for each network condition
avg_times = df.groupby('network_condition')['rtt_ms'].mean().reset_index()

# 4. Draw the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(avg_times['network_condition'], avg_times['rtt_ms'], color=['#4CAF50', '#FF9800', '#F44336'])

# 5. Add titles and labels
plt.title('Impact of Network Constraints on Coordinator Pattern', fontsize=14)
plt.xlabel('Network Condition', fontsize=12)
plt.ylabel('Average RTT (ms)', fontsize=12)

# 6. Put the numbers on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + (yval * 0.05), f'{int(yval)} ms', ha='center', va='bottom')

# 7. Save the picture
output_path = '/home/jovyan/multi_agent_benchmark/benchmarks/results/coordinator_base_chart.png'
plt.tight_layout()
plt.savefig(output_path)

print(f"Done! Chart saved to {output_path}")