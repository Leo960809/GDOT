import requests
import sys
from bs4 import BeautifulSoup
import webbrowser
import csv


def auto_download(letting_id):

	try:
		src = requests.get("https://www.bidx.com/ga/letting?lettingid=" + letting_id, stream=True).text
		print("Letting ID:", letting_id)
	except:
		sys.exit("ERROR. Wrong Letting ID.")

	soup = BeautifulSoup(src, "html.parser")

	links = []
	for link in soup.find_all("a", text="Tabulations of Bids"):
		webbrowser.open("https://www.bidx.com" + link.get("href"), new=0, autoraise=True)

if __name__ == "__main__":

	with open("letting_id (2011.1-2019.1).csv", "r") as csvfile:
		csv_reader = csv.reader(csvfile, delimiter="\\")
		id_count = 0
		for row in csv_reader:
			auto_download(f'Letting ID: {", ".join(row)}'.split()[2])
			id_count += 1
		print(f"Processed {id_count} letting ids.")