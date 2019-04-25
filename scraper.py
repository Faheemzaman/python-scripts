import re
from selenium import webdriver
#from selenium import WebElement
from selenium.webdriver.common.by import By


def get_links(html):

 #print (html)

 """ Return a list of links from html    """    
 
 

 # webpage_regex = re.compile("""/(http|https|ftp|ftps)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/\S*)?/""", re.IGNORECASE)    
 # a regular expression to extract all links from the webpage  
 # https?:\/\/.*?\/ 
 # "^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)+[A-Za-z]{2,6}$"
 # webpage_regex = re.compile("""^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)+[A-Za-z]{2,6}$""", re.IGNORECASE)    
 webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
 # list of all links from the webpage    
 return webpage_regex.findall(html) 

 
 
def get_urls():

 file = open("prc_pcu_precategorized_urls.csv") 
 urls = file.readlines()
 file.close()

 urls = [url.strip() for url in urls] 
 
 """
 i = 0
 for url in urls:
  urls[i].strip('\n')
  i = i + 1
 """
 return urls 

 

 
def open_url_in_browser(url):

 #print (url)
 url = 'http://' + url
 print (url)
 browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice

 
 try:
 
  browser.get(url) #navigate to the page
 
 except Exception as e:
  
   if 'Cannot navigate to invalid URL' in str(e):
    print ('INVALID URL')
 browser.close()

def is_valid_url (url):

 return


urls = get_urls()
# print (urls)

for url in urls:

 print (url) 
 open_url_in_browser(url)


 
 
 
"""
 
 
browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice

browser.get(url) #navigate to the page

#WebDriverWait(browser, 10)

#find number of iframes 
#numOfFrames = browser.execute_script("return window.length")
# numOfFrames = browser.findElements(By.tagName("iframe")).size()
ifameList = browser.find_elements_by_tag_name('iframe')

i = 0
while i < len(ifameList): 
 # browser.switch_to_frame(ifameList[i])
 full_text = browser.page_source
 # print (browser.page_source)
 i = i + 1
 
for link in get_links(full_text):            
 print (link)
 #if re.match(link_regex, link):                
 #crawl_queue.append(link)

 
#print(len(list))


#print (numOfFrames)

#switch to iframe based on index

"""
"""
i = 0

while (i < len(ifameList)):

driver.find_elements_by_tag_name('iframe')[i].getAttribute("id")
 

 str = "return document.getElementsByTagName('iframe')[{}].getAttribute('id')".format(i)

 id_name = browser.execute_script(str) #returns the inner HTML as a string

 #print (id_name)
 str2 = "return document.getElementById('{}').contentDocument.body.innerHTML".format(id_name)

 iframe_innerHtml = browser.execute_script(str2)
 print (iframe_innerHtml)
 i= i + 1
 

"""
#id = browser.execute_script("return document.getElementsByTagName('iframe')[i].getAttribute('id')") #returns the inner HTML as a string
  
  #WebElement abc = driver.find_elements_by_tag_name('iframe')[i]
  #browser.switch_to_frame(abc)  
  
"""
 # iframe = driver.find_elements_by_tag_name('iframe')[i]
  
  #browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
  browser.switch_to_frame(ifameList[i]) 
  # print (document.body.innerHTML)
  #print (ifameList[i].contentDocument.body.innerHTML)
  #iframe_innerHtml = browser.execute_script("return Document.contentDocument.body.innerHTML")
  print (iframe_innerHtml)
  i = i + 1
  #iframe_innerHtml = browser.execute_script("return document.getElementById('kayako-messenger-frame').contentDocument.body.innerHTML")
"""


# get all iframe id'


# get innerhtml of all iframes based on id's

#switch among frames
"""
i =0
while i < numOfFrames:
 browser.switch().frame(i)
 
 i +=1
"""


# deal "element not found" exception



#iframeElements = browser.findElements(By.tagName("iframe"));

#print (iframeElements.size())


#document.getElementsByTagName("iframe")[0].getAttribute("id")
#id = browser.execute_script("return document.getElementsByTagName('iframe')[0].getAttribute('id')") #returns the inner HTML as a string
#frames = browser.execute_script("return document.getElementsByTagName('iframe')") #returns the inner HTML as a string
#print (id)
#str = "return document.getElementById({}).document.body.innerHTML"
#element = str.format(id)
#print (element)


#iframe_innerHtml = browser.execute_script("return document.getElementById('kayako-messenger-frame').document.body.innerHTML")
#iframe_innerHtml = browser.execute_script("return document.getElementById('kayako-messenger-frame').contentDocument.body.innerHTML")

#iframe_innerHtml = browser.execute_script("return document.getElementById(%s).document.body.innerHTML")
#print (iframe_innerHtml)

#browser.find_element_by_id(iframes[0])

#iframes = browser.find_element_by_tag_name("iframe")
#print (iframes[0].id)
#print (browser.find_element_by_id(iframes[0]))

#iframe_innerHtml = browser.execute_script("return document.getElementById(iframes[0]).document.body.innerHTML")
#print (iframe_innerHtml)

#document.getElementById('myIframe').document.body.innerHTML;
#document.getElementById(iframes[0]).document.body.innerHTML;

#var iframes=document.getElementsByTagName("iframe");
#document.write("<br><br>IFRAME ids:<br>");
#for(var i=0; i<iframes.length; i++){

#document.write("["+i+"].id='"+iframes[i].id+"'<br>");
#}







#browser.get("http://abc.com") #navigate to page behind login
#size = browser.execute_script("return document.getElementsByTagName(\"iframe\")) #returns the inner HTML as a string
#innerHTML = browser.execute_script("return document.innerHTML") #returns the inner HTML as a string
#size = browser.findElements(By.tagName("iframe")).size();
#innerHTML = browser.execute_script("return window.frames") #returns the inner HTML as a string
#print (size)
#innerHTML = browser.execute_script("return window.frames") #returns the inner HTML as a string



#print (innerHTML)


#for link in get_links(innerHTML):            
# print (link)
  #if re.match(link_regex, link):                
  #crawl_queue.append(link)

#browser.close()
