import requests
import ezodf
from datetime import datetime

# ----- cofig part -----
api_key = 'd706ad079c66b2972d21137dca2be197'
city = 'Pune'
country = 'India'
ods_file = 'weather_data.ods'

# ----- data fetching part -----
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()

# ----- parsing the needed values
temp = data['main']['temp']
weather = data['weather'][0]['main']
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# ----- load and open existing ods file -----
ezodf.config.set_table_expand_strategy('all')
doc = ezodf.opendoc(ods_file)
sheet = doc.sheets[0]

# ----- function to find the next empty row -----
def find_next_empty_row(sheet):
    for row_index in range(sheet.nrows()):
        if all(cell.value is None for cell in sheet.row(row_index)):
            return row_index
        return sheet.nrows()

next_row = find_next_empty_row(sheet)

# -----Expand sheet if needed
min_required_rows = next_row + 1
min_required_cols = 4

while sheet.nrows() < min_required_rows:
    sheet.append_rows(1)

while sheet.ncols() < min_required_cols:
    sheet.append_columns(1)

# ----- entering the new data into the next row -----
sheet[next_row, 0].set_value(city)
sheet[next_row, 1].set_value(temp)
sheet[next_row, 2].set_value(weather)
sheet[next_row, 3].set_value(date)

# ----- saving the updated ods file -----
doc.save()
print("Weather data has been entered successfully! ")