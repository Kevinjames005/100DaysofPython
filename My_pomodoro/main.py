import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps == 8 :
        count_down(long_break)
        timer_label.config(text="Break" , fg=RED)
    elif reps %2 == 0 :
        count_down(work_min)
        timer_label.config(text="Work", fg=GREEN)
    else :
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10 :
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else :
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=YELLOW)

timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"normal"))
timer_label.grid(row=0,column=1)

canvas = Canvas(width=202,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato_img)
timer_text = canvas.create_text(102,132,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)


start_button= Button(text="Start",command=start_timer)
start_button.grid(row = 2,column=0)

reset_button= Button(text="Reset")
reset_button.grid(row = 2,column=3)

tick_label = Label(text="✓",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"normal"))
tick_label.grid(row=4,column=1)



window.mainloop()