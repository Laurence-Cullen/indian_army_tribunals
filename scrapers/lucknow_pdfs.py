import random
import time
from pathlib import Path

import pandas as pd
import requests


# def configure_proxies() -> requests.Session:
#
#     # IP address: 2.56.119.93
#     # port: 5074
#     # Username: ccsxnebc
#     # Password: w8uapzu6f72z
#
#     # Construct URL for proxy server from data above
#
#
#     proxy_servers = {
#         'http': '197.234.13.10:4145',
#         'https': '197.234.13.10:4145',
#     }
#
#     s = requests.Session()
#     s.proxies = proxy_servers
#
#     return s


def scrape_pdfs(region: str):
    # session = configure_proxies()

    region_data = pd.read_csv(f'structured_judgements/{region}.csv')

    # Iterate over the DataFrame and download the judgement PDF from each
    # row's 'pdf_url' column
    for index, row in region_data.iterrows():
        url = row['pdf_url']
        filename = f"judgement_pdfs/{region}/{url.split('/')[-1]}.pdf"

        # Check if the PDF already exists
        if Path(filename).exists():
            print('Skipping {} as it already exists'.format(filename))
            continue

        # Download the PDF
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

        # Wait for a random time between 0 and 0.2 seconds
        time.sleep(random.random() * 0.2)

        # Print progress
        print('Downloaded {} of {} judgements'.format(index + 1, len(region_data)))


def main():
    scrape_pdfs('lucknow')


if __name__ == '__main__':
    main()
