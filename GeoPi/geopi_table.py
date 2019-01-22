from bs4 import BeautifulSoup
import requests
import csv
import sys


def get_infotable(proj_id):

	try:
		source = requests.get('http://www.dot.ga.gov/applications/geopi/Pages/Dashboard.aspx?ProjectID=' + proj_id).text
		print("Project ID:", proj_id)
	except:
		sys.exit("ERROR. Plz check your Project ID.")

	soup = BeautifulSoup(source, 'lxml')

	tag_1 = soup.select('table')[2]
	info_table = [[item.text for item in line.select('td, b')]
			for line in tag_1.select('tr')]

	tag_2 = soup.select('table')[5]
	description = [[item.text for item in line.select('td')]
				for line in tag_2.select('tr')]

	tag_3 = soup.select('table')[7]
	rg_table = [[item.text for item in line.select('td')]
			for line in tag_3.select('tr')]

	f = open('info_' + proj_id + '.csv', 'w', newline='')
	writer = csv.writer(f)
	for item in info_table:
		writer.writerow(item)
	for item in description:
		writer.writerow(item)
	for item in rg_table:
		writer.writerow(item)
	f.close()
	print("Info Scraped!")

	return 0



if __name__ == "__main__":

	with open('project_id.csv') as csv_file_1:
		csv_reader = csv.reader(csv_file_1, delimiter='\\')
		line_count = 0
		for row in csv_reader:
			get_infotable(f'Project ID: {", ".join(row)}'.split()[2])
			line_count += 1
		print(f'Processed {line_count} lines.')

