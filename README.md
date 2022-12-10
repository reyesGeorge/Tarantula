Tarantula, a base scraping infastructure
<img height="300" width="400" alt="Spider Logo" src="https://github.com/reyesGeorge/Tarantula/blob/main/tarantula_image.png">


- To get started cd into the `theZoo` file and run: 
- chmod +x script.sh
- then: ./script.sh
- This will spin up a Postgres container, the Python environment, a Redis container, a Squid container (for the proxy) and a Splash container
- The docker container will automaticaly run the JS spider which is the most complicated one. The other spiders are located under the spider directory and there are some tests under the /validate directory. These tests will use pandas to sql query postgres to make sure the data was added to the DB.

- The project took me 2 days to complete. I spent most of my time learning about docker compose and the networking aspect of containers as well as the rotating proxies/user agents people add to their spiders.

> Below I have outlined the steps I took as I completed the project


## Docker
- I downloaded the Docker Desktop application for MacOS
- I looked up docker images for the technologies used, and I found some for postgres, squid, splash and redis

## Python Environment
- I setup a Python virtual environment in my IDE, here I developed the whole project to keep my packages enclosed so they did not conflict with my global packages in my machine. Once I was finished and tested the spiders to make sure they worked properly I dockerized everything into containers.
- Packages I downloaded: pip, setuptools, wheel, Scrapy, Pandas, SQLAlchemy, scrapy-splash, scrapy-redis and psycopg2-binary
- I created a requirements.txt file so I could cat the pip list of my package versions into the file for easy replication
- The models.py file contains the SQLAlchemy code and the database schema
- The pipelines.py file is where our data is sent to Postgres

### The Default Spider
This crawler grabs quotes from the `Default` endpoint using pagination. 

The data is scraped and sent to Postgres as well as downloaded to a json file called items.json

### The Scroll Spider
This crawler uses scrolling to grab quotes from the `Scroll` endpoint.

Previously I had used a puppeter like bot where you can input how much padding the bot should scroll to scrape your desired data. In this instance using Scrapy I did not know how to do that, so I ended up looking up an alternative method. I found that the data is still being paginated in the request. When you google inspect you can see a console log that names the page you are on, so I looked at the request body and found how the data was being loaded. At this point I could have used the requests library, but instead found how to do it using Scrapy. This scraper works the same as the default one where the page number is added to the end of the url to retreive the next batch of data.

### The JS Spider
This crawler uses a JS rendering service called Splash to query the `JavaScript` endpoint in order to grab the quotes.

I had to add Splash specific middlewares to the Scrapy settings in order to make this work. I also created a docker image in my docker compose file that holds the Splash instance. Then the scraping worked just like the default spider.

### The Login Spider
This crawler scrapes the input field for the csrf token. It then submits a form request, authenticates and scrapes the rest of the data as the default spider does.

## Notes
- I added a user agent that makes me look like a more realistic person in the settings file. I also added the item pipeline and some configuration for the docker containers. I also added a download delay of 2 seconds so that the scraper does not scrape too fast.

- Adding the Proxy was a bit tricky for me. I tried using a project called Scylla, however it did not end up working with my envirnonment so I was looking for alternatives. I ended up using Squid, created a docker image and added the proxy configuration in the middleware.py file.

- The pause/resume scraping functionality comes from scheduler_persist being set to `True` in the settings using the scrapy-redis package.

- While containerizing my application I have never had to use Docker Compose, SQLAlchemy or Redis so I quickly learned in order to integrate them into my project.


## Potential Features in the Future 
- I did not collect much metadata but I saw a package called scrapy-magic fields and I would have liked to implement it to add the timestamps and urls scraped to the DB items

- I did not create GUI tools for the Postgres and Redis to make it easier to view, this would have been a nice addition

- Since only the JS spider is triggered by the script the other ones are manual I only set up a single table, but for a more distributed process I think making more models and tables for each spider would have been good. I wanted to reuse the code so I left it how it is.

- Cron job functionality
