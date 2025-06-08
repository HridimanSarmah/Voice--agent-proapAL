import pandas as pd
from datetime import datetime

def log_metrics(metrics):
    df = pd.DataFrame([metrics])
    file_name = 'call_metrics.xlsx'
    try:
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, index=False, sheet_name='SessionLogs', startrow=writer.sheets['SessionLogs'].max_row)
    except FileNotFoundError:
        df.to_excel(file_name, index=False, sheet_name='SessionLogs')
