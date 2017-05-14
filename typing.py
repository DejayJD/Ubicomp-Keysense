try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import random, time

FONT = (None, 50)
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']

program_time = time.time()

colors = {"blue":"#626db8", "green": "#008000", "red":"#fc0000"}

char_errors = 0
chars_correct = 0

root = tk.Tk()
root.title("Typing trainer")

text_to_copy = tk.Label(root, text = "start", font=FONT)
text_to_copy.pack()
text_input = tk.Entry(root, font=FONT, background="#ffffff")
text_input.pack()

time_label = tk.Label(root, text = "Time Elapsed: 0", font=FONT)
time_label.pack()

status_bar = tk.Entry(root, font=FONT, background=colors['blue'])
status_bar.pack()

def get_random_words(amount):
    words = ""
    for i in range(amount):
        words += random.choice(WORDS) + " "
    return words

def check_keypress(event):
    global text_input, colors, chars_correct, char_errors
    example_text = text_to_copy.cget("text")
    input_text = text_input.get()
    keypress = event.char
    if (keypress):
        if ord(keypress) == 13:
            text_input.delete(0, 'end')
            text_to_copy['text'] = get_random_words(5)
            changeStatusColor('blue')
        else:
            position = len(input_text) - 1
            if example_text[position] == input_text[-1:]:
                chars_correct += 1
            else:
                char_errors += 1
            if example_text == input_text:
                changeStatusColor('green')
            else:
                changeStatusColor('red')

def updateTime():
    global time
    if time.time() != program_time:
        time_label['text'] = "Score: " + str(int(time_label['text'].split(': ')[-1]) + 1)



def changeStatusColor(color):
    status_bar.config(background=colors[color])

root.bind('<Key>', check_keypress)

root.mainloop()

print "Total Character Errors:" + str(char_errors)
print "Total Correct Characters:" + str(chars_correct)