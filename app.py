import pafy
import yt_dlp
import time
from playsound import playsound
print("Hi,I'm SAIF's creation.\n")
while(True):
    video_no=int(input("How many videos do you want to download- "))
    urllist=[]
    for i in range(video_no):
      a=input("Enter URL of Video- ")
      urllist.append(a)
    for i,j in enumerate(urllist):
        video=pafy.new(urllist[i])
        print("downloading ",video.title)
        str=video.streams
        for i in str:
            print(i)
    #if (ans=="yes" or ans=="Yes" or ans=="YES" or ans=="y"):
        best=video.getbest()
        s0=int(best.get_filesize())
        s1=int((s0/1024)/1024)
        print("best resolution = ",best.resolution,s1,"MB")
        starttime=time.time()
        best.download(filepath=r"C:\Users\syeds\video lectures")
        endtime=time.time()
        timetaken=((endtime-starttime)/60)
        print("Download Time = ",timetaken,"minutes")
        print("Average download speed = ",int(s1/timetaken),"MB/minute")
    playsound(r"C:\Users\syeds\Downloads\1664860841766p2rf0tzk-voicemaker.in-speech (2).mp3")



