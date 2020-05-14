# Mission-to-Mars-Web-Scraping-HTML
# Web Scraping Homework - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this challenge I built a web application that scrapes various websites for data related to the NASA Mission to Mars and displays the information in a single HTML page. The following outlines what was completed.

## Step 1 - Web Scraping

Completed my initial scraping of the information below using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Created a Jupyter Notebook file called `mission_to_mars.ipynb` to complete all of my scraping and analysis work. Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

### NASA Mars News

* I scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and used python script to collect the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image

* Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

### Mars Weather

* Visited the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Saved the tweet text for the weather report as a variable called `mars_weather`.

### Mars Facts

* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. and converedt the data to a HTML table string.

### Mars Hemispheres

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's 4 hemispheres.

* Used a Python dictionary to store both image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name.

* Appended the dictionary with the image url string and the hemisphere title to a list with one dictionary for each hemisphere.

- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* The Jupyter notebook was converted into a Python script with a function that executed all scraping code to return one Python dictionary containing all of the scraped data.

* Next, a route was created to import the Python dictionary and store the return value in Mongo as a Python dictionary.

* Created a root route to query the Mongo database and pass the mars data into an HTML template to be displayed.

* Created a template HTML file to take the mars data dictionary and display all of the data in the appropriate HTML elements.

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)
