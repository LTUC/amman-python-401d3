# Web Scraping

We can consume web sites with our eyes, ears and fingers. But how about getting your computer to consume it for you?

If a service exposes an API then you're good to go. But what if they haven't? That's where web scraping comes in.

#### Describe and Define

- Why to scrape a web site
- Legal pespectives on web scraping
- Challenges of web scraping

#### Execute

- Use `requests` and `beautiful soup` libraries
- Inspect a web pages content to determine an effective scraping method
- Execute web scraper from CLI

## Today's Outline

- Lab Preview
- Lecture
    - Legality
    - Ethics
    - Terms of service
    - Blocking
- Demo

## Notes
  - We can use a request library to get the data from the server
  - ajax from jquery lib
  - superagent
  - browser
  - postman
  - insomnia
  - curl
  - wget
  - httPie (http)

Webscraping - using scripts, bots or some other automated process to read data and aggregate data from a web page.

Why scrape ?
- No API available
- Make collecting the data easier to collect than copying and pasting or 'eyeballing' it
- Web page data is not in the format we need so we transform it
- Search Engines

user search -> keyword -> engine visits every website for this keyword <- returns sites that contains this keyword

We could use Caching but this still has some limits
 - Someone has to be first, so some user will get that slow result

## Legality
 - It is legal to scrape any published information
 - However it could be unethical
    - e.g. Scrape police websites for notices about criminal charges and keep a database of persons criminal records, the police websites removed the data after 1 week but this company had the records permanently.
    - Sell Data
    - Repost the data and make the persons pay to have it removed etc..
## Terms of Service
    - Ok to read data, maybe even bookmark the source or save the data but it may not be okay to republish the same data or modified data
## Not appreciated by the data holder
    
e.g. LinkedIn case
## May take steps to block you
 - I'm not a robot CAPTCHA
 - robots.txt -  Most search engines respect this; tells the crawler where it is allowed to go

## How to Scrape

 1. Find URL
 2. Find Data to Extract
    1. Visit Page
    2. Inspect Page (or View Source)
    3. Look for html around the data we are interested in
 3. Write The Code and Run it
    1. Reads URL - "https://www.monster.com?q=Programmer&location=Jordan" - requests library
        1. import an http client library
        2. setup and make the request headers, method, url
        3. save the response
    2. Parse Data - beautiful soup library
    3. Save Data


## Resources

- https://replit.com/@dariothornhill/web-scrape#search.draw
- https://realpython.com/beautiful-soup-web-scraper-python/
- https://web.archive.org/