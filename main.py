import tkinter as tk
from tkinter import ttk
import subprocess

def run_proc():
    result = subprocess.run(["./Project-com"], capture_output=True, text=True)
    return result.stdout.strip()

def display_window():
    window = tk.Tk()
    window.geometry("600x400")
    window.title("Test")

    process = run_proc()

    canvas = tk.Canvas(window, bg="#212020", scrollregion = (0,0,2000,5000))
    canvas.pack(expand=True, fill="both")

    frame = tk.Frame(canvas, bg="#212020")
    canvas.create_window((0,0), window=frame, anchor="nw")

    label = ttk.Label(frame, text=process)
    label.grid(sticky="w", padx=15, pady=15)

    scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    window.mainloop()

if __name__ == "__main__":
    display_window()