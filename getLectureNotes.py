import urllib2
import re
import os

# Replace with correct video lectures url (the url of the page you arrive at after clicking 'Video Lectures' in the left column of the Coursera class page)
url='https://class.coursera.org/getdata-004/lecture'

# Replace XXX with correct cookie (get it by visiting the Coursera page while logged in, opening some web inspector, select Net tab, reload page, opening the request headers of the first GET command)
hdrs={
	'Cookie':'XXX'
}

directory=url.split('/')[-2]+'_lectureNotes'
if not os.path.exists(directory):
	os.makedirs(directory)

req = urllib2.Request(url, headers=hdrs)
html=urllib2.urlopen(req).read()

pdfs=[pdf+'pdf' for pdf in re.findall(r'href=\"(.*?)pdf',html)]
for pdf in pdfs:
	title=pdf.split('/')[-1]
	print title # So you know it's actually working
	doc=urllib2.urlopen(pdf).read()
	f=open(directory+'/'+title,'w')
	f.write(doc)
	f.close()
