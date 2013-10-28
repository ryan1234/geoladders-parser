import pycurl
import StringIO
from bs4 import BeautifulSoup

html = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://www.geoladders.com/show_activity_history.php?user_id=582&daterange=13&year=&filter_rt=0&sort_by=2&sort_dir=0&all_data=1')
c.setopt(pycurl.WRITEFUNCTION, html.write)
c.perform()

soup = BeautifulSoup(html.getvalue())

for row_index, row in enumerate(soup.find_all('table')[6].find_all('tr')):
	if row_index > 0:
		new_row = []
	
		for cell_index, cell in enumerate(row.find_all('td')):
			if (cell_index == 0):
				new_row.append(cell.get_text())

			if (cell_index == 1):
				new_row.append(cell.get_text()[:10])

			if (cell_index == 3):
				new_row.append(cell.find_all('a')[0].get_text())
				
				miles = cell.find_all('font')[0].find_all('font')[0].get_text()
				new_row.append(miles.replace(u" miles\xa0\xa0\xa0\xa0\xa0\xa0", ""))				

				elevation = cell.find_all('font')[0].get_text().replace(miles, "")
				new_row.append(elevation.replace(u" ft\xa0\xa0\xa0\xa0\xa0\xa0", ""))

			if (cell_index == 4):
				time = cell.get_text()
				if (len(time) > 0):
					new_row.append(time.split(' ')[0])
					new_row.append(time.split(' ')[1])
				else:
					new_row.append("0:00:00")
					new_row.append("0:00:00")

			if (cell_index == 7):
				calories = cell.get_text()

				if (len(calories) > 0):
					new_row.append(cell.get_text())
				else:
					new_row.append("0")

			if (cell_index == 8):
				hrm = cell.get_text()
				
				if (len(hrm) > 0):
					if ("/" in hrm):
						new_row.append(hrm.split('/')[0])
						new_row.append(hrm.split('/')[1])
					else:
						new_row.append(hrm)
						new_row.append("0")
				else:
					new_row.append('0')
					new_row.append('0')

		print new_row
