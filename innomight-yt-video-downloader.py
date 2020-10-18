from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

# Module Level Variables
folder_location = ""


# Function to Open Files
def open_location():
    global folder_location
    folder_location = filedialog.askdirectory()
    if len(folder_location) > 1:
        ytd_location_error.config(text=folder_location, fg="green")
    else:
        ytd_location_error.config(text="Please Choose a Valid Location", fg="red")


# Function to Download Video
def video_downloader():
    quality = ytd_choices_var.get()
    url = ytd_entry.get()

    if len(url) > 1:
        ytd_error.config(text="")
        yt = YouTube(url)
        if quality == choices[0]:
            select = yt.streams.filter(progressive=True).first()

        elif quality == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif quality == choices[2]:
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytd_error.config(text="Check and Enter Link Again", fg="red")

    select.download(folder_location)
    ytd_error.config(text="Download Completed")


root = Tk()
root.title("Innomight YT Video Downloader")
root.geometry("400x450")

# Center The Content
root.columnconfigure(0, weight=1)

# Heading Label
ytd_label = Label(root, text="Innomight YT Video Downloader\n", font=("Agency-FB", 15))
ytd_label.grid()

# Enter URL Label
ytd_enter_url_label = Label(root, text="Enter URL:", font=("Agency-FB", 15))
ytd_enter_url_label.grid()

# Input Box
ytd_entry_var = StringVar()
ytd_entry = Entry(root, width=50, textvariable=ytd_entry_var)
ytd_entry.grid()

# Error Message
ytd_error = Label(root, text="\n", fg="red", font=("Agency-FB", 15))
ytd_error.grid()

# Add File Save Label
ytd_save_file_label = Label(root, text="Save The Video File", font=("Agency-FB",15))
ytd_save_file_label.grid()

# Save Button
ytd_save_button = Button(root, width=15, fg="white", bg="red", text="Choose File Path", command=open_location)
ytd_save_button.grid()

# Location Error
ytd_location_error = Label(root, text="Location Error\n", fg="red", font=("Agency-FB", 10))
ytd_location_error.grid()

# Download Quality Label
ytd_download_quality_label = Label(root, text="Select Download Quality", font=("Agency-FB", 15))
ytd_download_quality_label.grid()

# Quality List
choices = ["720p", "144p", "Audio Only (.mp3)"]
ytd_choices_var = ttk.Combobox(root, values=choices)
ytd_choices_var.grid()

# Download Button
ytd_download_button = Button(root, width=10, fg="white", bg="red", text="Download", command=video_downloader)
ytd_download_button.grid()

root.mainloop()


