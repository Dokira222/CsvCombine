import pandas as pd
import glob
import os

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))

    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    csv_files = [f for f in csv_files if os.path.basename(f) != 'compy.csv']

    if not csv_files:
        return

    all_data = pd.DataFrame()

    for file in csv_files:
        df = pd.read_csv(file)
        df['檔名'] = os.path.basename(file)
        all_data = pd.concat([all_data, df], ignore_index = True)

    output_path = os.path.join(folder_path, 'compy.csv')
    all_data.to_csv(output_path, index=False, encoding='utf-8-sig')
if __name__ == '__main__':
    main()
    input("\n按Enter關閉視窗...")
