#!/usr/bin/python
import os
import subprocess

dir_path='.'

for root, dirs, files in os.walk(dir_path):
    for file in files:

        if file == 'Thumbs.db':	
            continue
        if file == 'convert':
            continue

        tmp=file.split('.')
        tt=tmp[:(len(tmp)-1)]
        res_name='.'.join(tt);

        file = file.replace("(", "\(")
        file = file.replace(")", "\)")
        file = file.replace(" ", "\ ")

        #file = file.encode('string-escape')

        print 'Start.............' + file
        bc = 'ffmpeg -i ' + str(file) + ' -vcodec copy -acodec libmp3lame -ar 44100 -ac 2 -ab 192k convert/'+ str(file)
        print 'Process.............' + bc

        subprocess.call(bc,shell=True)

