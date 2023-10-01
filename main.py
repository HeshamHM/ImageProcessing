import numpy as np
import cv2
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
class Images:
    images=None
    imrest=None
class Operation:
    class Smoothing:
        def mean(image):
            im = image.copy()
            x, y = np.shape(image)
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    value = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            value = (value + (image[r + i][c + j]))
                    im.itemset((r, c), value / 9)
            return (im)
        def gaussian(image):
            im = image.copy()
            x, y = np.shape(image)
            list1 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    value = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            value = (value + (image[r + i][c + j] * list1[i][j]))
                    im.itemset((r, c), value / 16)
            return (im)
    class Edge_enhanching:
        def prewitt(image):
            im = image.copy()
            list1 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
            x, y = np.shape(image)
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    value = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            value = (value + (image[r + i][c + j] * list1[i][j]))
                    im.itemset((r, c), value / 9)
            return (im)
        def sobel(image):
            im = image.copy()
            list1 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
            x, y = np.shape(image)
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    value = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            value = (value + (image[r + i][c + j] * list1[i][j]))
                    im.itemset((r, c), value / 9)

            return (im)
        def laplace(image):
            im = image.copy()
            list1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
            x, y = np.shape(image)
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    value = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            value = (value + (image[r + i][c + j] * list1[i][j]))
                    im[r][c] = (value) * (1 / 9)
            return im
    class Non_linear:
        def min(image):
            x, y = np.shape(image)
            im = np.zeros((x, y))
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    list = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            list.append(image[r + i][c + j])
                    im[r][c] = np.min(list)
            im = Operation.im2double(im)
            return im
        def max(image):
            x, y = np.shape(image)
            im = np.zeros((x, y))
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    list = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            list.append(image[r + i][c + j])
                    im[r][c] = np.max(list)
            im = Operation.im2double(im)
            return im
        def median(image):
            x, y = np.shape(image)
            im = np.zeros((x, y))
            for r in range(1, x - 1):
                for c in range(1, y - 1):
                    list = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            list.append(image[r + i][c + j])
                    im[r][c] = np.median(list)
            im = Operation.im2double(im)
            return im
    def im2double(im):
        max_val = np.max(im)
        min_val = np.min(im)
        return np.round((im.astype('float') - min_val) / (max_val - min_val)*255)
    def increase_contrast(image):
        im=image.copy()
        im=Operation.im2double(im)
        im=im*2
        return im
    def decrease_contrast(image):
        im=image.copy()
        im=Operation.im2double(im)
        im=im/2
        return im
    def intensity_slicing(image):
        im=image.copy()
        x, y = np.shape(image)
        m=np.mean(image)
        for i in range(0, x ):
            for j in range(0, y):
             if im[i][j]<m:
                 im[i][j]=0
             else:
                 im[i][j] =255
        return im
    def negtive(image):
        im=image.copy()
        x,y=np.shape(image)
        return 255-im
    def histo(image):
        im=image.copy()
        rk,nk=np.unique(im,return_counts=True)
        pk=nk/im.size
        sk=np.cumsum(pk)*np.max(im)
        val=np.round(sk)
        for i in range(len(image)):
            for j in range(len(image[0])):
                im[i][j] = val[np.where(rk == image[i][j])]
        return im
    def log(image):
        im=image.copy()
        c = 255 / np.log(1 + np.max(im))
        return np.array(c * (np.log(im + 1)), dtype=np.uint8)
    def power_law(image):
        img=image.copy()
        img = np.array(255 * (img /255) **0.5, dtype='uint8')
        return img
root = tk.Tk()
canv = tk.Canvas(root, width=700, height=700)
canv.place(x=350, y=40)
def select_file():
        canv.delete()
        im = filedialog.askopenfile(title='Please select one (any) frame from your set of images.',
                                    filetypes=[('Image Files', ['.jpeg', '.jpg', '.png'])])
        global test
        global im2
        im2 = cv2.imread(im.name, 0)
        image = Image.fromarray(im2)
        test = ImageTk.PhotoImage(image)
        canv.create_image(50, 10, anchor=tk.NW, image=test)
        # canv.itemconfigure(img, state=tk.NORMAL)
        # Position image
        showinfo(
            title='Selected File',
            message=im.name
        )
        Images.images=im2
        Images.imrest=Images.images.copy()
