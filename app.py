from scrapy import Request
import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "bukukita"
    main_url = "https://www.bukukita.com/katalogbuku.php?page="
    start_urls = [main_url + str(999)]

    def parse(self, response):
        max_page = response.css("ul.pagination a::text").getall()[-1]
        for i in range(1, int(max_page) + 1):
            yield Request(self.main_url + str(i), callback=self.next_parse)

    def next_parse(self, response):
        catalog = response.css("div.product-grid a::attr(href)")
        for link in catalog:
            link = response.urljoin(link.get())
            yield Request(link, callback=self.parse_detail)

    def parse_detail(self, response):
        rows = response.css("div.row")
        book = {
            "Source": response.url,
            "Harga": response.css("span.price-box__new::text").get(),
            "Deskripsi": response.css("div.col-sm-12 p::text").get(),
        }
        for row in rows:
            cols = row.css("div[class*=col]")
            if len(cols) == 2:
                key = cols[0].css("::text").get()
                key = re.sub("\s+", " ", key).strip()
                value = cols[1].css("::text").get()
                value = re.sub("\s+", " ", value).strip()
                if key == "Text Bahasa":
                    value = " ".join(re.findall("\w+", value))
                if key != "":
                    book.update({key: value})

        yield book
