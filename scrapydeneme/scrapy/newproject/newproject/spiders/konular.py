import scrapy
class QuotesSpider(scrapy.Spider):
    name = "konu"
    start_urls=[
   "https://avesis.istanbulc.edu.tr/eyguven/topics"
    ]
    def parse(self,response):
        
          kisiler = response.css('ul.with-shaded-label')
          for kisi in kisiler.css('li h3::text').getall():
            if(kisi != ' '):
             yield {
            
              'Alan':kisi
             }
          
         

         