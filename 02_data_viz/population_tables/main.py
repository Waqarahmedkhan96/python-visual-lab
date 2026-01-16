import pandas as pd

data = {
    'City': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City'],
    'Population (Millions)': [37.4, 31.1, 27.7, 22.2, 21.9],
    'Country': ['Japan', 'India', 'China', 'Brazil', 'Mexico']
}

df = pd.DataFrame(data)
print("\n--- World City Populations ---")
print(df.to_string(index=False))

# Optional: Save to CSV
# df.to_csv("population.csv")
