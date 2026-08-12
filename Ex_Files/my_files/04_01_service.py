# $ python3 -m pip install requests
import requests 

response = requests.get("http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
  display_width = year["value"] // 10_000_000 # calculate the width of the display based on the population value
  print(f'{year["date"]}: {year["value"]}', "=" * display_width)

  # Note:
  # The use of the f-string to format the output, and the use of the "=" character to create a visual representation of the population value.
  # The width of the display is calculated by dividing the population value by 10 million, which gives a rough estimate of the number of "=" characters to display.
