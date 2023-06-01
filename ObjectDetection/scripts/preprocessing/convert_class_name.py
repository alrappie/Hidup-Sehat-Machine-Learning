import os
import glob
import pandas as pd
import io
import xml.etree.ElementTree as ET
import argparse

path = "D:/Pemrograman/Python/Project/google_image_scraper/Google-Image-Scraper/photos/new_dataset/ayam/test"
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
        if nama_class == 'ayam-goreng-tanpa-tepung':
            member.find('name').text = 'Ayam'
            
        if nama_class == 'ayam-kentucky':
            member.find('name').text = 'Ayam'
            
        if nama_class == 'nasi putih':
            member.find('name').text = 'Nasi Putih'
            
        if nama_class == 'tempe goreng':
            member.find('name').text = 'Tempe Goreng'
            
        if nama_class == 'tahu goreng':
            member.find('name').text = 'Tahu Goreng'
            
        if nama_class == 'Timun':
            member.find('name').text = 'Mentimun'
            
        if nama_class == 'tahu goreng':
            member.find('name').text = 'Tahu Goreng'
            
    tree.write(file_names)