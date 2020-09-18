#!/usr/bin/python3
from flask_restful import Resource, Api, reqparse
from yt_data import channel as ytchannel
from yt_data import search as ytsearch
from yt_data import video as ytvideo
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///yotter.db')
app = Flask(__name__)
api = Api(app)


class Channel(Resource):
    def get(self, channelId, page=1, includeVideos=True):
        if includeVideos < 1:
            includeVideos = False
        else:
            includeVideos = True

        channel = ytchannel.get_channel_info(channelId, includeVideos=includeVideos, page=page)
        return channel # Fetches first column that is Employee ID

api.add_resource(Channel, '/api/channel/<string:channelId>', 
                          '/api/channel/<string:channelId>/page/<int:page>',
                          '/api/channel/<string:channelId>/info/<int:includeVideos>') # 0 = False

class Video(Resource):
    def get(self, videoId):
        video = ytvideo.get_video_info(videoId)
        return video
api.add_resource(Video, '/api/video/<string:videoId>')

class Search(Resource):
    def get(self, search_terms, page=1, autocorrect=1, sort=0, filters={"time":0, "type":0, "duration":0}):
        search = ytsearch.search_by_terms(search_terms, page, autocorrect, sort, filters)
        return search
api.add_resource(Search, '/api/search/<string:search_terms>', 
                         '/api/search/<string:search_terms>/page/<int:page>',
                         '/api/search/<string:search_terms>/sort/<int:sort>',
                         '/api/search/<string:search_terms>/page/<int:page>/sort/<int:sort>')

if __name__ == '__main__':
     app.run()