import json
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Video:
    """Class with Video information"""

    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self.video_id: str = video_id
        data = self.video_data()
        try:
            self.title: str = data['items'][0]['snippet']['title']
            self.video_url: str = f'https://www.youtube.com/watch?v={self.video_id}'
            self.video_views: int = data['items'][0]['statistics']['viewCount']
            self.like_count: int = data['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.video_url = None
            self.video_views = None
            self.like_count = None

    def video_data(self) -> dict:
        """Return information about the video by its ID"""
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()
        return video_response

    def __str__(self) -> str:
        return self.video_name

class PLVideo(Video):
    """Class with the playlist"""
    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self.playlist_id: str = playlist_id
