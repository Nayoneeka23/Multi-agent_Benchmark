import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Read the combined results file
csv_path = '/home/jovyan/multi_agent_benchmark/benchmarks/results/benchmark_results.csv'
df = pd.read_csv(csv_path)

# 2. Filter only negotiation results
neg_df = df[df['pattern'] == 'negotiation']

# 3. Calculate average total time per network condition
avg_times = neg_df.groupby('network_condition')['total_time_ms'].mean().reset_index()

# 4. Create the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(avg_times['network_condition'], avg_times['total_time_ms'],
               color=['#4CAF50', '#FF9800', '#F44336'])

# 5. Add titles and labels
plt.title('Impact of Network Constraints on Multi-Agent Negotiation (Mistral x3)', fontsize=14)
plt.xlabel('Network Condition', fontsize=12)
plt.ylabel('Average Total Negotiation Time (ms)', fontsize=12)

# 6. Add the exact numbers on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100,
             f'{round(yval)} ms', ha='center', va='bottom', fontsize=10)

# 7. Save the chart
output_path = '/home/jovyan/multi_agent_benchmark/benchmarks/results/negotiation_base_chart.png'
plt.tight_layout()
plt.savefig(output_path)
print(f"Success! Chart saved to: {output_path}")