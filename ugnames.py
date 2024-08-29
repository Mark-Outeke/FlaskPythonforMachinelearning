import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "https://surnam.es/uganda"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()

# Parse the webpage content
soup = BeautifulSoup(response.content, "html.parser")

# Extract surnames
surnames = [item.text for item in soup.select("li a")]

# Create a DataFrame
df = pd.DataFrame(surnames, columns=["Surname"])

# Save to Excel file
df.to_excel("uganda_surnames.xlsx", index=False)

print("Excel file generated successfully.")
