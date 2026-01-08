# api/scrape.py
from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import requests
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Logic: Fetch the target URL
        url = "https://example.com"
        # Add headers to mimic a browser (helps avoid some basic blocks)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        # 2. Logic: Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        page_title = soup.title.string if soup.title else "No title found"

        # 3. Response: Send data back to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = {"title": page_title}
        self.wfile.write(json.dumps(data).encode())