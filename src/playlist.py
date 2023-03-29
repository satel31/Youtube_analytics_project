import datetime

from googleapiclient.discovery import build
import os
import isodate


class PlayList:
    """Class with playlist's information"""

    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, pl_id: str) -> None:
        self.id: str = pl_id
        self.title: str = self.get_playlist_data()['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/playlist?list={self.id}'

    def get_playlist_data(self) -> dict:
        playlist_videos: dict = self.youtube.playlists().list(id=self.id, part='contentDetails, snippet',
                                                              maxResults=50, ).execute()
        return playlist_videos

    def get_video_ids(self) -> list[str]:
        """Return ids of all videos in the playlist"""
        playlist_videos: dict = self.youtube.playlistItems().list(playlistId=self.id, part='contentDetails',
                                                            maxResults=50, ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    @property
    def total_duration(self) -> datetime.timedelta:
        """ Returns the total duration of videos in the playlist"""
        video_response: dict = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(self.get_video_ids())).execute()
        playlist_duration = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            playlist_duration += duration
        return playlist_duration

    def show_best_video(self) -> str:
        """ Return the best video in the playlist according to the amount of likes"""
        video_response: dict = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=','.join(self.get_video_ids())).execute()
        best_video: dict = max(video_response['items'], key=lambda x: int(x['statistics']['likeCount']))
        best_video_url: str = f'https://youtu.be/{best_video["id"]}'
        return best_video_url
