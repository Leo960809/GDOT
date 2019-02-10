from bs4 import BeautifulSoup
import requests
import csv
import sys


def get_infotable(letting_id):

	try:
		source = requests.get('https://www.bidx.com/ga/apparentbids?lettingid=' + letting_id).text
		print("Letting ID:", letting_id)
	except:
		sys.exit("ERROR. Plz check your Letting ID.")

	soup = BeautifulSoup(source, 'lxml')

	tag_1 = soup.select('table')[2]
	info = [[item.text for item in line.select('td')]
			for line in tag_1.select('tr')]

	f = open('info_' + letting_id + '.csv', 'w', newline='')
	writer = csv.writer(f)
	for item in info:
		writer.writerow(item)
	f.close()
	print("Info Scraped!")

	return 0



if __name__ == "__main__":

	with open('letting_id.csv') as csv_file_1:
		csv_reader = csv.reader(csv_file_1, delimiter='\\')
		line_count = 0
		for row in csv_reader:
			get_infotable(f'Letting ID: {", ".join(row)}'.split()[2])
			line_count += 1
		print(f'Processed {line_count} lines.')

