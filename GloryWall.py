
import tkinter
from tkinter import *
from random import choice
import sys
import cv2
import numpy as np
import time
import mediapipe as mp
# ---------------------------------------------------basicos ---------------------------------------------------------------
global x
global na
global nt
nt = 0
x = 0
na = 0
#-----------------------------Ventana-----------------------------------------------------------------------------------------------
ventana = tkinter.Tk()
ventana.geometry("1400x700")
ventana.title("Glory Wall")
ventana.configure(bg='#C3FBFF')
ventana.resizable(False,False)

etiqueta = tkinter.Label(ventana, text = "GloryWall", font = "Helvetica 80")
etiqueta.pack()
etiqueta.place( x=500, y = 10)
etiqueta.configure(bg='#C3FBFF')

etiquetaw = tkinter.Label(ventana, text = "Score:", font = "Helvetica 50")
etiquetaw.pack()
etiquetaw.place( x=50, y = 200)
etiquetaw.configure(bg='#C3FBFF')

etiquetawa = tkinter.Label(ventana, text = "presiona q para empezar el timer y esc para cerrar la camara", font = "Helvetica 20")
etiquetawa.pack()
etiquetawa.place( x=50, y = 600)
etiquetawa.configure(bg='#C3FBFF')


#------------funciones niveles -----------------------------------------------------------------------------------------

def nivel1():
    global na
    imgg = cv2.imread('images/Silueta.png')
    na = 1
    proceso(imgg, na)
    
    
def nivel2():
    global na
    imgg = cv2.imread('images/cross.png')
    na = 2
    proceso(imgg,na)
    
    
def nivel3():
    global na
    imgg = cv2.imread('images/armsup.png')
    na = 3
    proceso(imgg,na)
    
    
def nivel4():
    global na
    imgg = cv2.imread('images/soldier.png')
    na = 4
    proceso(imgg,na)
    
        
def nivel5():
    global na
    imgg = cv2.imread('images/freddy.png')
    na = 5
    proceso(imgg,na)
    
    
def nivel6():
    global na
    imgg = cv2.imread('images/walk.png')
    na = 6
    proceso(imgg,na)
    
    
def nivel7():
    global na
    imgg = cv2.imread('images/weird.png')
    na = 7
    proceso(imgg,na)
    
    
def nivel8():
    global na
    imgg = cv2.imread('images/jump.png')
    na = 8
    proceso(imgg,na)
    
    
def nivel9():
    global na
    imgg = cv2.imread('images/hard.png')
    na = 9
    proceso(imgg,na)
    
    
def nivel10():
    global na
    imgg = cv2.imread('images/impossible.png')
    na = 10
    proceso(imgg,na)
    



#------------------------------------------------------------ cerebro ----------------------------------------------------------


