import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton

kv = '''

BoxLayout:
    orientation: 'vertical'
    
    MDToolbar:
        title : 'Pharaoh Coding'
        md_bg_color: self.theme_cls.primary_color
        specific_text_color: 0,0,0,1
        
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'
            
            
            MDLabel:
                text: 'Python with Pharaoh Coding'
                halign: 'center'
                
            MDFillRoundFlatIconButton:
                text: 'Start learn'
                icon: 'language-python'
                pos_hint: {'center_x':.5, 'center_y':.4}
                on_release: app.python()
                
                
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'C++'
            icon: 'language-cpp'
            
            
            MDLabel:
                text: 'C++ with Pharaoh Coding'
                halign: 'center'
                
                
            MDFillRoundFlatIconButton:
                text: 'Start learn'
                icon: 'language-cpp'
                pos_hint: {'center_x':.5, 'center_y':.4}
                on_release: app.cpp()
                
                
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Java'
            icon: 'language-java'
            
            
            MDLabel:
                text: 'Java with Pharaoh Coding'
                halign: 'center'
                
                
            MDFillRoundFlatIconButton:
                text: 'Start learn'
                icon: 'language-java'
                pos_hint: {'center_x':.5, 'center_y':.4}
                on_release: app.java()
                
                
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Swift'
            icon: 'language-swift'
            
            
            MDLabel:
                text: 'Swift with Pharaoh Coding'
                halign: 'center'
                
                
            MDFillRoundFlatIconButton:
                text: 'Start learn'
                icon: 'language-swift'
                pos_hint: {'center_x':.5, 'center_y':.4}
                on_release: app.swift()
                
                
        MDBottomNavigationItem:
            name: 'screen 5'
            text: 'C#'
            icon: 'language-csharp'
            
            
            MDLabel:
                text: 'C# with Pharaoh Coding'
                halign: 'center'
                
                
            MDFillRoundFlatIconButton:
                text: 'Start learn'
                icon: 'language-csharp'
                pos_hint: {'center_x':.5, 'center_y':.4}
                on_release: app.csharp()

'''

class App(MDApp):
    
    def python(self):
        webbrowser.open('https://www.python.org/')
        
    def cpp(self):
        webbrowser.open('https://cplusplus.com/')
        
    def java(self):
        webbrowser.open('https://www.java.com/en/')
        
    def swift(self):
        webbrowser.open('https://www.swift.com/')
        
    def csharp(self):
        webbrowser.open('https://learn.microsoft.com/en-us/dotnet/csharp/')
    
    def build(self):
        self.theme_cls.theme_style= 'Dark'
        self.theme_cls.primary_palette= 'Green'
        
        return Builder.load_string(kv)
        
App().run()