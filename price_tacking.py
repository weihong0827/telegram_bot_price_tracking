# %%
def lazada_price(url):
    global logFile
    detail = {}
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    
    br = webdriver.Chrome(options = chrome_options)
    br.get(url)
    time.sleep(5)
    html = etree.HTML(br.page_source)
    try:
        detail['title'] = html.xpath('.//span[@class="pdp-mod-product-badge-title"]/text()')[0]
        detail['price'] = html.xpath('.//div[@class="pdp-product-price"]/span/text()')[0]
    except:
        now = datetime.datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")
        logFile.write(current_time+'|p&tError|' + url+'\n')
        sentemail('lazada get title and price error',url)
    if not detail['title'] or not detail['price']:
        sentemail('lazada bug',url)
    return detail
 


# In[ ]:


def shopee_price(url):
    
    detail = {}
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    
    br = webdriver.Chrome(options = chrome_options)
    br.get(url)
    time.sleep(5)
    html = etree.HTML(br.page_source)
    try:
        detail['title'] = html.xpath('.//div[@class="flex-auto flex-column  _2TJgvU"]/div/span/text()')[0]

        detail['price'] = html.xpath('.//div[@class="_3n5NQx"]/text()')[0]
    except:
        global logFile
        now = datetime.datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")
        logFile.write(current_time+'|p&tError|' + url+'\n')
        sentemail('shopee get title and price error',url)
    if not detail['title'] or not detail['price']:
        sentemail('shopee bug',url)
    return detail
    
#shopee_price('https://shopee.sg/Medical-Grade-Disposable-Mask-3PLY-(50pcs)-i.251231796.7729085519')


# In[ ]:


def carousell_price(url):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    response = requests.get(url,headers = headers)
    html = etree.HTML(response.text)
    detail = {}
    try:
        detail['title'] = html.xpath('.//h1/text()')[0]

        detail['price'] = html.xpath('.//h2/text()')[0]
    except:
        global logFile
        now = datetime.datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")
        logFile.write(current_time+'|p&tError|' + url+'\n')
        sentemail('carousell get title and price error',url)
        
    if not detail['title'] or not detail['price']:
            sentemail('carousell bug',url)
            
    return detail
#carousell_price('https://sg.carousell.com/p/kn95-mask-286427470/?t-id=of7Yg41tiE_1589004167518&t-referrer_browse_type=search_results&t-referrer_request_id=ggmFeg_xPx2zKVrT&t-referrer_search_query=kn95%20mask&t-referrer_sort_by=popular')


# In[ ]:


def ntuc_price(url):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    response = requests.get(url,headers = headers)
    html = etree.HTML(response.text)

    detail = {}
    try:
        detail['price'],detail['title']  = html.xpath('.//span[@class="sc-13n2dsm-3 bZLqUs"]/span/text()')
    except:
        global logFile
        now = datetime.datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")
        logFile.write(current_time+'|p&tError|' + url+'\n')
        sentemail('ntuc get title and price error',url)
    
    if not detail['title'] or not detail['price']:
        sentemail('ntuc bug',url)

    return detail
#ntuc_price('https://www.fairprice.com.sg/product/labmed-3-ply-adult-disposable-face-mask-50pcs-90016760')


# In[ ]:


def giant_price(url):
    detail = {}
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    
    br = webdriver.Chrome(options = chrome_options)
    br.get(url)
    time.sleep(60)
    html = etree.HTML(br.page_source)
    try:
        detail['title'] = html.xpath('.//div[@class="fancybox-container product-lightbox2 fancybox-is-open"]/div[2]/div[4]/div/div/div/div[2]/h1/text()')[0]
        detail['price'] = html.xpath('.//div[@class="fancybox-container product-lightbox2 fancybox-is-open"]/div[2]/div[4]/div/div/div/div[2]/div[2]/div/div/text()')[0]

    except:
        global logFile
        now = datetime.datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")
        logFile.write(current_time+'|p&tError|' + url+'\n')
        sentemail('giant get title and price error',url)
    
    if not detail['title'] or not detail['price']:
        sentemail('giant bug',url)
    return detail


# In[ ]:


def guardian_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    
    response = requests.get(url,headers = headers)
    html = etree.HTML(response.text)

    detail = {}
    try:
        detail['title'] = html.xpath('.//h2[@class="product_name_pdp"]/text()')[0]
        try:
            detail['price'] = html.xpath('.//div[@class = "pdp_price_section pull-right text-right"]/p/text()')[0].strip()
        except:
            detail['price'] = html.xpath('.//div[@class = "pdp_price_section pull-right text-right"]/h2/text()')[0].strip()
    except:
        global logFile
        now = datetime.datetime.now()
        current_time = now.strftime("%Y/%m/%d %H:%M:%S")
        logFile.write(current_time+'|p&tError|' + url+'\n')
        sentemail('giant get title and price error',url)
    
    if not detail['title'] or not detail['price']:
            sentemail('guradian bug',url)

    return detail
    
#guardian_price('https://www.guardian.com.sg/stylemaster-3-ply-surgical-mask-50s/p/616426')
