import os
import requests
import time
import pandas as pd
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from http.client import responses as http_responses

# Define the base URL for SEC EDGAR
BASE_URL = 'https://www.sec.gov'

# Create a requests session
session = requests.Session()

# Define a retry strategy to handle request rate limiting
retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504]
)

# Filter methods for retry based on your whitelist
def method_filter(request):
    return request.method in ["HEAD", "GET", "OPTIONS"]

retry_strategy._method_whitelist = method_filter

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount('https://', adapter)
session.mount('http://', adapter)

# Define the headers including the custom User-Agent
headers = {
    'User-Agent': 'MyCustomApp/1.0 (Macintosh; Intel Mac OS X 10_15_7) Python/3.9 requests/2.31.0',
    'Naresh': 'nc623367@wne.edu',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.sec.gov'
}

# Function to make a throttled request
def throttled_request(url):
    response = session.get(url, headers=headers)
    time.sleep(0.1)  # Sleep 100ms to ensure compliance with the rate limit
    return response

# Function to download and save the file
def download_file(url, filepath):
    response = throttled_request(url)
    if response.status_code == requests.codes.ok:
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {filepath}")
        return True
    else:
        print(f"Failed to download file: {response.status_code} - {http_responses.get(response.status_code, 'Unknown')}")
        return False

# Function to download data for each year and quarter
def download_data_for_year_quarters(year, quarters):
    data = []
    for quarter in quarters:
        # Construct the URL for the file based on the year and quarter
        file_url = f'{BASE_URL}/{year}/{quarter}/sample.pdf'  # Adjust the URL and file extension as needed
        # Specify the directory where you want to save the file
        download_directory = 'downloads'
        # Ensure the download directory exists
        os.makedirs(download_directory, exist_ok=True)
        # Construct the file path
        filename = f'{year}_{quarter}.pdf'
        filepath = os.path.join(download_directory, filename)
        # Download the file
        if download_file(file_url, filepath):
            data.append({'Year': year, 'Quarter': quarter, 'Filepath': filepath})
    return data
