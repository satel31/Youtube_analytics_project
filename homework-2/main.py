from src.channel import Channel

if __name__ == '__main__':
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # Get data
    print(vdud.title)  # вДудь
    print(vdud.video_count) 
    print(vdud.url)  # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

    # Can't change
    vdud.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # Get object to work with API
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # Create file 'vdud.json' with channel data
    vdud.to_json('vdud.json')
