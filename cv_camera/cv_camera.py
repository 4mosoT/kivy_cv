from kivy.uix.image import Image as imm
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from kivy.app import App
from PIL import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import cv2


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
class Cv_Camera(App):
    def build(self):
        

        self.img1=imm()
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(self.img1)
        button = Button(text = 'Stop Capturing',size_hint= (1, .5),pos_hint={'center_x':.5, 'center_y':.2})
        
       
        
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        #cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)

        
        return layout

    
    def update(self, dt):
        
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("CV2 Image", frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
         
        for rect in faces:
            (x,y,w,h) = rect
       

            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
	
	    
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1
        

if __name__ == '__main__':
    Cv_Camera().run()
    cv2.destroyAllWindows()
