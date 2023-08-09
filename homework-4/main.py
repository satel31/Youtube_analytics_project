from src.video import Video, PLVideo

if __name__ == '__main__':
    
    video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - id youtube video
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert str(video1) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert str(video2) == 'Пушкин: наше все?'
