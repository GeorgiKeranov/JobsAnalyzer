import time
from scraper import Scraper
from selenium.webdriver.common.keys import Keys
from visualize_data import visualize_data_in_pie_chart

# Here you can change the search terms to the things you want
# to analyze like for example progamming languages, frameworks, etc.
jobs_search_terms = [
	'Spring Boot',
	'Laravel',
	'Ruby on Rails',
	'Django',
	'Express.js',
]

jobs_found_results = []

# Initialize the scraper for linkedin
scraper = Scraper('https://www.linkedin.com')
# Go to LinkedIn and login with username and password or cookies if we have already logged in
scraper.add_login_functionality('https://www.linkedin.com/login', '#username', '#password', '', 'button[type="submit"]', 'linkedin')

# Enter the first search term in the search bar
search_input_selector = '.search-global-typeahead__input'
scraper.element_send_keys(search_input_selector, jobs_search_terms[0] + Keys.ENTER)

# Filter search results by jobs
jobs_button_selector = 'button[aria-label="Jobs"]'
scraper.element_click(jobs_button_selector)

# Filter search results location to be WorldWide
location_input_selector = 'input[aria-label="City, state, or zip code"]'
scraper.element_clear(location_input_selector)
scraper.element_send_keys(location_input_selector, 'Worldwide' + Keys.ENTER)

# Filter the jobs to only Remote ones
onsite_remote_button_selector = 'button[aria-label="On-site/Remote filter. Clicking this button displays all On-site/Remote filter options."]'
remote_jobs_label_selector = 'label[for="workplaceType-2"]'
show_results_button_selector = '.artdeco-hoverable-content--visible button[data-control-name="filter_show_results"]'
scraper.element_click(onsite_remote_button_selector)
scraper.element_click(remote_jobs_label_selector)
scraper.element_click(show_results_button_selector)

# Wait until the new jobs count is loaded
time.sleep(5)

# Get number of jobs found
jobs_found = scraper.find_element('.jobs-search-results-list__title-heading small')
jobs_found_text = (jobs_found.text).split(' ')[0]
jobs_found_number = int(jobs_found_text.replace(',', ''))

jobs_found_results.append(jobs_found_number)

search_input_jobs_selector = '.jobs-search-box__input--keyword .relative input:nth-child(2)'

for index, search_term in enumerate(jobs_search_terms):
	if index == 0:
		continue;

	scraper.element_clear(search_input_jobs_selector)
	scraper.element_send_keys(search_input_jobs_selector, search_term + Keys.ENTER)

	# Wait until the new jobs count is loaded
	time.sleep(5)

	# Get number of jobs found
	jobs_found_text = (jobs_found.text).split(' ')[0]
	jobs_found_number = int(jobs_found_text.replace(',', ''))
	jobs_found_results.append(jobs_found_number)

print(jobs_search_terms)
print(jobs_found_results)

visualize_data_in_pie_chart(jobs_found_results, jobs_search_terms)
