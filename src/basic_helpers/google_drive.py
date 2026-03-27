from __future__ import annotations
import requests    # type: ignore
from bs4 import BeautifulSoup
from pathlib import Path

def download_file_from_google_drive(file_id: str, destination: str | Path) -> None:
    URL = "https://drive.google.com/uc?export=download&id=" + file_id
    session = requests.Session()
    response = session.get(URL, stream=True)

    # Check if the response contains a virus scan warning
    if "Google Drive - Virus scan warning" in response.text:
        # Parse the HTML to find the confirm token and uuid
        soup = BeautifulSoup(response.text, 'html.parser')
        confirm_raw = soup.find('input', {'name': 'confirm'})
        assert confirm_raw is not None
        confirm = confirm_raw['value']

        uuid_raw = soup.find('input', {'name': 'uuid'})
        assert uuid_raw is not None
        uuid = uuid_raw['value']

        # Prepare the parameters for the download request
        params = {
            'id': file_id,
            'confirm': confirm,
            'uuid': uuid
        }
        
        URL2 = "https://drive.usercontent.google.com/download"
        response = session.get(URL2, params=params, stream=True)

    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size=32768):
            if chunk:
                f.write(chunk)

    return None

