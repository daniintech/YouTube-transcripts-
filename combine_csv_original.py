import os
import pandas as pd

#combines all csv-files from folder_path into one, with a new name
#the new csv file is stored in the same path
#folder_path & name_for_new_csv need to be specified 
folder_path = ''
name_for_new_csv = ''

all_files = os.listdir(folder_path)

csv_files = [f for f in all_files if f.endswith('.csv')]

df_list = []

for csv in csv_files:
    file_path = os.path.join(folder_path, csv)

    try:
        # Try reading the file using default UTF-8 encoding
            df = pd.read_csv(file_path)
            df_list.append(df)
    except UnicodeDecodeError:
        try:
            # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
                df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
                df_list.append(df)
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")
    except Exception as e:
        print(f"Could not read file {csv} because of error: {e}")

# Concatenate all data into one DataFrame
big_df = pd.concat(df_list, ignore_index=True)

# Save the final result to a new CSV file
big_df.to_csv(os.path.join(folder_path, name_for_new_csv + '.csv'), index=False)
