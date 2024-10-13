from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
import requests
import webbrowser
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image,AsyncImage
from kivy.animation import Animation
from kivy.clock import Clock
kv='''
Manager:
    Fir:
    Sec:
                              
                                
<Fir>:
    name:'s1'
    id:sc1
    MDTextFieldRect: 
        id:tf1    
        size_hint:1,0.1
        pos_hint:{'center_y':0.83}
        multiline:True
        input_filter:'float'
        
        
        
    MDFloatingActionButton:
        id:b1
        pos_hint:{'center_x':0.1,'center_y':0.7}
        on_press:
            app.add('1')            
        MDTextButton:
            text:'1'
            size_hint:0,0     
           
    MDFloatingActionButton:
        id:b2
        pos_hint:{'center_x':0.3,'center_y':0.7}
        on_press:
            app.add('2')
        MDTextButton:
            text:'2'  
            size_hint:0,0                    
            
    MDFloatingActionButton:
        id:b3
        pos_hint:{'center_x':0.5,'center_y':0.7}
        on_press:
            app.add('3')  
        MDTextButton:
            text:'3'    
            size_hint:0,0          
        
    MDFloatingActionButton:
        id:b4
        pos_hint:{'center_x':0.7,'center_y':0.7}
        on_press:
            app.add('4')            
        MDTextButton:
            text:'4' 
            size_hint:0,0             
        
    MDFloatingActionButton:
        id:b÷
        pos_hint:{'center_x':0.9,'center_y':0.7}
        md_bg_color:0,0,1,1
        on_press:
            app.add('/')           
        MDTextButton:
            text:'÷'      
            size_hint:0,0           
            color:1,1,1,1
    
    MDFloatingActionButton:
        id:b5
        pos_hint:{'center_x':0.1,'center_y':0.6}
        on_press:
            app.add('5')            
        MDTextButton:
            text:'5'  
            size_hint:0,0
             
    MDFloatingActionButton:
        id:b6
        pos_hint:{'center_x':0.3,'center_y':0.6}
        on_press:
            app.add('6')            
        MDTextButton:
            text:'6'          
            size_hint:0,0
                     
    MDFloatingActionButton:
        id:bc
        pos_hint:{'center_x':0.6,'center_y':0.6}
        size_hint:0.3,0.07     
        md_bg_color:0,1,0,1
        on_press:
            app.remove()
        MDTextButton:
            text:'C'               
            color:1,0,0,1        
            size_hint:0,0
            
    MDFloatingActionButton:
        id:bX
        pos_hint:{'center_x':0.9,'center_y':0.6}
        md_bg_color:0,0,1,1
        on_press:
            app.add('*')           
        MDTextButton:
            text:'X'      
            size_hint:0,0           
            color:1,1,1,1                        

    MDFloatingActionButton:
        id:b7
        pos_hint:{'center_x':0.1,'center_y':0.5}
        on_press:
            app.add('7')            
        MDTextButton:
            text:'7'          
            size_hint:0,0

    MDFloatingActionButton:
        id:b8
        pos_hint:{'center_x':0.3,'center_y':0.5}
        on_press:
            app.add('8')            
        MDTextButton:
            text:'8'          
            size_hint:0,0
            
    MDFloatingActionButton:
        id:b9
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:
            app.add('9')            
        MDTextButton:
            text:'9'          
            size_hint:0,0
            
    MDFloatingActionButton:
        id:b.
        pos_hint:{'center_x':0.7,'center_y':0.5}
        md_bg_color:0,1,0,1
        on_press:
            app.add('.')            
        MDIconButton:
            icon:'circle'          
            size_hint:0,0
            color:1,0,0,1

            
    MDFloatingActionButton:
        id:b+
        pos_hint:{'center_x':0.9,'center_y':0.5}
        md_bg_color:0,0,1,1
        on_press:
            app.add('+')           
        MDTextButton:
            text:'+'      
            size_hint:0,0           
            color:1,1,1,1   

    MDFloatingActionButton:
        id:b-
        pos_hint:{'center_x':0.9,'center_y':0.4}
        md_bg_color:0,0,1,1
        on_press:
            app.add('-')           
        MDTextButton:
            text:'-'      
            size_hint:0,0           
            color:1,1,1,1   

    MDFloatingActionButton:
        id:b0
        pos_hint:{'center_x':0.1,'center_y':0.4}
        on_press:
            app.add('0')  
        MDTextButton:
            text:'0'          
            size_hint:0,0
            
    MDFloatingActionButton:
        id:bks
        pos_hint:{'center_x':0.7,'center_y':0.3}
        size_hint:0.5,0.07     
        md_bg_color:0,1,0,1
        on_press:
            app.bk()
        MDIconButton:
            icon:'keyboard-backspace'               
            color:1,0,0,1        
            size_hint:0,0            

    MDFloatingActionButton:
        id:sol
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:0.6,0.07     
        md_bg_color:1,0,0,1
        on_press:
            app.solve()
        MDTextButton:
            text:'='               
            color:1,1,1,1       
            size_hint:0,0            

    MDFloatingActionButton:
        id:bh
        pos_hint:{'center_x':0.2,'center_y':0.3}
        size_hint:0.3,0.07
        on_press:
            app.thank()  
        MDTextButton:
            text:'HELLO'          
            size_hint:0,0 

    MDFloatingActionButton:
        id:ps
        pos_hint:{'center_x':0.5,'center_y':0.2}
        size_hint:1,0.07
        on_press:
            app.bg()
        MDTextButton:
            text:'PRINT SAME '          
            size_hint:0,0 

    MDFloatingActionButton:
        id:ns
        pos_hint:{'center_x':0.5,'center_y':0.1}
        size_hint:1,0.07
        on_press:
            app.root.current='s2'
            app.root.transition.direction='left'
        MDTextButton:
            text:'BMI CALCULATOR'          
            size_hint:0,0 
    




















    MDTopAppBar:
        id:ta1
        md_bg_color:1,0,0,1
        size_hint:1,0.1
        pos_hint:{'top':1}
        title:'CALCULATOR'
        left_action_items:[['menu',lambda x: nd1.set_state('open')]]        
        right_action_items:[['calculator',lambda x: app.solve()]]
        

                

                


                                                                           
   
    MDNavigationDrawer:
        id:nd1       
        MDCard:
            id:mdc1
            pos_hint:{'top':1}
            size_hint:1,0.3
            FitImage:
                source:'assests/pres.png'                                                                                 
                            

                                                        

<Sec>:
    name:'s2'
    id:sc2     
    Image:
        source:'assests/bmi.png'
        size_hint:0.3,0.3
        pos_hint:{'center_x':0.5,'center_y':0.9}
   
    MDTextField:      
        id:tfr1
        input_filter:'float'
        hint_text:'ENTER HEIGHT IN (Metere)'
        pos_hint:{'center_x':0.45,'center_y':0.75}
        size_hint:0.7,0.1
        
    MDTextField:      
        id:tfr2
        input_filter:'float'
        hint_text:'ENTER WEIGHT IN(KG)'
        pos_hint:{'center_x':0.45,'center_y':0.65}
        size_hint:0.7,0.1               

                                       
    MDFloatingActionButton:
        id:cl1
        pos_hint:{'center_x':0.45,'center_y':0.55}
        size_hint:0.5,0.05
        on_press:
            app.bmi()
        MDTextButton:
            text:'CALCULATE'          
            size_hint:0,0       
                                      
    MDLabel:      
        id:ll1
        text:'____________________'
        pos_hint:{'center_x':0.5,'center_y':0.45}
        size_hint:0.5,1
                     
    MDLabel:      
        id:ll2
        text:'____________________'
        pos_hint:{'center_x':0.5,'center_y':0.35}     
        size_hint:0.5,1                      
                               
                                       
    MDFloatingActionButton:
        id:gb
        pos_hint:{'center_x':0.5,'center_y':0.1}
        size_hint:1,0.07
        on_press:
            app.root.current='s1'
            app.root.transition.direction='right'
        MDTextButton:
            text:'GO BACK'          
            size_hint:0,0         
        
        
        
'''

