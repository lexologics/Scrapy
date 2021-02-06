import scrapy


class MitraSpider(scrapy.Spider):
    name = "whiskey"
    allowed_domains = ['mitra.nl']
    start_urls = ['https://www.mitra.nl/webshop/groep/whisky/99-48-6C-B7-61-C4-31-A6']

    #custom_settings={ 'FEED_URI': "mitra_%(time)s.json",
    #                  'FEED_FORMAT': 'json'}

    def parse(self, response):
        #print('processing: ' + response.url)
        product_name = response.xpath('//span[@class="product-name"]/a/h2/text()').getall()
        product_name_content = response.xpath('//span[@class="product-name"]/a/h3/text()').getall()
        product_price_euro = response.xpath('//span[@class="vrkpr"]/text()').getall()  #.replace('.', '')
        product_price_cents = response.xpath('//span[@class="cents"]/text()').getall()
        product_available = response.xpath('//div[@class="product-buttons"]/a/text()').getall()
        #page_link = response.xpath().getall()
        #current_page = response.xpath('//li[@class="page-item"]/a/text()').getall()
        #next_page = response.xpath('//li[@class="page-item"]/a/text()').getall()


        row_data = zip(
            product_name,
            product_name_content,
            product_price_euro,
            product_price_cents,
            product_available,
            #next_page
        )

        for item in row_data:
            scrapped_info = {
                #'page:': response.url,
                'product_name': item[0],
                'product_name_content': item[1],
                'product_price_euro': item[2],
                'product_price_cents': item[3],
                'product_available': item[4],
                #'next_page': next_page[5],
            }

            yield scrapped_info

# current_page = response.xpath('//li[@class="page-item"]/a/text()').get()
# next_page = response.xpath('//li[@class="page-item"]/a/text()').get()

        
'''
    def start_requests(self):
        urls = [
            'https://www.mitra.nl/webshop/groep/whisky/99-48-6C-B7-61-C4-31-A6',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'mitra-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

'''