import os
import requests 
from datetime import date

# get image url in jason format
# idx parameter determines where to start from: 0 is the current day
response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
image_data = response.json()

# Form the URL for the image
image_url = image_data["images"][0]["url"].split("&")[0]
full_url = "https://www.bing.com" + image_url

# get HOME path
home_path = os.path.expanduser("~")

# save_dir is used to set the location where Bing pics of the day are stored.
save_dir = home_path + "/Pictures/.bing-images/"

# create save directory if it does not already exist
os.makedirs(save_dir, exist_ok=True)

# image name: current date
image_name = str(date.today())+".jpg"

# download and save image
res_full_url = requests.get(full_url)

with open(save_dir + image_name, 'wb') as f:
    f.write(res_full_url.content)

# command to set wallpaper
os.system("gsettings set org.gnome.desktop.background picture-uri file://" + save_dir+image_name)