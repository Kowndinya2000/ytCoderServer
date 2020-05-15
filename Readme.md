## A python NodeJS application (YT CODER):
## To run the application on local machine(localhost:5000):
```
npm run dev
```
### To deploy the app to heroku :

Add the following to your `buildpack commands`:
``` 
heroku buildpacks:add heroku-community/apt
heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-python.git
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-nodejs.git
heroku run bash
find -iname tessdata
```
Paste the path from above command: 
```
heroku config:set TESSDATA_PREFIX= <add the path here>
```
#### `Aptfile` Contains: 
All the necessary sudo apt install commands for the heroku app
#### `requirements.txt` Contains:
All the necessary pip installation commands for the heroku app
### For local usage:
#### pip installs
```
python -m pip install --upgrade pip
sudo pip install imageio
sudo pip install pafy
sudo pip install numpy
sudo pip install opencv-python
sudo pip install pytesseract
sudo pip install pillow
sudo pip install nltk
sudo pip install youtube_dl
sudo pip install --trusted-host pypi.python.org moviepy
sudo apt update
sudo apt upgrade
sudo apt install snapd
sudo apt update
sudo apt upgrade
sudo snap install ffmpeg
sudo pip install opencv-contrib-python
```
#### pip3 installs
```
python3 -m pip install --upgrade pip
sudo pip3 install imageio
sudo pip3 install pafy
sudo pip3 install numpy
sudo pip3 install opencv-python
sudo pip3 install pytesseract
sudo pip3 install pillow
sudo pip3 install nltk
sudo pip3 install youtube_dl
sudo pip3 install --trusted-host pypi.python.org moviepy
sudo apt update
sudo apt upgrade
sudo apt install snapd
sudo apt update
sudo apt upgrade
sudo snap install ffmpeg
sudo pip3 install opencv-contrib-python
```
### References: 
https://note.nkmk.me/en/python-package-version/
https://medium.com/@pro_science108/configurin-tesseract-ocr-in-heroku-16-444a4c079c41