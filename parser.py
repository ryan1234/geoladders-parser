import pycurl
import StringIO
from HTMLParser import HTMLParser

class GeoParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.in_td = False
		self.current_row = []
		self.recording = False

	def handle_starttag(self, tag, attrs):
		for name, value in attrs:
			if name == "action" and value == "show_activity_history.php#trips":
				self.recording = True
		if tag == "td" and self.recording == True:
			self.in_td = True
	def handle_endtag(self, tag):
		if tag == "tr" and self.recording == True:
        		print '\t'.join(self.current_row)
			self.current_row = []
		if self.recording == True and tag == "table":
			self.recording = False
	def handle_data(self, data):
		if self.in_td and self.recording == True:
			self.current_row.append(data)
 
parser = GeoParser()
html = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://www.geoladders.com/show_activity_history.php?user_id=582&daterange=13&year=&filter_rt=0&sort_by=2&sort_dir=0&all_data=1')
c.setopt(pycurl.WRITEFUNCTION, html.write)
c.perform()
parser.feed(html.getvalue())
