import pycurl
import StringIO
from HTMLParser import HTMLParser

class GeoParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
	if tag == "table":
        	print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
	if tag == "table":
        	print "Encountered an end tag :", tag
    #def handle_data(self, data):
        #print "Encountered some data  :", data
 

parser = GeoParser()
html = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://www.geoladders.com/show_activity_history.php?user_id=582&daterange=13&year=&filter_rt=0&sort_by=2&sort_dir=0&all_data=1')
c.setopt(pycurl.WRITEFUNCTION, html.write)
c.perform()
parser.feed(html.getvalue())
