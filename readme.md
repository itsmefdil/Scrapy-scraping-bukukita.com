## Scrapy Scraping Bukukita.com

### Description

This is a simple scraping project using Scrapy to scrape data from Bukukita.com. The data scraped are book title, author, publisher, price, and book category. The data will be saved in a csv file.

### How to Run

1. Clone this repository

2. Install Scrapy

```
pip install scrapy
```

3. Run the spider

```
scrapy runspider app.py -o data_bukukita.csv
```

4. The data will be saved in a csv file named `bukukita.csv`
