# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from plushockey_backEnd.items import Match


class results(scrapy.Spider):
    name = 'results'
    allowed_domains = ['www.server2.sidgad.es/fgpatinaxe/fgpatinaxe_mc_1.php']
    start_urls = ['http://www.server2.sidgad.es/fgpatinaxe/fgpatinaxe_mc_1.php/']

    def parse(self, response):
        results = Selector(response).xpath('//div[@class="scorer_box"]/a')
        count = 0
        for result in results:
            
            item = Match()
            item['home_team'] = result.xpath('//div/div[@class="scorer_team_left"]/text()').extract()[count]
            item['away_team'] = result.xpath('//div/div[@class="scorer_team_right"]/text()').extract()[count]
            score = result.xpath('//div/div[@class="scorer_score"]/text()').extract()[count]
            score = score.replace("\n","")
            score = score.replace("\t","")
            item['score_home'] = score
            item['score_away'] = score
            item['date_time'] = result.xpath('//div/div[@class="scorer_bot_left"]/text()').extract()[count]
            count = count + 1
            # item['league'] = 
            yield item
