## IN THIS I FIRST INSTALL IS requests-html==0.10.0
## SECOND IS pip install lxml5.1.0 
## https://www.google.com/search?q=WEATHER+IN+PONDICHERY
##user agent Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
## span class="wob_t q8U8x"  id="wob_tm"
## for that *c class="vk_bk wob-unit"

from requests_html import HTMLSession


def  get_weather():
        s= HTMLSession()
        query = "pondicherry"
        url = f'https://www.google.com/search?q=WEATHER+IN+{query}'
        r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})
        temp = r.html.find('span#wob_tm' , first= True).text
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
        desc= r.html.find('span#wob_dc', first= True).text
        return temp+ " " + unit+ " " + desc
