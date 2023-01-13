## NOTE
The complete 

## Description
A docker-containerized django based application that uses an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response with a scheduler that runs in background and fetched data from the Youtube API

## Instructions
This project is extremely easy and user friendly to setup, only pre-requisites being you should have docker in your system

 - Install docker in your machine (https://docs.docker.com/desktop/install/mac-install/)
 - Clone this repository 
 - `git clone https://github.com/atg-coder27/youtube-scheduler.git`
 - Cd into the directory
 - `cd youtube_api_project`
 - Run the docker-compose command to setup everything
 - `docker-compose up --build`


## API URLS
 - GetVideosByQuery (url = http://127.0.0.1:80/api/get_vidoes_by_query/)
 - params: [query,title,page_no]
 - Example : http://127.0.0.1:80/api/get_vidoes_by_query/?query=fifaWorldCup&page_no=1&title=football
 - This API inputs query as search_query , title and page_no required for pagination
 
   
## Features with Technologies
 - Django/Django-REST for the entire project
 - APS-Schduler to schdule and perform the fetching tasks from the Youtube API and saving asynchronously in the db in background
 - Postgres - To store the data, and perform db operations 
 - Redis - To create local in-memory caching system for updating tags based on clicks
 - Docker - To containerize everything and to make connections between them
 - Django.Pagination - To support pagination