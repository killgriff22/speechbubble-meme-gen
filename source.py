from PIL import Image
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog
import os
root = tk.Tk()
root.title("Speech Bubble gif generator")
#root.geometry("400x400")
CWD = os.getcwd()
#create a file selector for the target image
def file_selector():
    return filedialog.askopenfilename()
def path_selector():
    return  filedialog.askdirectory()
def percent_of(num, per):
    return int(((num/100) * per)//1)
target_image_path = None
output_path = None 

#create a button to select the target image
row0frame = tk.Frame(root)
row0frame.grid(row=0, column=0)
row1frame = tk.Frame(root)
row1frame.grid(row=1, column=0)
row2frame = tk.Frame(root)
row2frame.grid(row=2, column=0)
input_path_label = tk.Label(row0frame, text="No image selected")
output_path_label = tk.Label(row1frame, text="No output path selected")
def select_image():
    global target_image_path
    target_image_path = file_selector()
    input_path_label.config(text=target_image_path.split("/")[-1])
    print(f"Image Path: {target_image_path}")

def select_output_path():
    global output_path
    output_path = path_selector()
    output_path_label.config(text=output_path)
    print(f"Output Path: {output_path}")
def convert():
    if not target_image_path:
        mb.showerror("Error", "No image selected")
        return
    if output_path:
        os.chdir(output_path)
    speechbubble = Image.open("speechbubble.png")
    image_name = target_image_path.split("/")[-1].split(".")[0]
    target_image = Image.open(target_image_path)
    speechbubble = speechbubble.resize((target_image.width, percent_of(target_image.height, 35)))
    target_image.paste(speechbubble, (0, 0), speechbubble)
    target_image.save(f"{image_name}.gif")
    mb.showinfo("Success", "Image converted successfully")
    os.chdir(CWD)
select_image_button = tk.Button(row0frame, text="Select Image", command=select_image)
select_image_button.grid(row=0, column=0)
input_path_label.grid(row=0, column=1)
select_output_path_button = tk.Button(row1frame, text="Select Output Path", command=select_output_path)
select_output_path_button.grid(row=0, column=0)
output_path_label.grid(row=0, column=1)
convert_button = tk.Button(row2frame, text="Convert", command=convert)
convert_button.grid(row=0, column=0)
root.mainloop()