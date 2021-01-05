from pytube import YouTube

print("-------- Welcome to our youtube video downloader Tautorial ---------")

video_link = input("Please enter the youtube video link: \n")

yt = YouTube(video_link)

available_videos = yt.streams

file_format = input("In which format you want to download the video : \n [video or audio] : ")

if file_format == "video":
    videos = available_videos.filter(file_extension='mp4')
elif file_format == "audio":
    videos = available_videos.filter(only_audio=True)
else:
    print("Invalid file format !!!!")

print(f"Displaying all the ' ",file_format," ' file format")

for video in videos:
    print(video)

file_index = int(input("Please enter the file index : \n [Starting with 0,1,2,.. ] : "))

videos[file_index].download()

print(f"Your file '",yt.title,"' Downloaded Successfully !!!!")