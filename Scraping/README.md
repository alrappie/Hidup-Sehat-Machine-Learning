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
4. after that save the information to csv using pandas library
