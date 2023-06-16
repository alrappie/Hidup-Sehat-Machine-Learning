# Scraping nutriet foods from fatsecret and feeds content from halodoc

1. For foods nutrient is in scraped_halodoc_artikel.ipynb (File)

2. For feeds content halodoc is in scraped_informasi_makanan.ipynb

## How to run the scraping using beautifulSoup

1. get the url website that u want to scraped
2. create an instance response and parse the html data
```python
response = requests.get(URL)

# Parse the HTML data and create a BeautifulSoup object.
soup = BeautifulSoup(response.content, 'html.parser')
```
3. do a looping for the information that you needed in website
```python
# Example
makanan_umum = soup.find_all("div", class_="next-link")
index = -1

for i in makanan_umum:
    print('BAB '+i.find('a').get('href'))
    clicked_url_1 = i.find('a').get('href')
    response = requests.get(basic_url+str(clicked_url_1))
    soup = BeautifulSoup(response.content, 'html.parser')
    each_makanan = soup.find_all("div", class_="next-link")[:-18]
    for makanan in each_makanan:
        print('Makanan ',index,makanan.find('a').get('href'))
        clicked_url_2 = makanan.find('a').get('href')
        response = requests.get(basic_url+str(clicked_url_2))
        soup = BeautifulSoup(response.content, 'html.parser')
        
        porsi_makanan = soup.find_all('div',"other-link")[::2]
        for porsi in porsi_makanan:
            index +=1
            print('Porsi ',porsi.find('a').get('href'))
            clicked_url_3 = porsi.find('a').get('href')
            response = requests.get(basic_url+str(clicked_url_3))
            soup = BeautifulSoup(response.content, 'html.parser')
            tes_title = soup.find('div',attrs={'class':['padding page-title']})
            tes_right = soup.find_all('div',attrs={'class':['serving_size black serving_size_value','nutrient right tRight', 'nutrient black right tRight', 'nutrient black right tRight',]})
            tes_left = soup.find_all('div',attrs={'class':["serving_size black serving_size_label",'nutrient black left','nutrient sub left','nutrient left',]})
            dataframe.loc[index,'Nama'] = re.sub(r'\n','',tes_title.get_text())
            for k,v,in zip(tes_left,tes_right):
                dataframe.loc[index,k.get_text()] = v.get_text()
```
5. after that save the information to csv using pandas library
```python
# Example
dataframe.to_csv('database_makanan_5k.csv',index=False)
```
