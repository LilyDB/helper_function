import pandas as pd

# customized example
def write_to_excel(dataframes, dir, name,table):
    with pd.ExcelWriter(f'{dir}/{name}.xlsx', engine='xlsxwriter') as writer:
        workbook = writer.book
        worksheet = workbook.add_worksheet('Result')
        worksheet.write(0,0,'Data quality control report')
        worksheet.write(1,0,'Time stamp:')
        worksheet.write(1,1,datetime.datetime.now().strftime("%d-%b-%Y"))
        worksheet.write(2,0,'Number of data points')
        worksheet.write(2,1,str(table.shape))
        writer.sheets['Result'] = worksheet

        COLUMN = 0
        row = 4

        for df in dataframes:
            worksheet.write_string(row, COLUMN,df.name)
            row += 1
            df.to_excel(writer, sheet_name='Result',
                        startrow=row, startcol=COLUMN)
            row += df.shape[0] + 5
