import scrapy

from quotes.items import Quote

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def __init__(self):
        self.tag = "inspirational"

    def start_requests(self):
        base_url = "http://quotes.toscrape.com/tag/"
        urls = [
            base_url + self.tag,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quotes_selectors = response.css("div.quote")

        for selector in quotes_selectors:
            quote = Quote()

            quote["text"] = selector.css("span.text::text").extract_first()
            quote["author"] = selector.css("span>small.author::text").extract_first()

            yield quote