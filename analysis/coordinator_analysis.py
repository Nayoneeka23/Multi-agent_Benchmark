import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Read your specific Coordinator data file
csv_path = '/home/jovyan/multi_agent_benchmark/benchmarks/results/benchmark_advanced_20260521_211803.csv'
df = pd.read_csv(csv_path)

# 2. Use the whole dataframe
coord_data = df.copy()

# 3. Create a Box Plot grouped by network condition
plt.figure(figsize=(10, 6))

# Set whis=1.5 for the standard academic anomaly detection
coord_data.boxplot(column='rtt_ms', by='network_condition', 
                   grid=True, patch_artist=True, whis=1.5,
                   boxprops=dict(facecolor='#E3F2FD', color='#1565C0', linewidth=1.5),
                   medianprops=dict(color='#F44336', linewidth=2),
                   flierprops=dict(marker='X', markerfacecolor='#F44336', markersize=8, markeredgecolor='#F44336'))

# 4. Clean up the titles and labels
plt.title('Coordinator Pattern: Standard Anomaly Detection (IQR = 1.5)', fontsize=14)
plt.suptitle('') 
plt.xlabel('Network Condition', fontsize=12)
plt.ylabel('Round Trip Time (ms)', fontsize=12)

# 5. Save the chart
output_dir = '/home/jovyan/multi_agent_benchmark/analysis'
os.makedirs(output_dir, exist_ok=True)

output_path = f'{output_dir}/coordinator_boxplot_standard.png'
plt.tight_layout()
plt.savefig(output_path)

print(f"\nSuccess! Standard box plot saved to: {output_path}")