import time
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from visualize_data import visualize_data_in_pie_chart

# Here you can change the search terms to the things you want
# to analyze like for example progamming languages, frameworks, etc.
jobs_search_terms = [
	"Python Developer",
	"JavaScript Developer",
	"Java Developer",
	"C# Developer",
	"C++ Developer",
	"C Developer",
	"PHP Developer",
	"Ruby Developer",
	"Golang Developer",
	"Perl Developer",
	"Swift Developer",
	"Rust Developer",
	"SQL Developer"
]

# Here we will save the jobs count for every search term
jobs_found_results = []

# URL for the LinkedIn jobs that are worldwide
url = "https://www.linkedin.com/jobs/search?location=Worldwide&geoId=92000000&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&keywords="

# Search by every search term
for search_term in jobs_search_terms:
	# Add the search term to the url
	url_specific = url + urllib.parse.quote(search_term)
	
	# Create get request with the search term
	page = urlopen(url_specific)
	html = page.read().decode("utf-8")

	# Create BeatifulSoup object to get html data easier from the html response
	soup = BeautifulSoup(html, "html.parser")

	# Search for <label for="f_TRP-3"></label> and get the text in it
	jobs_count_text = soup.find("label", {"for" : "f_TPR-3"}).text

	# We have this text now "Any Time (143,727)" and we are converting it to "143,727"
	jobs_count_text = ((jobs_count_text.split("("))[1]).split(")")[0]

	# We have this text now "143,727" so we convert it to "143727" and integer
	jobs_count = int(jobs_count_text.replace(",", ""))

	jobs_found_results.append(jobs_count)

	# Create the next request after 2 seconds in order to not be detected as a bot
	time.sleep(2)

# Visualize data in pie chart
visualize_data_in_pie_chart(jobs_found_results, jobs_search_terms)