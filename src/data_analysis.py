import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURATION ---
# We are strictly looking for 'skoda.csv'
file_name = 'skoda.csv'
file_path = os.path.join('data', 'raw', file_name)

print(f"Searching for file at: {file_path} ...")

# 1. LOAD DATA
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("✅ Success: 'skoda.csv' loaded!")
else:
    print(f"❌ ERROR: Could not find '{file_name}'.")
    print(f"Please check if '{file_name}' exists inside the 'data/raw' folder.")
    exit()

# 2. DATA INSPECTION
print("\n--- Dataset Info ---")
print(f"Total Cars: {len(df)}")
print(df.head())

# 3. FEATURE ENGINEERING (200k Check)
# Standard datasets usually use 'mileage' or 'km_driven'. We check for both.
mileage_col = 'mileage' if 'mileage' in df.columns else 'km_driven'
price_col = 'price' if 'price' in df.columns else 'selling_price'

if mileage_col in df.columns:
    # Create the column checking if mileage > 200,000
    df['is_high_mileage'] = df[mileage_col] > 200000
    
    # Count how many cars are above 200k
    count_high = df['is_high_mileage'].sum()
    print(f"\n--- Mileage Analysis ---")
    print(f"Column used: '{mileage_col}'")
    print(f"Cars with > 200,000 km: {count_high}")
else:
    print("⚠️ Warning: Could not find a mileage column (mileage/km_driven).")

# 4. VISUALIZATION
# Plot: Year vs Price (colored by Transmission)
plt.figure(figsize=(10, 6))

if 'year' in df.columns and price_col in df.columns:
    # Check if 'transmission' exists for coloring, otherwise just plot blue dots
    hue_col = 'transmission' if 'transmission' in df.columns else None
    
    sns.scatterplot(
        x='year', 
        y=price_col, 
        data=df, 
        hue=hue_col, 
        alpha=0.6
    )
    plt.title('Skoda Market: Year vs Price')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.grid(True)
    
    # Save the chart
    plot_name = 'skoda_price_analysis.png'
    plt.savefig(plot_name)
    print(f"\n✅ Chart saved as '{plot_name}'.")
else:
    print("❌ Could not create chart. Missing year or price columns.")

# 5. SIMPLE STATS
if 'fuelType' in df.columns and price_col in df.columns:
    print("\n--- Average Price by Fuel Type ---")
    print(df.groupby('fuelType')[price_col].mean().round(2))

print("\nAnalysis Script Finished.")
