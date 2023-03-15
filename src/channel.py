import json
from googleapiclient.discovery import build
import os


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        data = self.json_to_python()

        self.title = data['items'][0]['snippet']['title']
        self.channel_description = data['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.channel_subscription = data['items'][0]['statistics']['subscriberCount']
        self.video_count = data['items'][0]['statistics']['videoCount']
        self.channel_views = data['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        return json.dumps(channel, indent=2, ensure_ascii=False)

    def json_to_python(self):
        json_data = self.print_info()
        channel_data = json.loads(json_data)
        return channel_data

    @classmethod
    def get_service(cls):
        """ :return: объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, filename):
        """Сохранят в файл значения атрибутов экземпляра Channel"""
        python_data = {}

        python_data['channel_id'] = self.__channel_id
        python_data['title'] = self.title
        python_data['channel_description'] = self.channel_description
        python_data['url'] = self.url
        python_data['channel_subscription'] = self.channel_subscription
        python_data['video_count'] = self.video_count
        python_data['channel_views'] = self.channel_views

        json_data = json.dumps(python_data, indent=2, ensure_ascii=False)

        filepath = os.path.join(os.getcwd(), filename)

        with open(filepath, 'w') as file:
            file.write(json_data)
