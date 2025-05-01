import pygame
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.is_playing = False
        self.volume = 0.5  # Default volume level

        # Create a frame for the controls
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=20)

        # Load Music Button
        self.load_button = tk.Button(self.control_frame, text="Load Music", command=self.load_music)
        self.load_button.grid(row=0, column=0, padx=10)

        # Play Button
        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play_music)
        self.play_button.grid(row=0, column=1, padx=10)

        # Stop Button
        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_music)
        self.stop_button.grid(row=0, column=2, padx=10)

        # Volume Label
        self.volume_label = tk.Label(root, text="Volume:")
        self.volume_label.pack(pady=10)

        # Volume Slider
        self.volume_slider = ttk.Scale(root, from_=0, to=1, orient='horizontal', command=self.set_volume, length=300)
        self.volume_slider.set(self.volume)
        self.volume_slider.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(root, text="Status: Not Playing", fg="red")
        self.status_label.pack(pady=10)

        self.music_file = ""

        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)

    def load_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.music_file:
            self.status_label.config(text=f"Loaded: {self.music_file.split('/')[-1]}", fg="blue")
            print(f"Loaded: {self.music_file}")

    def play_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            self.is_playing = True
            self.status_label.config(text="Status: Playing", fg="green")
        else:
            messagebox.showwarning("Warning", "Please load a music file first.")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.status_label.config(text="Status: Stopped", fg="red")

    def set_volume(self, value):
        self.volume = float(value)
        pygame.mixer.music.set_volume(self.volume)

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()