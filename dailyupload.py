# -*- coding: utf-8 -*-
import dropbox
import datetime

#today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days = 1)
beer_name = 'Citra%20Ale%20V2'
directory = '/home/brewpi/data/'

file_name = beer_name + '-' + str(yesterday) + '.json'
file_path = directory + beer_name + '/' + beer_name + '-' + str(yesterday) + '.json'
access_token = 'MY_ACCESS_TOKEN'

dropbox_path='/'
dbx=dropbox.Dropbox(access_token)
with open(file_path, 'rb') as f:
    dbx.files_upload(f.read(),dropbox_path+file_name,mute=True) # The change from f to f.read() was made to comply with the late-2016 change in the API.
 
dbx.files_download_to_file('Copy of '+file_name,dropbox_path+file_name)
