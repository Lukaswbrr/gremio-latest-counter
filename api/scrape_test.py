# api/scrape.py
from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json

class handler(BaseHTTPRequestHandler):
    def get_gremio_data(self, headers=None):
        html = ""

        try:
            html = requests.get("https://www.fotmob.com/en/teams/9769/overview/gremio", headers=headers)
            html.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error Occured: {err}")
            return

        soup = BeautifulSoup(html.text, "lxml")

        json_data_element = soup.find("script", id="__NEXT_DATA__")
        json_data = json.loads(json_data_element.text)

        return json_data
    
    def get_latest_matches(self):
        # gets recent matches
        recent_matches = self.get_gremio_data()["props"]["pageProps"]["fallback"]["team-9769"]["overview"]["teamForm"]
        
        return recent_matches

    def do_GET(self):
        # 1. Logic: Fetch the target URL
        url = "https://example.com"

        ua = UserAgent()

        # # Add headers to mimic a browser (helps avoid some basic blocks)
        headers = {'User-Agent': ua.random}
        response = requests.get(url, headers=headers)

        # # 2. Logic: Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        page_title = soup.title.string if soup.title else "No title found"

        # 3. Response: Send data back to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = {"title": page_title}
        self.wfile.write(json.dumps(data).encode())

# def format_match_results(recent_matches):
#     for k in recent_matches:
#         match k["resultString"]:
#             case "W":
#                 print(f"venceu! ({k['tooltipText']['homeTeam']} {k['tooltipText']['homeScore']} x {k['tooltipText']['awayScore']} {k['tooltipText']['awayTeam']})")
#             case "L":
#                 print(f"perdeu! ({k['tooltipText']['homeTeam']} {k['tooltipText']['homeScore']} x {k['tooltipText']['awayScore']} {k['tooltipText']['awayTeam']})")
        