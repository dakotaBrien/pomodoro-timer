import tkinter as t
import os

# constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checks = ""
reps = 0
timer_running = False
stop = True


def start_timer():
    global timer_running
    global checks
    global reps
    global stop
    stop = False
    raise_above_all(window)
    if not timer_running:
        timer_running = True
        check_label.config(text=checks)
        reps += 1
        if reps % 2 == 1:
            count_down(WORK_MIN * 60)
            timer_label.config(text="Work", fg=GREEN)
        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            timer_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            timer_label.config(text="Break", fg=PINK)
    else:
        pass


def count_down(count):
    global timer_running
    global checks
    global stop
    if not stop:
        count_min = round((count / 60) - .49)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            window.after(1000, count_down, count - 1)
        if count == 0:
            if reps % 2 == 1:
                checks += "✔"
            elif reps % 8 == 0:
                checks = ""
            timer_running = False
            start_timer()


def raise_above_all(win):
    win.state('normal')
    win.attributes('-topmost', 1)
    win.attributes('-topmost', 0)


def reset_timer():
    global timer_running
    global checks
    global reps
    global stop
    timer_running = False
    stop = True
    checks = ""
    check_label.config(text="✔")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="")
    reps = 0


window = t.Tk()
window.title("Pomodoro Timer")
window.config(padx=60, pady=40, bg=YELLOW)
icon = t.PhotoImage(file="tomato.png")
window.iconphoto(True, icon)

canvas = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_pic = t.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom_pic)
timer_text = canvas.create_text(100, 130, text="", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = t.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = t.Button(text="Start", padx=9, bg=PINK, fg=YELLOW, font=(FONT_NAME, 10, "bold"), border=0,
                        command=start_timer)
start_button.grid(column=0, row=2)

restart_button = t.Button(text="Reset", padx=9, bg=PINK, fg=YELLOW, font=(FONT_NAME, 10, "bold"), border=0, command=reset_timer)
restart_button.grid(column=2, row=2)

check_label = t.Label(text="✔", font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
