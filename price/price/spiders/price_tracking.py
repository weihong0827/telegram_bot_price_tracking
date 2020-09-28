from scrapy_redis.spiders import RedisSpider


class PriceTrackingSpider(RedisSpider):
    name = 'price_tracking'

    def parse(self, response):
        print(response)
