from datetime import date
import json
import os

import requests

# $saveDir is used to set the location where Bing pics of the day are stored.
save_dir="/home/eli/Pictures/.bing-images/"

# get image url
response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
image_data = json.loads(response.text)

image_url = image_data["images"][0]["url"].split("&")[0]
full_image_url = "https://www.bing.com" + image_url

# image's name: current date
image_name = str(date.today())+".jpg"

# download and save image
response_full_url = requests.get(full_image_url)
with open(save_dir+image_name, 'wb') as f:
    f.write(response_full_url.content)

# command to set wallpaper
os.system("gsettings set org.gnome.desktop.background picture-uri file://"+save_dir+image_name)