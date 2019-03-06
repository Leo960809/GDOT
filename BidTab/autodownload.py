import requests
import sys
from bs4 import BeautifulSoup


def auto_download(letting_id):

	try:
		src = requests.get("https://www.bidx.com/ga/letting?lettingid=" + letting_id, stream=True).text
		print("Letting ID:", letting_id)
	except:
		sys.exit("ERROR. Wrong Letting ID.")

	soup = BeautifulSoup(src, "html.parser")

	for link in soup.find_all("a", text="Tabulations of Bids"):
		print(link.get("href"))



if __name__ == "__main__":

	auto_download("18121401")