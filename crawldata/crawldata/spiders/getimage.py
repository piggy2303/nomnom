import scrapy


class QuotesSpider(scrapy.Spider):
    name = "getimage"

    def start_requests(self):
        urls = [
            "http://www.dulichsontra.com/chua-linh-ung"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = []
        for image in response.xpath('//img/@src').extract():
            # make each one into a full URL and add to item[]
            item.append(image)

        yield item
