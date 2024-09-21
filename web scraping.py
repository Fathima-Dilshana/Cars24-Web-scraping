Original file is located at
    https://colab.research.google.com/drive/1QwzOUJmqwT8qGY9gcHaXNayI20yFBC8q

# **WEBSCRAPING CODE**
"""

!pip install bs4

"""# Chennai"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=2135718455.1725707831&listingSource=TabFilter&storeCityId=5732"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('chennai.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('chennai.csv', index=False)

print("Data has been successfully saved to 'chennai.xlsx' and 'chennai.csv'.")

"""# Surat"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=2135718455.1725707831&listingSource=TabFilter&storeCityId=1605"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('surat.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('surat.csv', index=False)

print("Data has been successfully saved to 'surat.xlsx' and 'surat.csv'.")

"""# Kolkata"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=2135718455.1725707831&storeCityId=777"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('kolkata.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('kolkata.csv', index=False)

print("Data has been successfully saved to 'kolkata.xlsx' and 'kolkata.csv'.")

"""# Patna"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=2135718455.1725707831&storeCityId=8184"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('patna.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('patna.csv', index=False)

print("Data has been successfully saved to 'patna.xlsx' and 'patna.csv'.")

"""# Coimbatore"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=1301600899.1725538448&storeCityId=6105"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('Coimbatore.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('Coimbatore.csv', index=False)

print("Data has been successfully saved to 'Coimbatore.xlsx' and 'Coimbatore.csv'.")

"""# Kochi"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=1301600899.1725538448&storeCityId=6356"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('Kochi.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('Kochi.csv', index=False)

print("Data has been successfully saved to 'Kochi.xlsx' and 'Kochi.csv'.")

"""# Ahamedabad"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=1301600899.1725538448&storeCityId=1692"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('Ahamedabad.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('Ahamedabad.csv', index=False)

print("Data has been successfully saved to 'Ahamedabad.xlsx' and 'Ahamedabad.csv'.")

"""# Hyderabad"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=1301600899.1725538448&storeCityId=3686"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('Hyderabad.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('Hyderabad.csv', index=False)

print("Data has been successfully saved to 'Hyderabad.xlsx' and 'Hyderabad.csv'.")

"""# Indore"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=1301600899.1725538448&storeCityId=2920"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('Indore.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('Indore.csv', index=False)

print("Data has been successfully saved to 'Indore.xlsx' and 'Indore.csv'.")

"""# Agra"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=1301600899.1725538448&storeCityId=136"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('Agra.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('Agra.csv', index=False)

print("Data has been successfully saved to 'Agra.xlsx' and 'Agra.csv'.")

"""# New Delhi"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Step 1: Fetch the webpage content
url = "https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Arenault%3AOR%3Amake%3A%3D%3Ajeep&sort=bestmatch&serveWarrantyCount=true&gaId=2135718455.1725707831&listingSource=TabFilter&storeCityId=2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all car entries
car_entries = soup.find_all('div', class_='_7jb8Q _1Ey60')

# Step 4: Loop through each car entry and extract details
cars_data = []

