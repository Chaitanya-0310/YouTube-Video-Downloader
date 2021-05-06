from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


Folder_Name = " "

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text = Folder_Name, fg="royalblue")

    else:
        locationError.config(text="Please Select Folder",fg="red")


#download video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text = "Select Video Quality", fg="red")

        #download function
        select.download(Folder_Name)
        ytdError.config(text="Download Completed")

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("400x400")
root.columnconfigure(0,weight=1)

#video_entry
ytdLabel = Label(root, text= "Enter the URL of the Video", font = ("Palatino",15,"bold"))
ytdLabel.grid()


ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=60, textvariable = ytdEntryVar)
ytdEntry.grid()

#choose_path
saveLabel = Label(root,text="Save the Video file",font=("Palatino",15,"bold"))
saveLabel.grid()

saveEntry = Button(root,width=15,bg="turquoise",activebackground = "Sky blue",fg="black",text="Choose Path",command = openLocation)
saveEntry.grid()

#folderError
locationError = Label(root,text="Path Error Message", fg="steelblue",font=("Palatino",11))
locationError.grid(column=0, row=6, padx=20, pady=20)

locationError.grid()

#video_quality
ytdQuality = Label(root,text ="Select Video Quality",font=("Palatino",15,"bold"))
ytdQuality.grid()

choices = ("360p","720p","Only Audio")
ytdchoices = ttk.Combobox(root,values=choices)




ytdchoices.grid()

#choice_error
ytdError = Label(root,text ="Error Message",fg="steelblue",font=("Palatino",11))
ytdError.grid()




downloadbtn = Button(root,text="Download",width=12,bg="turquoise",activebackground = 'sky blue',fg="black",command=DownloadVideo)
downloadbtn.grid(column=0, row=10, padx=20, pady=15)


downloadbtn.grid()


root.mainloop()

