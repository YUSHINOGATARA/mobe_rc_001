from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class ScreenMain(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        gridlayout = GridLayout(cols=2, on_touch_move=lambda x, y: self.touch(y))

        Helmet = Button(text=" Головной убор ", font_size=14, size_hint=[0.2, 0.2], on_press=self.HelmetOpen)
        Armor = Button(text=" Armor ", font_size=14, size_hint=[0.5, 0.2])

        gridlayout.add_widget(Helmet)
        gridlayout.add_widget(Armor)

        self.add_widget(gridlayout)

    def HelmetOpen(self, *args):
        self.manager.current = 'helmet'

    def touch(self, y):
        if y.dx > 0:
            self.manager.transition.direction = 'right'
            self.manager.current = 'sec'
        else:
            pass


class SecondMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gridlayout = GridLayout(cols=2, on_touch_move=lambda x, y: self.touch(y))
        H = Button(text=" првое меню ", font_size=14, size_hint=[0.5, 0.2])
        A = Button(text=" Правой меню ", font_size=14, size_hint=[0.5, 0.2])
        gridlayout.add_widget(H)
        gridlayout.add_widget(A)
        self.add_widget(gridlayout)

    def touch(self, y):
        if y.dx > 0:
            pass
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'menu'


class Helmet(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        gridlayout = GridLayout(cols=1)

        Button1 = Button(text='eda.jpg', font_size=14, size_hint=[0.5, 0.2], background_normal='eda.jpg')
        Button2 = Button(text="принять", font_size=14, size_hint=[0.5, 0.2], on_press=self.Nazad)

        gridlayout.add_widget(Button1)
        gridlayout.add_widget(Button2)

        self.add_widget(gridlayout)

    def Nazad(self, *args):
        self.manager.current = 'menu'

    def menu_return(self, *args):
        self.manager.current = 'menu'


class RqCalcApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='menu'))
        sm.add_widget(Helmet(name='helmet'))
        sm.add_widget(SecondMenu(name='sec'))
        return sm


if __name__ == "__main__":
    RqCalcApp().run()
