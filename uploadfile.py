# -*- coding: utf-8 -*-
import dropbox

directory = raw_input('Directory: ')
file_name= raw_input('Filename: ')
file = directory + file_name
access_token = 'MY_ACCESS_TOKEN'

dropbox_path='/'
dbx=dropbox.Dropbox(access_token)
with open(file, 'rb') as f:
    dbx.files_upload(f.read(),dropbox_path+file_name,mute=True) # The change from f to f.read() was made to comply with the late-2016 change in the API.
 
dbx.files_download_to_file('Copy of '+file_name,dropbox_path+file_name)
