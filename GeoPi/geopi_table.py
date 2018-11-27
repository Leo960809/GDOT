from bs4 import BeautifulSoup
import requests
import csv
import sys


def get_infotable(proj_id):
	try:
		source = requests.get('http://www.dot.ga.gov/applications/geopi/Pages/Dashboard.aspx?ProjectID=' + proj_id).text
	except:
		sys.exit("ERROR. Plz check your Project ID.")

	soup = BeautifulSoup(source, 'lxml')
	tag_1 = soup.select('table')[2]
	info_table = [[item.text for item in line.select('td, b')]
			for line in tag_1.select('tr')]

	tag_2 = soup.select('table')[7]
	rg_table = [[item.text for item in line.select('td')]
			for line in tag_2.select('tr')]

	f_1 = open('infotable_' + proj_id + '.csv', 'w', newline='')
	writer = csv.writer(f_1)
	for item in info_table:
		writer.writerow(item)
	f_1.close()
	print("Project Info Table Scraped!")

	f_2 = open('rgtable_' + proj_id + '.csv', 'w', newline='')
	writer = csv.writer(f_2)
	for item in rg_table:
		writer.writerow(item)
	f_2.close()
	print("RG Master Table Scraped!")

	return 0


if __name__ == "__main__":
	proj_id = input("Input the Project ID:\n")
	get_infotable(proj_id)

