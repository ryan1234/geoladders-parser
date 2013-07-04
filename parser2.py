import pycurl
import StringIO
from bs4 import BeautifulSoup

html = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://www.geoladders.com/show_activity_history.php?user_id=582&daterange=13&year=&filter_rt=0&sort_by=2&sort_dir=0&all_data=1')
c.setopt(pycurl.WRITEFUNCTION, html.write)
c.perform()

soup = BeautifulSoup(html.getvalue())

#for table in soup.find_all('table'):
	#print(table)

state = soup.find_all('table')[6].find_all('tr')[1].find_all('td')[0]
print state.get_text()
