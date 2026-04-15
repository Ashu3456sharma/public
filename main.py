import pandas as pd
import os

# 📁 Folder path
folder_path = "dataset"

# 📄 All files
all_files = os.listdir(folder_path)

print("Files found:", all_files)

df_list = []

# 🔁 Read files
for file in all_files:
    if (file.endswith(".xls") or file.endswith(".xlsx") or file.endswith(".ods")) and not file.startswith("._"):
        
        file_path = os.path.join(folder_path, file)
        print(f"Reading: {file}")
        
        try:
            df = pd.read_excel(file_path)
            df_list.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")

# ❗ Check if data mila ya nahi
if len(df_list) == 0:
    print("No Excel files found!")
else:
    # 🔗 Merge all data
    final_df = pd.concat(df_list, ignore_index=True)

    print("\nAll files merged successfully!")
    print("Total Rows:", final_df.shape[0])
    print("Total Columns:", final_df.shape[1])

    print("\nPreview:")
    print(final_df.head())

    # 🧹 DATA CLEANING (FIXED)
    
    # ❌ Remove unwanted unnamed columns
    final_df = final_df.loc[:, ~final_df.columns.str.contains('^Unnamed')]

    # ✅ Keep only required columns
    final_df = final_df[['MDDS STC', 'STATE NAME', 'MDDS DTC', 'DISTRICT NAME',
                        'MDDS Sub_DT', 'SUB-DISTRICT NAME', 'MDDS PLCN', 'Area Name']]

    # ❌ Remove duplicates only
    final_df = final_df.drop_duplicates()

    print("\nData cleaned!")
    print("Rows after cleaning:", final_df.shape[0])

    # 🧩 CREATE TABLES (FIXED)

    # 🟢 State Table
    state_df = final_df[['MDDS STC', 'STATE NAME']].drop_duplicates()

    # 🟡 District Table
    district_df = final_df[['MDDS DTC', 'DISTRICT NAME', 'MDDS STC']].drop_duplicates()

    # 🔵 SubDistrict Table
    subdistrict_df = final_df[['MDDS Sub_DT', 'SUB-DISTRICT NAME', 'MDDS DTC']].drop_duplicates()

    # 🔴 Village Table
    village_df = final_df[['MDDS PLCN', 'Area Name', 'MDDS Sub_DT']].drop_duplicates()

    print("\nTables created successfully!")

    # 💾 Save to CSV
    state_df.to_csv("states.csv", index=False)
    district_df.to_csv("districts.csv", index=False)
    subdistrict_df.to_csv("subdistricts.csv", index=False)
    village_df.to_csv("villages.csv", index=False)

    print("\nAll tables saved as CSV files!")