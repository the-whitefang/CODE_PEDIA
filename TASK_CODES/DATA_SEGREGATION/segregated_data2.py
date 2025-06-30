import pandas as pd

file_path = 'sample_data.xlsx'
excel_data = pd.read_excel(file_path, sheet_name=['parent', 'child'])

parent_df = excel_data['parent']
child_df = excel_data['child']

print(parent_df.duplicated().sum())

print(child_df.duplicated().sum())
print()

parent_values =excel_data['parent'].iloc[:, 0].tolist()
print(parent_values)

child_values =excel_data['child'].iloc[:, 0].tolist()
print(child_values)

matched = [x if x in child_values else None for x in parent_values]

unmatched = [x if x not in child_values else None for x in parent_values]

resultant_matched_df = pd.DataFrame({'Matched_Values': matched})

resultant_unmatched_df = pd.DataFrame({'Unmatched_Values': unmatched})

resultant_matched_df.to_excel('segregated_matched_parahs.xlsx', index= False)
resultant_unmatched_df.to_excel('segregated_unmatched_parahs.xlsx', index= False)