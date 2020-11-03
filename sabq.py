from bs4 import BeautifulSoup as bs
import requests
import lxml
import sys
reload(sys)
sys.setdefaultencoding('utf8')
response = requests.get("https://sabq.org/%D9%85%D8%AD%D8%B7%D8%A7%D8%AA")
page_html = response.text
#print page_html
soup = bs(page_html, "lxml")
newsdivs = soup.findAll("div", {"class": "news-block"})
titles_list = []
links_list  = [] 
summary_list= [] 
images_list = [] 
for div in newsdivs:
    title = div.find("h2")
    link = title.find("a")
    titles_list.append(link.text) 
    links_list.append(link['href'])
    # to do remove the last for elements from the list 
for div in newsdivs:
    try:
      image = div.find("img") 
      image_link = image["src"] 
      images_list.append(image_link)
      p = div.find("p") 
      summary = p.text
      summary_list.append(summary)
    except:
        #print "this tag does not have an image" 
        pass

# clean lists from garbage data, here the last four items are garbage, so delete them  
titles_list = titles_list[: len(titles_list) - 4]
links_list = links_list[: len(links_list) - 4]

#open the html page 
with open("header.html","r") as hr:
    page_header = hr.read()
with open("footer.html","r") as fr:
    page_footer = fr.read() 
output_page = open("sabq.html","w") 
# include the header template to the page 
output_page.write(page_header)
 
for news in range(len(titles_list)):
        output_page.write("<div class= 'ui piled segment' dir='rtl' >") # start of container div 
        output_page.write("<h4 class='header'>" + titles_list[news] + "</h4>")
        output_page.write("<a href="+links_list[news]+">")   
        output_page.write("<img class='ui responsive image'  src="+images_list[news]+">")
        output_page.write("</a>") 
        output_page.write("<p>" + summary_list[news] + "<p>")
        output_page.write("</div>") # this is the end of container div 
#close the page container
output_page.write("<div class='ui container'>")   
# include the page footer to the page 
output_page.write(page_footer)  
        
