import tkinter as tk
import speech_recognition as sr
def parse_voice_command(text):
    text = text.lower()
    text = text.replace("plus", "+")
    text = text.replace("add", "+")
    text = text.replace("minus", "-")
    text = text.replace("subtract", "-")
    text = text.replace("times", "*")
    text = text.replace("multiply", "*")
    text = text.replace("multiply by", "*")
    text = text.replace("divided by", "/")
    text = text.replace("divide", "/")
    text = text.replace("modulus", "%")
    text = text.replace("mod", "%")
    text = text.replace("zero", "0")
    text = text.replace("one", "1")
    text = text.replace("two", "2")
    text = text.replace("three", "3")
    text = text.replace("four", "4")
    text = text.replace("five", "5")
    text = text.replace("six", "6")
    text = text.replace("seven", "7")
    text = text.replace("eight", "8")
    text = text.replace("nine", "9")
    text = text.replace("x", "*")


    cleaned_text = "".join(char for char in text if char in "0123456789+-*/.%")
    return cleaned_text

def process_voice_input():
    global expression
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        display_text.set("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        display_text.set("Recognizing...")
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        
        expression = parse_voice_command(command)
        display_text.set(expression)

        parsed_expression = parse_voice_command(command)
        if parsed_expression:
            try:
                result = eval(parsed_expression)
                display_text.set(result)
                expression = str(result)
            except Exception as e:
                print(f"Could not evaluate math expression: {e}")
                display_text.set("Invalid Math")
                expression = ""

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        display_text.set("Could not understand")
        expression = ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        display_text.set("API Error")
        expression = ""

def calculate(num1, num2, operation):
    if operation == "+":
     return num1 + num2
    elif operation == "-":
       return num1 - num2
    elif operation == "*":
       return num1 * num2
    elif operation == "/":
       return num1 / num2
    elif operation == "%":
       return (num1 / 100) * num2

expression = ""
def on_button_click(value):
    global expression

    if value == "=":
        try:
            result = eval(expression)
            display_text.set(result)
            expression = str(result)
        except ZeroDivisionError:
            display_text.set("ZeroDivisionError")
        except:
            display_text.set("Invalid Input")

    elif value == "C":
        expression = ""
        display_text.set("0")
    elif value in ['+', '-', '*', '/', '%']:
        expression += value
        display_text.set(expression)
        if expression[-2] in ['+', '-', '*', '/', '%']:
            expression = expression[:-2] + value
            display_text.set(expression)
    else:
        expression += value
        display_text.set(expression)
    current_text = display_text.get()
    if current_text == "0":
        display_text.set(value)

window = tk.Tk()
window.title("VOICE-CALCULATOR")
window.geometry("335x524")
display_text = tk.StringVar(value="0")
display = tk.Label(window, textvariable=display_text, font=("Helvetica", 20), anchor="e", bg="darkgreen", fg="orange", padx=10, pady=10)
display.pack(fill=tk.X)

button_frame = tk.Frame(window, bg="darkgreen")
button_frame.pack()
buttons = [
    ['🎤'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C', '(', ')', '%']
    ]
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
       btn = tk.Button(button_frame, text=text, font=("Helvetica", 18), width=5, height=2, command=lambda val=text: on_button_click(val))
       btn.grid(row=i, column=j, padx=2, pady=2)
       if text == '🎤':
           btn.config(command=process_voice_input)
           btn.grid(row=i, column=0, columnspan=4, padx=2, pady=2, sticky='ew')
       else:
           btn.grid(row=i, column=j, padx=2, pady=2)

window.protocol("WM_DELETE_WINDOW", window.destroy)
window.mainloop()












#Terminal UI
#while True:    
#    user_input = input("do a calculations:")
#    parts = user_input.split()
#    if user_input == "exit":
#       print("cya")
#       break
#    try:
#        num1 = int(parts[0])
#        num2 = int(parts[2])
#        operation = parts[1]
#        result = calculate(num1, num2, operation)
#        print("result is:", result)
#    except ZeroDivisionError:
#       print("cannot divide by 0")
#    except:
#       print("wrong input:\n use spaces between numbers and operator\n example:(8 + 3! not 8+3)\n or use strictly numbers:\n 5! not five")