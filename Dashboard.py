import requests
from bs4 import BeautifulSoup

import nfl_data_py as nfl

# Fetch data for a specific player
pbp = nfl.import_pbp_data([1990: 2022])
