#!/usr/bin/python

import webbrowser
import zipfile
from bs4 import BeautifulSoup
import urllib2
import lxml.html
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import requests ,io

#Second Page Parsing


def  directwithout(searchurl,g):
	a=[]
	s=[]
	#print searchurl
	dr = {'User-Agent': 'Mozilla/5.0'}
	req1 = urllib2.Request(searchurl,headers=dr)
	MyFile1= urllib2.urlopen(req1)
	MyHtml1 = MyFile1.read()
	MyFile1.close()
	soup1 = BeautifulSoup(MyHtml1,"lxml")
	i=0
	#print soup1.findAll("span").text.strip()
	for link in soup1.findAll('a'):

		if 'english' in link.get('href'):

		 	
		 	a.append(link.get('href'))

		 	

		 	if i < 5:
		 		
		 	 print "\n", i+1,':' ,link.findAll("span")[1].text.strip()
		 	 i=i+1
	print "\nCan't find the movie subtitle ? Make sure you enter the correct movie name"

	num = input("\nEnter the respective Number to Download: ")





	if num == 1:
	 f='https://subscene.com/'+a[0]
	 final(f)


	if num == 2:
	 q='https://subscene.com/'+a[1]
	 final(q)

	if num == 3:

	 w='https://subscene.com/'+a[2]
	 final(w)

	if num == 4:

	 e='https://subscene.com/'+a[3]
	 final(e)

	if num == 5:

	 r='https://subscene.com/'+a[4]
	 
	 final(r)

	if num =='EOF':
		print "hU"

	

	
	#print f



#Thrid page Parsing
def final(su):
	r = {'User-Agent': 'Mozilla/5.0'}
	req2 = urllib2.Request(su,headers=r)
	MyFile2= urllib2.urlopen(req2)
	MyHtml2 = MyFile2.read()
	MyFile2.close()
	soup2 = BeautifulSoup(MyHtml2,"lxml")
	third= soup2.find("div", {"class": "download"})
	inside2 = third.find('a')
	download='https://subscene.com/'+inside2['href']
	print "Downloading and Extracting Subtitle"
	r = requests.get(download)
	z = zipfile.ZipFile(io.BytesIO(r.content))
	z.extractall()
	print "Subtitle has downloaded Succesfully!!"


mna = raw_input("Enter Movie name: ")
mname=mna.replace(" ",'+').rstrip("+")
g = mname[:3]



searchurl = "https://subscene.com/subtitles/title?q="+mname+".720p"





print "\nGenerating Url"


hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(searchurl,headers=hdr)
MyFile= urllib2.urlopen(req)
MyHtml = MyFile.read()
MyFile.close()
soup = BeautifulSoup(MyHtml,"lxml")

a=soup.findAll()
j=len(a)

directwithout(searchurl,g)
 





 





