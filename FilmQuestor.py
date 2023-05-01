import tkinter as tk
import tkinter.messagebox as msgbox
from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
        msgbox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        msgbox.showerror("Error", f"An error occurred during download:\n{str(e)}")

root = tk.Tk()
root.title("FilmQuestor")
root.geometry("400x200")
root.config(bg="#41436A")

label = tk.Label(root, text="Enter YouTube Video URL:", font=("Arial", 18), fg="#ffffff", bg="#41436A")
label.pack(pady=10)

url_entry = tk.Entry(root, font=("Arial", 14), width=30)
url_entry.pack(pady=10)

def submit_url():
    url = url_entry.get()
    download_video(url)

submit_button = tk.Button(root, text="Download Video", font=("Arial", 14), fg="#ffffff", bg="#F64688", command=submit_url)
submit_button.pack(pady=10)

def on_enter(e):
    submit_button['background'] = '#984063'

def on_leave(e):
    submit_button['background'] = '#F64688'

submit_button.bind("<Enter>", on_enter)
submit_button.bind("<Leave>", on_leave)

root.mainloop()
