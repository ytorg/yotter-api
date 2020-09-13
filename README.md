# yotter-api
Yotter API built with Flask and Python.
* [Test the API](test-the-api)
* [Endpoints](endpoints)

## Repo structure
* **yt_data** contains all the python files required to gather all the Youtube data.
* **tw_data** contains all the python files required to gather all the Twitter data.
* **server.py** contains the API logic.

# Yotter-Youtube API
## Endpoints:
All endpoints return a JSON with the info.

### Search:
* `/api/search/<string:search_terms>`
  > Returns a JSON with the 20 first search results.
  
* `/api/search/<string:search_terms>/page/<int:page>`
  > Returns a JSON with the 20 first search results from page <int:page>
  
* `/api/search/<string:search_terms>/sort/<int:sort>`
  > Returns a JSON with the 20 first search results sorted by <int:sort>.
  
*  `/api/search/<string:search_terms>/page/<int:page>/sort/<int:sort>`
   > Returns a JSON with the 20 first search results from page <int:page> sorted by <int:sort>.
   
### Channels:
* `/api/channel/<string:channelId>`
  > Returns a channel's (channelId) info and videos.
* `/api/channel/<string:channelId>/page/<int:page>`
  > Returns a channel's (channelId) info and the videos from page <int:page>
* `/api/channel/info/<string:channelId>`
  > Returns only a channel's info.
  
## Test the API
Install `python3`, `python3 pip`, `python3 venv` and `git` if not already installed.

1. Clone this repository:
  * `git clone https://github.com/ytorg/yotter-api`
2. `cd yotter-api`
3. Create a python `venv`:
  * `python3 -m venv venv`
4. Activate the virtual environment:
  * `source venv/bin/activate`
5. Install requirements:
  * `pip install -r requirements.txt`
6. Run the development server:
  * `flask run --host 0.0.0.0`
7. Try it out!
  * `curl 127.0.0.1:5000/api/search/Never Gonna Give You Up`
