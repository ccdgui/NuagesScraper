# NuagesScraper
## Gentle scraping of online forums using Scrapy 

The purpose of this scraper is to crawl select pages of a publicly available section of an online health forum ('message board'). The crawler returns structured json data from the messages posted by users. 

Highlights of this folder: 

  * nuages_spider: crawls pages in the domain patient.info and returns the following items: 1. 'bubble id' (arbitrary number generated by  a counter), 2. the author of the thread ('node 0'), 3. author of the post ('node 1'), reciever of the post ('node 2') and message content ('bubble content').  
 
  * items.py: contains the Class object ForumCloudItem for input processing (remove tags) and output processing (take first element, where applicable. 
  
  * pipeline.py: starts exporting, processing, saves json to file and close spider. 
  
  * settings.py: sets 'depth limit' to 2 to control the volume of data returned by the crawler and sets a Download_delay of 3 seconds to limit the number of requests made to the site. 


  