class Manager(ScreenManager):
    pass

class Fir(Screen):
    pass

class Sec(Screen):
    pass





class de(MDApp):
    def build(self):
        self.b=Builder.load_string(kv)   
        return self.b
    
    def add(self,te):
        try:
            self.b.get_screen('s1').ids.tf1.text+=te 
        except:
            pass                                                      
                                          
    def solve(self):
        so=self.b.get_screen('s1').ids.tf1.text 
        try:
            self.b.get_screen('s1').ids.tf1.text=str(eval(so))                                          
        except:
            toast('ERROR')
            self.b.get_screen('s1').ids.tf1.text=''          
    def remove(self):
        try:
            self.b.get_screen('s1').ids.tf1.text=''
        except:
            toast('SOORY,SOME ERROR PLEASE TRY AGAIN')            
            
    def bk(self):
        try:
            self.b.get_screen('s1').ids.tf1.do_backspace(from_undo=False,mode='bkspc')                        
        except:
            toast('SORRY,I TRYING TO REMOVE')                
            
    def thank(self):
        try:
            toast('THANKS,FOR USING OUR APP')  
        except:
            pass   
            
    def bg(self):
        a=self.b.get_screen('s1').ids.tf1.text
        self.b.get_screen('s1').ids.tf1.text +=a     
        
    
    def on_start(self,*args):          
        anim=Animation(opacity=1,duration=3)
        anim += Animation(opacity=1,duration=2)
        anim +=Animation(opacity=0,duration=3)
        anim+=Animation(opacity=0,duration=2)
        anim.repeat=True
        anim.start(self.b.get_screen('s1').ids.mdc1) 
                                            
    def bmi(self):
        try:
            he=float(self.b.get_screen('s2').ids.tfr1.text)                      
            he2=he*he
            he3=str(he2)                                                                               
            kg=float(self.b.get_screen('s2').ids.tfr2.text)                                             
            kg2=kg/he2
            kg3=str(kg2)         
            self.b.get_screen('s2').ids.ll1.text=kg3
            try:
                if kg2<18.4:
                    self.b.get_screen('s2').ids.ll2.text='LOW WEIGHT'
                elif kg2>=18.5 and kg2<=24.9:
                    self.b.get_screen('s2').ids.ll2.text='NORMAL WEIGHT'        
                elif kg2>=25.0 and kg2<=29.9:
                    self.b.get_screen('s2').ids.ll2.text='OVER WEIGHT'                                                                                            
                elif kg2>=30.0 and kg2<=34.9:
                    self.b.get_screen('s2').ids.ll2.text='OVER WEIGHT (OBESITY CLASS-1)'         
                elif kg2>=35.0 and kg2<=39.9:
                    self.b.get_screen('s2').ids.ll2.text='OVER WEIGHT (OBESITY CLASS-2)'                                                                 
                else:
                    self.b.get_screen('s2').ids.ll2.text='OVER WEIGHT (OBESITY CLASS-3)'                                                                 
                    
            except:
                pass               
        except:
            toast('PLEASE,ENTER DETAILS CORRECTLY')             
       
            
                 
                           
de().run()     