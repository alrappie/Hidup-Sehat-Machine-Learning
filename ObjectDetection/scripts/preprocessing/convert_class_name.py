import os
import glob
import pandas as pd
import io
import xml.etree.ElementTree as ET
import argparse

path = "D:/Pemrograman/Python/Project/google_image_scraper/Google-Image-Scraper/datasets/new_dataset/xml_lama_test"

saved_dir = "D:/Pemrograman/Python/Project/google_image_scraper/Google-Image-Scraper/datasets/new_dataset/xml_baru"
os.chdir(saved_dir)

for xml_file in glob.glob(path + '/*.xml'):
    file_names = xml_file.split('\\')[1]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('filename').text
    for member in root.findall('object'):
        # print(member)
        nama_class = member.find('name').text
        if nama_class == 'n07614500':
            member.find('name').text = 'Es Krim'
            
        if nama_class == 'n07615774':
            member.find('name').text = 'Es Loli'
            
        if nama_class == 'n07693725':
            member.find('name').text = 'Roti Bagel'
            
        if nama_class == 'n07695742':
            member.find('name').text = 'Pretzel Cinnamon Sugar'
            
        if nama_class == 'n07697313':
            member.find('name').text = 'Cheeseburger'
            
        if nama_class == 'n07697537':
            member.find('name').text = 'Hotdog'
            
        if nama_class == 'n07711569':
            member.find('name').text = 'Kentang Tumbuk'
            
        if nama_class == 'n07714571':
            member.find('name').text = 'Kubis'
            
        if nama_class == 'n07714990':
            member.find('name').text = 'Brokoli'
            
        if nama_class == 'n07715103':
            member.find('name').text = 'Kembang Kol'
            
        if nama_class == 'n07720875':
            member.find('name').text = 'Paprika Merah'
            
        if nama_class == 'n07745940':
            member.find('name').text = 'Stroberi'
            
        if nama_class == 'n07747607':
            member.find('name').text = 'Jeruk'
            
        if nama_class == 'n07749582':
            member.find('name').text = 'Lemon'
            
        if nama_class == 'n07753275':
            member.find('name').text = 'Nanas'
            
        if nama_class == 'n07753592':
            member.find('name').text = 'Pisang'
            
        if nama_class == 'n07754684':
            member.find('name').text = 'Nangka'
            
        if nama_class == 'n07831146':
            member.find('name').text = 'Spaghetti Carbonara'
            
        if nama_class == 'n07873807':
            member.find('name').text = 'Pizza dengan Daging dan Sayuran'
            
        if nama_class == 'n12144580':
            member.find('name').text = 'Jagung'
    tree.write(file_names)