for car in car_entries:
    # Extract car title and model
    car_title = car.find('h3', class_='_2Out2').contents[0].strip() if car.find('h3', class_='_2Out2') else None
    car_model = car.find('h3', class_='_2Out2').find('span').text.strip() if car.find('h3', class_='_2Out2').find('span') else None

    # Extract the year from the car title
    year = car_title.split()[0] if car_title else None
    car_title = ' '.join(car_title.split()[1:]) if car_title else None  # Remove the year from the title

    # Extract mileage, fuel type, and ownership using more flexible methods
    details_list = car.find('ul', class_='_3jRcd').find_all('li') if car.find('ul', class_='_3jRcd') else []

    # Use regular expression to find mileage
    mileage = None
    if details_list:
        for detail in details_list:
            if re.search(r'\d+[,.\d]*\s*km', detail.text, re.IGNORECASE):
                mileage = detail.text.strip()
                break

    if mileage and not mileage.lower().endswith('km'):
        mileage += " km"

    # Extract fuel type using keyword search
    fuel_type = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "petrol" in text:
            fuel_type = "Petrol"
            break
        elif "diesel" in text:
            fuel_type = "Diesel"
            break

    # Extract ownership using keyword search
    ownership = None
    for detail in details_list:
        text = detail.text.strip().lower()
        if "1st owner" in text:
            ownership = "1st Owner"
            break
        elif "2nd owner" in text:
            ownership = "2nd Owner"
            break

    # Extract EMI information and remove "EMI from" text
    emi_info = car.find('div', class_='_1Oul-').find('span', class_='_1t1AA').text.strip() if car.find('div', class_='_1Oul-') else None
    if emi_info:
        emi_info = emi_info.replace('EMI from', '').strip()

    # Extract price details
    price_div = car.find('div', class_='_1Oul- VMjdr')
    current_price = price_div.find('strong', class_='_37WXy').text.strip() if price_div and price_div.find('strong', class_='_37WXy') else None
    original_price = price_div.find('span', class_='_3hb01').text.strip() if price_div and price_div.find('span', class_='_3hb01') else None

    # Extract location details only and remove "at"
    location_info = car.find('p', class_='_2rxhF').find('span').text.strip() if car.find('p', class_='_2rxhF') and car.find('p', class_='_2rxhF').find('span') else None
    if location_info:
        location_info = location_info.replace('at', '').strip()

    # Store extracted details in a dictionary
    car_details = {
        'Year': year,
        'Car Title': car_title,
        'Car Model': car_model,
        'Mileage': mileage,
        'Fuel Type': fuel_type,
        'Ownership': ownership,
        'EMI Info': emi_info,
        'Current Price': current_price,
        'Original Price': original_price,
        'Location': location_info
    }

    cars_data.append(car_details)

# Step 5: Create a DataFrame using pandas
df = pd.DataFrame(cars_data)

# Step 6: Save the DataFrame to an Excel file
df.to_excel('New Delhi.xlsx', index=False)

# Step 7: Save the DataFrame to a CSV file
df.to_csv('New Delhi.csv', index=False)

print("Data has been successfully saved to 'New Delhi.xlsx' and 'New Delhi.csv'.")

"""# Combine All Location Details into Single File"""

import pandas as pd

# Read the Excel files into separate DataFrames
df_ahamedabad = pd.read_excel('/content/Ahamedabad.xlsx')
df_hyderabad = pd.read_excel('/content/Hyderabad.xlsx')
df_indore = pd.read_excel('/content/Indore.xlsx')
df_agra = pd.read_excel('/content/Agra.xlsx')
df_Coimbatore = pd.read_excel('/content/Coimbatore.xlsx')
df_Kochi = pd.read_excel('/content/Kochi.xlsx')
df_chennai = pd.read_excel('/content/chennai.xlsx')
df_kolkata = pd.read_excel('/content/kolkata.xlsx')
df_patna = pd.read_excel('/content/patna.xlsx')
df_surat = pd.read_excel('/content/surat.xlsx')
df_NewDelhi = pd.read_excel('/content/New Delhi.xlsx')

# Concatenate the DataFrames
combined_df = pd.concat([df_ahamedabad, df_hyderabad, df_indore, df_agra,df_Coimbatore,df_Kochi,df_chennai,df_kolkata,df_patna,df_surat,df_NewDelhi], ignore_index=True)

# Save the combined DataFrame to a new Excel file
combined_df.to_csv('cars24_data.csv', index=False)

print("Combined data saved to 'cars24_data.csv'")

"""# **DATA CLEANING**"""

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/content/cars24_data.csv')

# Forward fill the 'Ownership' and 'Original Price' columns
df[['Ownership', 'Original Price']] = df[['Ownership', 'Original Price']].fillna(method='ffill')

# Save the updated DataFrame back to the CSV file
df.to_csv('cars.csv', index=False)

print("Forward fill and special character removal completed and saved to 'cars.csv'.")

"""# **EDA**"""

import pandas as pd
import re

df=pd.read_csv('/content/cars.csv')
df.head().T

df.isna().sum()

df['Fuel Type'].value_counts()

df[df['Fuel Type'].isna()]

df.fillna('Petrol',inplace=True)

df.isna().sum()

df.info()

df_cate=df.select_dtypes(exclude=['int64',"float64"])
df_cate

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for i in df_cate.columns:
     df[i]=le.fit_transform(df_cate[i])
     print(i)
df

from sklearn.preprocessing import LabelEncoder

# Initialize a dictionary to store LabelEncoders for each column
label_encoders = {}

