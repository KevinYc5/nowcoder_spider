from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import NowcoderItem

class NowcoderSpider(Spider):
    name = 'nowcoder_jobs'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.nowcoder.com/intern/center'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = NowcoderItem()
        jobs = response.xpath('//ul[@class="reco-job-list"]/li')
        for job in jobs:
            title = job.xpath(
                './/div[@class="reco-job-cont"]/a/text()').extract_first()
            if title:
                item['title'] = title
            else:
                item['title'] =' '

            company =  job.xpath(
                './/div[@class="reco-job-com"]/a/text()').extract_first()
            if company:
                item['company'] = company
            else:
                item['company'] = ' '

            address = job.xpath(
                '/html/body/div[1]/div[2]/div[2]/div/div[4]/ul/li[29]/div/div[3]/div[1]/span[1]/text()').extract_first()
            if address:
                item['address'] = address
            else:
                item['address'] = ' '

            salary = job.xpath(
                '/html/body/div[1]/div[2]/div[2]/div/div[4]/ul/li[29]/div/div[3]/div[1]/span[2]/text()').extract_first()
            if salary:
                item['salary'] =salary
            else:
                item['salary'] = ' '
            yield item

        next_url = response.xpath('/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/ul/li[11]/a/@href').extract()
        if next_url:
            next_url = 'https://www.nowcoder.com' + next_url[0]
            yield Request(next_url, headers=self.headers)
