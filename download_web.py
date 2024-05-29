import requests

def download_file():
    # User inputs for URL and local file path
    url = input("Enter the URL of the file to download: ")
    local_filename = input("Enter the local path where you want to save the file: ")
    
    # Send a GET request to the URL
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # Raises an HTTPError for bad responses
        # Open local file in binary write mode
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

    print("Download completed!")

# Call the download function
download_file()