def proceso(imgg,na):

    

    # Best contour machining -----------------------------------------------------------
    img1 = imgg
    cv2.imshow('Pose', imgg)
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    # Video de entrada
    cap = cv2.VideoCapture( cv2.CAP_DSHOW)
    # Video que se ubica en el fondo
    video_name = "video.extensión"
    cap2 = cv2.VideoCapture(video_name)
    # Boomerang reference image silueta a buscar
    
    TIMER = int(10)
    BG_COLOR = (219, 203, 255)
    def filtro(img):
        ret2, bg_image = cap2.read()
        # Transformar los fotogramas de BGR a RGB y
        # aplicación de MediaPipe Selfie Segmentation
        frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = selfie_segmentation.process(frame_rgb)
        # Obtener imagen binaria
        _, th = cv2.threshold(results.segmentation_mask, 0.75, 255, cv2.THRESH_BINARY)
        # Cambio de tipo de dato para poder usarlo con OpenCV
        # e invertir la máscara
        th = th.astype(np.uint8)
        th = cv2.medianBlur(th, 13)
        th_inv = cv2.bitwise_not(th)
        # Background
        bg_image = np.ones(img.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        #bg_image = cv2.imread("image_0001.jpg")
        #bg_image = cv2.GaussianBlur(bg_image, (15, 15), 0)
        bg = cv2.bitwise_and(bg_image, bg_image, mask=th_inv)
        # Foreground
        fg = cv2.bitwise_and(img, img, mask=th)
        # Background + Foreground
        return cv2.add(bg, fg)
        
        
    with mp_selfie_segmentation.SelfieSegmentation(
         model_selection=1) as selfie_segmentation:
        while True:
        	
           	# Read and display each frame
           	ret, img = cap.read()
           	output_image = filtro(img)
           	cv2.imshow('a', output_image)
       
           	# check for the key pressed
           	k = cv2.waitKey(125)
           
           	# set the key for the countdown
           	# to begin. Here we set q
           	# if key pressed is q
           	if k == ord('q'):
           		prev = time.time()
    
           		while TIMER >= 0:
           			ret, img = cap.read()
           			output_image = filtro(img)
           			# Display countdown on each frame
           			# specify the font and draw the
           			# countdown using puttext
           			font = cv2.FONT_HERSHEY_SIMPLEX
           			cv2.putText(output_image, str(TIMER),
           						(200, 250), font,
           						7, (0, 255, 255),
           						4, cv2.LINE_AA)
                    
           			cv2.imshow('a', output_image)
           			cv2.waitKey(125)
           
           			# current time
           			cur = time.time()
           
           			# Update and keep track of Countdown
           			# if time elapsed is one second
           			# than decrease the counter
           			if cur-prev >= 1:
           				prev = cur
           				TIMER = TIMER-1
           
           		else:
           			ret, img = cap.read()
           			output_image = filtro(img)
           
           			# Display the clicked frame for 2
           			# sec.You can increase time in
           			# waitKey also
           			cv2.imshow('a', output_image)
                       
           
           			# time for which image displayed
           			cv2.waitKey(2000)
           
           			# Save the frame
           			cv2.imwrite('images/output.png', output_image, [cv2.IMWRITE_PNG_COMPRESSION])
           
           			# HERE we can reset the Countdown timer
           			# if we want more Capture without closing
           			# the camera
            
            	# Press Esc to exit
           	elif k == 27:
           		break
    
    # close the camera
    cap.release()
    cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    # Extract all the contours from the image
    def get_all_contours(img):
        ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours
    
    
    # Extract reference contour from the image
    def get_ref_contour(img):
        contours = get_all_contours(img)
    
        for contour in contours:
            area = cv2.contourArea(contour)
            img_area = img.shape[0] * img.shape[1]
            if 0.05 < area / float(img_area) < 0.8:
                return contour
    
    
    

    # Input image containing all the different shapes
    img2 = cv2.imread('images/output.png')
    
    # Extract the reference contour
    ref_contour = get_ref_contour(img1)
    
    # Extract all the contours from the input image
    
    input_contours = get_all_contours(img2)
    
    closest_contour = None
    min_dist = None
    contour_img = img2.copy()
    cv2.drawContours(contour_img, input_contours, -1, color=(0, 0, 255), thickness=3) # rojo
    #cv2.imshow('Contours', contour_img) # borrar esto ----------------------------------------------///////////////////////
    # Finding the closest contour
    for i, contour in enumerate(input_contours):
        # Matching the shapes and taking the closest one using
        # Comparison method CV_CONTOURS_MATCH_I3 (second argument)
    
        ret = cv2.matchShapes(ref_contour, contour, 3, 0.0)
        print("Contour %d matchs in %f" % (i, ret))
        if min_dist is None or ret < min_dist:
    
            min_dist = ret
            closest_contour = contour
    print (len(closest_contour))
    x =(len(closest_contour))
    cv2.drawContours(img2, [closest_contour], 0, color=(0, 255, 0), thickness=3)  #verde
    #cv2.imshow('Best Matching', img2) # borrar esto ----------------------------------------------///////////////////////
    print ('coincidencia: ', x)
    ifsdeniveles(x,na)
    waitKey()
    cv2.destroyAllWindows()

#----------- ifs de niveles ------------------------------------------------

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0


def ifsdeniveles(x,na):
    global nt
    # ------1------
    if na ==1:
        if x > 100:
            n1 = 10
            print('nivel 1: ', n1)
            nt = nt + n1
        elif x < 100:
            n1 = 0
            print('nivel 1: ', n1)
            nt = nt + n1
        

    # ------2------
    if na ==2:
        if x > 100:
            n2 = 10
            print('nivel 2: ', n2)
            nt = nt + n2
        elif x < 100:
            n2 = 0
            print('nivel 2: ', n2)
            nt = nt + n2


    # ------3------
    if na ==3:
        if x > 200:
            n3 = 10
            print('nivel 3: ', n3)
            nt = nt + n3
        elif x < 200:
            n3 = 0
            print('nivel 3: ', n3)
            nt = nt + n3


        # ------4------
    if na ==4:
        if x > 100:
            n4 = 10
            print('nivel 4: ', n4)
            nt = nt + n4
        elif x < 100:
            n4 = 0
            print('nivel 4: ', n4)
            nt = nt + n4
    
    
        # ------5------
    if na ==5:
        if x > 200:
            n5 = 10
            print('nivel 5: ', n5)
            nt = nt + n5
        elif x < 200:
            n5 = 0
            print('nivel 5: ', n5)
            nt = nt + n5
    
    
        # ------6------
    if na ==6:
        if x > 200:
            n6 = 10
            print('nivel 6: ', n6)
            nt = nt + n6
        elif x < 200:
            n6 = 0
            print('nivel 6: ', n6)
            nt = nt + n6
    
        # ------7------
    if na ==7:
        if x > 100:
            n7 = 10
            print('nivel 7: ', n7)
            nt = nt + n7
        elif x < 100:
            n7 = 0
            print('nivel 7: ', n7)
            nt = nt + n7
    
    
        # ------8------
    if na ==8:
        if x > 200:
            n8 = 10
            print('nivel 8: ', n8)
            nt = nt + n8
        elif x < 200:
            n8 = 0
            print('nivel 8: ', n8)
            nt = nt + n8
    
    
        # ------9------
    if na ==9:
        if x > 200:
            n9 = 10
            print('nivel 9: ', n9)
            nt = nt + n9
        elif x < 200:
            n9 = 0
            print('nivel 9: ', n9)
            nt = nt + n9
    
    
        # ------10------
    if na ==10:
        if x > 300:
            n10 = 10
            print('nivel 10: ', n10)
            nt = nt + n10
        elif x < 300:
            n10 = 0
            print('nivel 10: ', n10)
            nt = nt + n10
    
    print('total: ', nt)
    etiquetawe = tkinter.Label(ventana, text = nt, font = "Helvetica 45")
    etiquetawe.pack()
    etiquetawe.place( x=350, y = 208)
    etiquetawe.configure(bg='#C3FBFF')

#---------------------------------------------INTERFAZ--------------------------------------------------------------------------




#------pantalla mini niveles---------------------------------------------


canvaslevel = Canvas(ventana, width = 500, height = 500, bg= '#FFA448')#pantalla tutorial
canvaslevel.pack()
canvaslevel.place( x=850, y = 150) 

canvaslevel2 = Canvas(ventana, width = 480, height = 480, bg= '#FFF867')#pantalla tutorial
canvaslevel2.pack()
canvaslevel2.place( x=860, y = 160) 

etiquetale = tkinter.Label(ventana, text = "Niveles", font = "Helvetica 40", fg = 'white', bd = 2)
etiquetale.pack()
etiquetale.place( x=1010, y = 140)
etiquetale.configure(bg='#FFA448')



#----- Niveles ------------------

botonc1 = tkinter.Button(ventana, text = "1", padx = 10, pady = 7, command= nivel1, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc1.pack()    
botonc1.place( x=900, y = 250)

botonc2 = tkinter.Button(ventana, text = "2", padx = 10, pady = 7, command= nivel2, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc2.pack()    
botonc2.place( x=1050, y = 250)

botonc3 = tkinter.Button(ventana, text = "3", padx = 10, pady = 7, command= nivel3, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc3.pack()    
botonc3.place( x=1200, y = 250)

botonc4 = tkinter.Button(ventana, text = "4", padx = 10, pady = 7, command= nivel4, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc4.pack()    
botonc4.place( x=900, y = 350)

botonc5 = tkinter.Button(ventana, text = "5", padx = 10, pady = 7, command= nivel5, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc5.pack()    
botonc5.place( x=1050, y = 350)

botonc6 = tkinter.Button(ventana, text = "6", padx = 10, pady = 7, command= nivel6, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc6.pack()    
botonc6.place( x=1200, y = 350)

botonc7 = tkinter.Button(ventana, text = "7", padx = 10, pady = 7, command= nivel7, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc7.pack()    
botonc7.place( x=900, y = 450)

botonc8 = tkinter.Button(ventana, text = "8", padx = 10, pady = 7, command= nivel8, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc8.pack()    
botonc8.place( x=1050, y = 450)

botonc9 = tkinter.Button(ventana, text = "9", padx = 10, pady = 7, command= nivel9, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc9.pack()    
botonc9.place( x=1200, y = 450)

botonc10 = tkinter.Button(ventana, text = "10", padx = 10, pady = 7, command= nivel10, font = "Arial 20", bg = '#FFBC2C', fg = 'white')
botonc10.pack()    
botonc10.place( x=900, y = 550)

#-------------------------Funciones--------------------------------------------------------------------------------------------

#------------Funciones de destruccion de pantallas----------------------------
def pantalla1(): 
   canvasp.destroy()


def pantalla2(): 
   canvas2.destroy()

#------------------------------------------CANVAS------------------------------------------------------------------------------


#-------------------------------------------tutorial--------------------------------------------------------------------------
canvas2 = Canvas(ventana, width = 1400, height = 700, bg= '#CEEFF1')#pantalla tutorial
canvas2.pack()
canvas2.place( x=0, y = 0) 

boton2 = tkinter.Button(canvas2, text = "siguiente", padx = 20, pady = 5, command= pantalla2, font = "Arial 20")
boton2.pack()    
boton2.place( x=600, y = 600)

imgpantalla2 = PhotoImage(file = 'tutorialimg.png')
canvas2.create_image(100,100, image = imgpantalla2, anchor=NW)

etiqueta2 = tkinter.Label(canvas2, text = "Y como se juega?", font = "Helvetica 60")
etiqueta2.pack()
etiqueta2.place( x=500, y = 100)
etiqueta2.configure(bg='#CEEFF1')

etiquetat2 = tkinter.Label(canvas2, text = "Viendo a la camara, deberás ver la forma mostrada,", font = "Helvetica 20")
etiquetat2.pack()
etiquetat2.place( x=600, y = 250)
etiquetat2.configure(bg='#FDFFE2')

etiquetat3 = tkinter.Label(canvas2, text = "y tomar esa forma moviendo tu cuerpo para", font = "Helvetica 20")
etiquetat3.pack()
etiquetat3.place( x=600, y = 300)
etiquetat3.configure(bg='#FDFFE2')


etiquetat4 = tkinter.Label(canvas2, text = "imitar figura lo mejor posible.", font = "Helvetica 20")
etiquetat4.pack()
etiquetat4.place( x=600, y = 350)
etiquetat4.configure(bg='#FDFFE2')

etiquetat5 = tkinter.Label(canvas2, text = "Si no lo logras a tiempo, perderás!! RECUERDA EL TIEMPO!", font = "Helvetica 20")
etiquetat5.pack()
etiquetat5.place( x=600, y = 450)
etiquetat5.configure(bg='#FFEBE2')





# -----------------------------------------CANVAS PRINCIPAL --------------------------------------------------------
canvasp = Canvas(ventana, width = 1400, height = 700, bg= '#CEEFF1')#pantalla principal
canvasp.pack()
canvasp.place( x=0, y = 0) 

imgpantalla1 = PhotoImage(file = 'img1.png')
canvasp.create_image(100,100, image = imgpantalla1, anchor=NW)

botonp = tkinter.Button(canvasp, text = "Empezar", padx = 30, pady = 5, command= pantalla1, font = "Arial 30")
botonp.pack()    
botonp.place( x=700, y = 300)

etiquetaa = tkinter.Label(canvasp, text = "GloryWall", font = "Helvetica 80")
etiquetaa.pack()
etiquetaa.place( x=500, y = 10)
etiquetaa.configure(bg='#CEEFF1')



















ventana.mainloop()