def update_image(im):
    canv.delete('all')
    global test
    global image
    image = Image.fromarray(im)
    test = ImageTk.PhotoImage(image)
    canv.create_image(50, 10, anchor=tk.NW, image=test)
    # Position image
    showinfo(
        title='Done',
        message="Updated"
    )
    Images.images = im.copy()
root.title("Image Processing")
root.geometry("1000x905")
root.resizable(0, 0)
def move_window(event,root):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
root.overrideredirect(True)
title_bar = tk.Frame(root, height="30", width="1000", bg="darkred", relief='raised', bd=2).place(x=0, y=0)
close_button = tk.Button(title_bar, bg="darkred", text='X', command=root.destroy, fg='#ffffff', heigh=1, width=4)
close_button.place(x=960, y=0)
frame = tk.Frame(root, height="900", width="340", bg="darkred").place(x=0, y=0)
myFont = font.Font(size=15)
images = np.zeros((3, 3))
buttonMean = tk.Button(frame, text="Mean", width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda: update_image(Operation.Smoothing.mean(Images.images)))
buttonMean.place(x=0, y=0)
buttongaussian = tk.Button(frame, text="Gaussian", width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda: update_image(Operation.Smoothing.gaussian(Images.images)))
buttongaussian.place(x=0, y=60)
buttongaussian['font'] = myFont
buttonMean['font'] = myFont
buttonprewitt = tk.Button(frame,text="Prewitt",width=30, heigh=2, bg="darkred", fg='#ffffff' ,command=lambda :update_image(Operation.Edge_enhanching.prewitt(Images.images)))
buttonprewitt.place(x=0, y=120)
buttonprewitt['font'] = myFont
buttonsobel = tk.Button(text="Sobel",width=30, heigh=2, bg="darkred", fg='#ffffff' ,command=lambda: update_image(Operation.Edge_enhanching.sobel(Images.images)))
buttonsobel.place(x=0, y=180)
buttonsobel ['font'] = myFont
buttonlaplace = tk.Button(frame, text="Laplace", width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda: update_image(Operation.Edge_enhanching.laplace(Images.images)))
buttonlaplace.place(x=0, y=240)
buttonlaplace['font'] = myFont
buttonMin =  tk.Button(frame,text="Min",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.Non_linear.min(Images.images)))
buttonMin.place(x=0, y=300)
buttonMin['font'] = myFont
buttonMax =tk.Button(frame,text="Max",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.Non_linear.max(Images.images)))
buttonMax.place(x=0, y=360)
buttonMax['font'] = myFont
buttonMedian = tk.Button(frame,text="Median",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.Non_linear.median(Images.images)))
buttonMedian.place(x=0, y=420)
buttonMedian['font'] = myFont
buttonLog =tk.Button(frame,text="Log",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.log(Images.images)))
buttonLog.place(x=0, y=480)
buttonLog['font'] = myFont
buttonincrease_contrast = tk.Button(frame,text="Increase Contrast",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.increase_contrast(Images.images)))
buttonincrease_contrast.place(x=0, y=540)
buttonincrease_contrast['font'] = myFont
buttondecrease_contrast = tk.Button(frame,text="Decrease Contrast",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.decrease_contrast(Images.images)))
buttondecrease_contrast.place(x=0, y=600)
buttondecrease_contrast['font'] = myFont
buttonintensity = tk.Button(frame,text="Intensity Slicing ",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.intensity_slicing(Images.images)))
buttonintensity.place(x=0, y=660)
buttonintensity['font'] = myFont
buttonnegtive =tk.Button(frame,text="Negtive",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.negtive(Images.images)))
buttonnegtive.place(x=0, y=720)
buttonnegtive['font'] = myFont
buttonHist =tk.Button(frame,text="Histograme",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.histo(Images.images)))
buttonHist.place(x=0, y=780)
buttonHist['font']=myFont
buttonPower_law =tk.Button(frame,text="Power Law",width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda:update_image(Operation.power_law(Images.images)))
buttonPower_law.place(x=0, y=840)
buttonPower_law['font']=myFont
buttonBrowes = tk.Button(root, text="Browes", width=30, heigh=2, bg="darkred", fg='#ffffff',command=lambda: select_file())
buttonBrowes.place(x=450, y=800)
buttonrest= tk.Button(root, text="Rest", width=20, heigh=2, bg="darkred", fg='#ffffff',command=lambda: update_image(Images.imrest))
buttonrest.place(x=800, y=800)
buttonBrowes['font'] = myFont
buttonrest['font'] = font.Font(size=10)
root.mainloop()