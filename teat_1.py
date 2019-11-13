import os
from hashlib import md5
import requests
from urllib.parse import urlencode

headers = {
    'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

url = "https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis"


response = requests.get(url, headers=headers)

print(response.json())