# BrewPi Dropbox

Basic python upload script taken from [Liudr's Dropbox Python API](https://liudr.wordpress.com/2016/02/20/dropbox-python-api/)

dailyupload.py will running daily in the early morning and send yesterday's temperature log json files to dropbox
upload.py is copied onto the raspberry pi to be executable from ssh in case I need to specify a file to upload
