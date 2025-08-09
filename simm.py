import tkinter as tk
import random
root = tk.Tk()
root.title("Simon Says Game")
colors = ['red', 'green', 'blue', 'yellow']
buttons = {}
pattern = []
user_pattern = []
level = 0
waiting = False

def start_game():
    global pattern, user_pattern, level
    pattern = []
    user_pattern = []
    level = 1
    level_label.config(text="Level " + str(level))
    add_to_pattern()
def add_to_pattern():
    global pattern, user_pattern, waiting
    user_pattern = []
    waiting = False
    new_color = random.choice(colors)
    pattern.append(new_color)
    show_pattern()
def show_pattern():
    delay = 500
    for i in range(len(pattern)):
        root.after(i * 700, lambda i=i: flash_button(pattern[i]))
    root.after(len(pattern) * 700, allow_input)
def flash_button(color):
    btn = buttons[color]
    old_color = btn['bg']
    btn.config(bg='white')
    root.after(300, lambda: btn.config(bg=color))

def allow_input():
    global waiting
    waiting = True
def button_click(color):
    global user_pattern, waiting, level
    if not waiting:
        return
    user_pattern.append(color)
    flash_button(color)
    index = len(user_pattern) - 1
    if user_pattern[index] != pattern[index]:
        level_label.config(text="Game Over! Press Start")
        waiting = False
        return
    if len(user_pattern) == len(pattern):
        level += 1
        level_label.config(text="Level " + str(level))
        waiting = False
        root.after(1000, add_to_pattern)
frame = tk.Frame(root)
frame.pack()
for i, color in enumerate(colors):
    btn = tk.Button(frame, bg=color, width=10, height=5, command=lambda c=color: button_click(c))
    btn.grid(row=i//2, column=i%2, padx=10, pady=10)
    buttons[color] = btn
level_label = tk.Label(root, text="Click Start to Play", font=("Arial", 14))
level_label.pack(pady=10)
start_btn = tk.Button(root, text="Start", command=start_game)
start_btn.pack(pady=10)
root.mainloop()
