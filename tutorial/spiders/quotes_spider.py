import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

            # next_page = response.css('li.next a').extract_first()
            if a in response.css('li.next a'):
                # next_page = response.urljoin(next_page)
                yield response.follow(a, callback=self.parse)