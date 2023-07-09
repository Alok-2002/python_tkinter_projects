from tkinter import *
import math
import os
import pygame


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

reps = 0
timer = None
is_paused = False
remaining_time = 0


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00:00")
    canvas.itemconfig(progress_bar, fill="green")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps, is_paused, remaining_time
    reps = 0
    is_paused = False
    remaining_time = 0
    pause_button.config(text="Pause")


def start_timer():
    global reps, remaining_time
    reps += 1

    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())

    count = hours * 3600 + minutes * 60 + seconds

    if remaining_time > 0:
        count_down(remaining_time)
        title_label.config(text="Work", fg=GREEN)
        remaining_time = 0
    elif count > 0:
        count_down(count)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):
    global timer, is_paused, remaining_time

    if is_paused:
        remaining_time = count
        return

    count_hours = math.floor(count / 3600)
    count_min = math.floor((count % 3600) / 60)
    count_sec = (count % 3600) % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_hours:02d}:{count_min:02d}:{count_sec}")

    elapsed_time = int(hours_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get()) - count
    progress = elapsed_time / (int(hours_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get()))
    canvas.itemconfig(progress_bar, fill=GREEN)
    canvas.coords(progress_bar, (0, 0, canvas_width * progress, 30))

    if count > 0:
        if count % 60 == 0:
            play_tick_sound()
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        play_finish_sound()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


def pause_timer():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")
        start_timer()


def play_tick_sound():
    pygame.mixer.music.load(resource_path("./assets/tick.wav"))
    pygame.mixer.music.play()


def play_finish_sound():
    pygame.mixer.music.load(resource_path("./assets/finish.wav"))
    pygame.mixer.music.play()


window = Tk()
window.title("TimerZen")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas_width = 300
canvas_height = 224
canvas = Canvas(width=canvas_width, height=canvas_height, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("./assets/tomato.png"))
image_x = canvas_width // 2
image_y = canvas_height // 2
canvas.create_image(image_x, image_y, image=tomato_img)
timer_text = canvas.create_text(image_x, image_y + 20, text="00:00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

hours_label = Label(text="Hours", fg="black", bg=YELLOW)
hours_label.grid(column=0, row=2)
hours_entry = Entry(width=10, justify="center")
hours_entry.grid(column=0, row=3)

minutes_label = Label(text="Minutes", fg="black", bg=YELLOW)
minutes_label.grid(column=1, row=2)
minutes_entry = Entry(width=10, justify="center")
minutes_entry.grid(column=1, row=3)

seconds_label = Label(text="Seconds", fg="black", bg=YELLOW)
seconds_label.grid(column=2, row=2)
seconds_entry = Entry(width=10, justify="center")
seconds_entry.grid(column=2, row=3)

start_button = Button(text="Start", highlightthickness=0,width=10 ,pady=5 , command=start_timer)
start_button.grid(column=0, row=4)

pause_button = Button(text="Pause", highlightthickness=0,pady=5 ,width=10, command=pause_timer)
pause_button.grid(column=1, row=4)

reset_button = Button(text="Reset", highlightthickness=0,pady=5 ,width=10, command=reset_timer)
reset_button.grid(column=2, row=4)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=7)

progress_bar = canvas.create_rectangle(0, 0, 0, 30, fill=GREEN)

pygame.mixer.init()

window.mainloop()
