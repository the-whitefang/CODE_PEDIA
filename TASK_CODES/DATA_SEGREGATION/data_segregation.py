import pandas as pd

file_path = '/home/abhilash.venugopal/PYTHON/TASK_CODES/DATA_SEGREGATION/text comparison.xlsx'
excel_data = pd.read_excel(file_path, sheet_name=['parent', 'child'])

parent_df = excel_data['parent']
child_df = excel_data['child']

parent_df.duplicated().sum()

parent_df.drop_duplicates(inplace=True)

child_df.duplicated().sum()

child_df.drop_duplicates(inplace=True)

parent_values = excel_data['parent'].iloc[:, 0].tolist()
print(parent_values)

child_values = excel_data['child'].iloc[:, 0].tolist()
print(child_values)

matched = [x if x in child_values else None for x in parent_values]
print(matched)

unmatched = [x if x not in child_values else None for x in parent_values]
print(unmatched)

resultant_matched_df = pd.DataFrame({'Matched_Values': matched})

resultant_unmatched_df = pd.DataFrame({'Unmatched_Values': unmatched})

resultant_matched_df.to_excel('segregated_matched_data.xlsx', index= False)
resultant_unmatched_df.to_excel('segregated_unmatched_data.xlsx', index=False)