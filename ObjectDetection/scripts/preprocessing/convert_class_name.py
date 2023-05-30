import os
import glob
import pandas as pd
import io
import xml.etree.ElementTree as ET
import argparse

path = "D:/Pemrograman/Python/Project/google_image_scraper/Google-Image-Scraper/photos/food/train"
saved_dir = "D:/Pemrograman/Python/Project/google_image_scraper/Google-Image-Scraper/photos/new_dataset/xml_baru"
os.chdir(saved_dir)

for xml_file in glob.glob(path + '/*.xml'):
    file_names = xml_file.split('\\')[1]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('filename').text
    for member in root.findall('object'):
        # print(member)
        nama_class = member.find('name').text
        if nama_class == 'Telur Dadar -93 kal per 100gr-':
            member.find('name').text = 'telor dadar'
        if nama_class == 'Nasi -129 kal per 100gr-':
            member.find('name').text = 'nasi'
        if nama_class == 'Tempe -225 kal per 100 gr-':
            member.find('name').text = 'tempe'
        if nama_class == 'Tahu -80 kal per 100 gr-':
            member.find('name').text = 'tahu'
        if nama_class == 'Ayam Goreng -260 kal per 100 gr-':
            member.find('name').text = 'ayam'
    tree.write(file_names)