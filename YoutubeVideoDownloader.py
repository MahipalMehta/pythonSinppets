from pytube import YouTube
 
youtube_video_url = 'https://www.youtube.com/watch?v=DkU9WFj8sYo'
savepath="D:/" 
try:
    yt_obj = YouTube(youtube_video_url)
 
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
    # download the highest quality video
    filters.get_highest_resolution().download(savepath)
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)