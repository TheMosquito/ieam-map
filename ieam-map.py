from flask import Flask
from flask import send_file
from flask import request
import requests

WEB_SERVER_BIND_ADDRESS = '0.0.0.0'
WEB_SERVER_PORT = 80

HTML_FILE = 'site.html'
CSS_FILE = 'site.css'
FAVICON_ICO = 'favicon.ico'
LOGO_PNG = 'logo.png'
GPS_COORDINATES = ''

# We need to find the WAN IP address of this server
GET_IP_ADDRESS_URL='https://api.ipify.org?format=json'

# curl 'https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=8.8.8.8'
IP_LOCATION_API_URL='https://api.ipgeolocation.io/ipgeo'
IP_LOCATION_API_KEY='<<< Get your API key at ipgeolocation.io >>>'

webapp = Flask('hello')
webapp.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@webapp.route("/site.css")
def get_css():
  return send_file(CSS_FILE)

@webapp.route("/favicon.ico")
def get_favicon_ico():
  return send_file(FAVICON_ICO)

@webapp.route("/logo.png")
def get_logo_png():
  return send_file(LOGO_PNG)

@webapp.route("/")
def get_page():
  out = site_html
  return out.replace('GPS_COORDINATES', str(GPS_COORDINATES), 1)

# Prevent caching everywhere
@webapp.after_request
def add_header(r):
  r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
  r.headers["Pragma"] = "no-cache"
  r.headers["Expires"] = "0"
  r.headers['Cache-Control'] = 'public, max-age=0'
  return r

# Get the WAN IP address first...
query = { "format": "json" }
response = requests.get(GET_IP_ADDRESS_URL, params=query)
j = response.json()
addr = j['ip']
#print(addr)

# Use this WAN I{P address to get the approximate location of this server
query = { "apiKey": IP_LOCATION_API_KEY, "ip" : addr }
response = requests.get(IP_LOCATION_API_URL, params=query)
j = response.json()
lat = j['latitude']
lon = j['longitude']
GPS_COORDINATES = ('%s,%s' % (lat, lon))
#print(GPS_COORDINATES)

# Read the site HTML template
with open(HTML_FILE) as f:
  site_html= ' '.join(f.readlines())
webapp.run(host=WEB_SERVER_BIND_ADDRESS, port=WEB_SERVER_PORT)

