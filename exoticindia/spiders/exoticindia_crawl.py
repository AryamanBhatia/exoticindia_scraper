from pathlib import Path
#to be resolved: multiple names, only first page covered, be sure to collect correct xpath using cmd + f
#books, it is taking things like audiobook and facebook also, hidden stuff like childrens books
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "exoticindia_crawler"

    def start_requests(self):
        urls = [
            'https://www.exoticindiaart.com/find?q=*&exactsearch=-1&materialsearch=&sizesearch=&colorsearch=&languagesearch=',
            #'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = f'quotes-{page}.html'
        #Path(filename).write_bytes(response.body)
        #self.log(f'Saved file {filename}')
    def parse(self, response):
        # Gives the product name
        product_name = response.css('div.product-textarea-title.is-size-6.has-text-weight-medium.ellipsis.is-ellipsis-2 a::text').getall()
        # Gives the price
        prices = response.css('span.product-textarea-finalprice::text').getall()
        prices_without_sign = []
        for i in prices:
            i = i.replace('$', '')
            prices_without_sign.append(i)
        for i in range(len(product_name)):
            yield {
                'name': product_name[i],
                'price': prices_without_sign[i]
            }