# Apply Label Encoding to each categorical column
for column in df_cate.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df_cate[column])  # Encode the column

    # Save the LabelEncoder object for later use
    label_encoders[column] = le

    # Print the mapping for each column
    print(f"Mappings for column '{column}':")
    for index, class_label in enumerate(le.classes_):
        print(f"{class_label} -> {index}")
    print("\n")

df.corr()

"""# **MODEL BUILDING FOR PREDICTIVE ANALYSIS**"""

!pip install lazypredict

from lazypredict.Supervised import LazyRegressor

from lazypredict.Supervised import LazyRegressor

X = df.drop({'Current Price','Location'}, axis=1)
y = df['Current Price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

reg = LazyRegressor(verbose=0, ignore_warnings=False, custom_metric=None)
models, predictions = reg.fit(X_train, X_test, y_train, y_test)

print(models)

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

X = df.drop({'Current Price','Location'}, axis=1)
y = df['Current Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = XGBRegressor()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

y_pred = model.predict([[2018,12,44,171,0,1,2.92,3.3]])
y_pred

"""## **DATA VISUALIZATION**

# Correlation
"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(df.corr(),annot=True)

"""# Univariate"""

df['Car Title'].value_counts().plot(kind='bar')
plt.xlabel('Car Title')
plt.ylabel('Highest Selling')
plt.show()

"""# Price Distribution"""

sns.histplot(df['Current Price'],kde=True)

df['Current Price'].mean(),df['Current Price'].median()

"""# Fuel"""

import plotly.express as px

px.bar(df['Fuel Type'].value_counts())

"""# Bivariate Analysis

Vehicle Listing for different number of previous owners
"""

sns.barplot(x=df['Ownership'],y=df['Current Price'],errorbar=None)

"""Vehicle listing from different locations"""

from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Assuming 'df' is the DataFrame with the encoded "Location" column
# Assuming 'label_encoders' is the dictionary with all LabelEncoders created earlier

# Retrieve the LabelEncoder for the "Location" column
location_le = label_encoders['Location']

# Create a mapping from encoded values to original names
location_mapping = dict(enumerate(location_le.classes_))

# Replace encoded "Location" values with their original names in a new column for plotting
df['Location Name'] = df['Location'].map(location_mapping)

# Plotting using the original "Location" names
df.groupby(['Location Name'])['Year'].count().sort_values(ascending=False).plot(kind='bar', figsize=(10, 6))
plt.ylabel('Number of Vehicles', fontsize=12)
plt.xlabel('Location', fontsize=12)
plt.title('Vehicle Listing from Different Locations')
plt.show()

"""Comparing year and price"""

sns.lineplot(x=df['Year'],y=df['Current Price'],errorbar=None)

"""How will fuel type impact resale price"""

sns.boxplot(x=df['Fuel Type'],y=df['Current Price'])

"""# Multivariate Analysis"""

sns.barplot(x=df['Year'],y=df['Current Price'],errorbar=None,hue=df['Ownership'])

"""# **WEBSCRAPING WITH TRANSMISSION TYPE DATA**

We faced a lot of data loss while trying to scrap the transmission type data, Thus I am uploading the code used for that at last.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#  path to your chromedriver executable
service = Service('C:\webdrivers\chromedriver.exe')

# Creating a webdriver instance with the correct service
driver = webdriver.Chrome(service=service)

# Opening a website to verify that it works
driver.get('https://www.google.com')
print(driver.title)

"""# Surat"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# Seting up Selenium WebDriver
service = Service('C:\\webdrivers\\chromedriver.exe')  # ChromeDriver path
driver = webdriver.Chrome(service=service)

# main page
main_url = 'https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amahindra%3AOR%3Amake%3A%3D%3Ajeep%3AOR%3Amake%3A%3D%3Arenault&sort=bestmatch&serveWarrantyCount=true&gaId=2135718455.1725707831&listingSource=TabFilter&storeCityId=1605'
driver.get(main_url)
time.sleep(5)

# Extracting car detail URLs from the main page
car_elements = driver.find_elements(By.CLASS_NAME, '_1_1Uy')
car_urls = [car_element.get_attribute('href') for car_element in car_elements]
car_details = []

# Iterate through each car URL and extract the required information
for car_url in car_urls:
    driver.get(car_url)
    time.sleep(5)  # Wait for the page to load fully

    # Use BeautifulSoup to parse the page content
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract details from the page
    try:
        title = soup.find('h1', class_='_2Ximl').text.strip()
        year_make_model = title.split(' ', 1)  # Extract year, make, and model from the title
        km_driven = soup.find('ul', class_='_2JSmz').find_all('li')[0].text.strip()
        ownership = soup.find('ul', class_='_2JSmz').find_all('li')[1].text.strip()
        fuel_type = soup.find('ul', class_='_2JSmz').find_all('li')[2].text.strip()
        transmission_type = soup.find('ul', class_='_2JSmz').find_all('li')[3].text.strip()
        location = soup.find('li', class_='_1Rvdw').find('strong').text.strip()
        prices = soup.find_all('strong', class_='_3i9_p')

        # Extract prices that contain "Lakh" only
        current_price = next((price.text.strip() for price in prices if "Lakh" in price.text), None)
        original_price_tag = soup.find('span', class_='F6S7B _3RIaW')
        original_price = original_price_tag.text.strip() if original_price_tag and "Lakh" in original_price_tag.text else None

        # Only append the details if both prices are available
        if current_price and original_price:
            car_details.append({
                'Year': year_make_model[0],
                'Make': year_make_model[1].split(' ', 1)[0],
                'Model': year_make_model[1].split(' ', 1)[1],
                'Kilometers Driven': km_driven,
                'Ownership': ownership,
                'Fuel Type': fuel_type,
                'Transmission Type': transmission_type,
                'Location': location,
                'Original Price': original_price,
                'Current Price': current_price
            })
    except Exception as e:
        print(f"Error extracting data from {car_url}: {e}")

# Close the WebDriver
driver.quit()

# Write the extracted car details to a CSV file
with open('details_surat.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Year', 'Make', 'Model', 'Kilometers Driven', 'Ownership', 'Fuel Type', 'Transmission Type', 'Location', 'Original Price', 'Current Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write each car detail to the CSV file
    for car in car_details:
        writer.writerow(car)

print("Car details saved to car_details_surat.csv")

"""# Here after, we are doing this for the remaining locations and then combining everything in a single dataset"""

import pandas as pd

# Define the file names
filenames = ['details_agra.csv', 'details_Ahamedabad.csv', 'details_chennai.csv', 'details_covai.csv', 'details_Hyderabad.csv', 'details_indore.csv', 'details_kochi.csv', 'details_kolcata.csv', 'details_patna.csv', 'details_surat.csv']

dataframes = []

for filename in filenames:
    # Read the CSV file into a dataframe
    df = pd.read_csv(filename)
    # Append the dataframe to the list
    dataframes.append(df)

# Concatenate all the dataframes into a single dataframe
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('upated_cars24_file.csv', index=False)

print("CSV files combined into combined_file.csv")

from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Assuming 'df' is the DataFrame with the encoded "Location" column
# Assuming 'label_encoders' is the dictionary with all LabelEncoders created earlier

# Retrieve the LabelEncoder for the "Location" column
title_le = label_encoders['Car Title']

# Create a mapping from encoded values to original names
title_mapping = dict(enumerate(title_le.classes_))

# Replace encoded "Location" values with their original names in a new column for plotting
df['Car title Name'] = df['Car Title'].map(title_mapping)

# Plotting using the original "Location" names
df.groupby(['Car title Name'])['Year'].count().sort_values(ascending=False).plot(kind='bar', figsize=(10, 6))
plt.ylabel('Number of Vehicles', fontsize=12)
plt.xlabel('Car Title', fontsize=12)
plt.title('Vehicle Listing from Different Car Title')
plt.show()

from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Assuming 'df' is the DataFrame with the encoded "Location" column
# Assuming 'label_encoders' is the dictionary with all LabelEncoders created earlier

# Retrieve the LabelEncoder for the "Location" column
location_le = label_encoders['Location']

# Create a mapping from encoded values to original names
location_mapping = dict(enumerate(location_le.classes_))

# Replace encoded "Location" values with their original names in a new column for plotting
df['Location Name'] = df['Location'].map(location_mapping)

# Plotting using the original "Location" names
df.groupby(['Location Name'])['Year'].count().sort_values(ascending=False).plot(kind='bar', figsize=(10, 6))
plt.ylabel('Number of Vehicles', fontsize=12)
plt.xlabel('Location', fontsize=12)
plt.title('Vehicle Listing from Different Locations')
plt.show()
