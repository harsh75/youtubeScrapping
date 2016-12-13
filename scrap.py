import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.youtube.com/user/narendramodi/videos")
soup=BeautifulSoup(r.content)
li=list(soup.find_all("li",{"class":"channels-content-item yt-shelf-grid-item"}))
count=0
for lix in li:
	print("Link is https://www.youtube.com%s" % lix.find("a",{"class":"yt-uix-sessionlink"}).get("href"))
	print("Time is %s" % lix.find("span",{"class":"video-time"}).text)
	print("Title is %s" % lix.find("h3",{"class":"yt-lockup-title"}).text)
	if(lix.find("ul",{"class":"yt-lockup-meta-info"}) != None):
		print("Number of Views is %s" % lix.find("ul",{"class":"yt-lockup-meta-info"}).find_all("li")[0].text)
		print("Time aploaded %s" % lix.find("ul",{"class":"yt-lockup-meta-info"}).find_all("li")[1].text)
	print()
	print()	
	count+=1
print('Total videos are')
print(count)	
