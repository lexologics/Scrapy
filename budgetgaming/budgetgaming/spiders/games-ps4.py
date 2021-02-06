import scrapy


class GamePS4Spider(scrapy.Spider):
    name = "gamesps4"
    allowed_domains = ['budgetgaming.nl']
    start_urls = []

    for i in range(1,77):
        start_urls.append(f'https://www.budgetgaming.nl/gamesonly/{i}/console-ps4.html')

    custom_settings={ 'FEED_URI': "gamesps4_%(time)s.csv",
                      'FEED_FORMAT': 'csv'}

    def parse(self, response):
        game_name = response.xpath('//tbody/tr/td[1]/a/text()').getall()
        game_price = response.xpath('//tbody/tr/td[2]').getall()
        game_cheapest = response.xpath('//tbody/tr/td[3]/a/text()').getall()

        row_data = zip(game_name, game_price, game_cheapest)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            game_name = item[0] #item[0] means product in the list and so on, index tells what value to assign
            game_price = item[1]
            game_cheapest= item[2]    

            scraped_info = {
                #key:value
                'game_name' : game_name,
                'game_price': game_price,
                'game_cheapest': game_cheapest,
            }

            #yield or give the scraped info to Scrapy
            yield scraped_info


