import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Convert date columns to actual days for calculation if not already in days
df['Arrived at hospital'] = pd.to_numeric(df['Arrived at hospital'])
df['Left hospital'] = pd.to_numeric(df['Left hospital'])
df['CTDNA positivity (# days after surgery)'] = pd.to_numeric(df['CTDNA positivity (# days after surgery)'], errors='coerce')
df["Patient's head fell off (# days after surgery)"] = pd.to_numeric(df["Patient's head fell off (# days after surgery)"], errors='coerce')
df["Patient's head reattached"] = pd.to_numeric(df["Patient's head reattached"], errors='coerce')

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Loop over each patient to create a line for their timeline
for i, row in df.iterrows():
    patient = row['Patient name']
    start = row['Arrived at hospital']
    end = row['Left hospital']
    
    # Plot the main line for the hospital stay
    ax.plot([start, end], [i, i], color='skyblue', lw=2, label='Hospital Stay' if i == 0 else "")
    
    # Plot events as individual markers on the line
    if not pd.isna(row['CTDNA positivity (# days after surgery)']):
        ax.plot(row['CTDNA positivity (# days after surgery)'], i, 'o', color='purple', label='CTDNA Positive' if i == 0 else "")
    if not pd.isna(row["Patient's head fell off (# days after surgery)"]):
        ax.plot(row["Patient's head fell off (# days after surgery)"], i, 'x', color='red', label="Head Fell Off" if i == 0 else "")
    if not pd.isna(row["Patient's head reattached"]):
        ax.plot(row["Patient's head reattached"], i, '^', color='green', label='Head Reattached' if i == 0 else "")

# Set labels
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Patient name'])
ax.set_xlabel('Days')
ax.set_title('Patient Timeline in Hospital')

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()
