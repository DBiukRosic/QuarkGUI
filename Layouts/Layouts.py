from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from GameTabs.GameTab import GameTab

Builder.load_file("Layouts/Layouts.kv")


class UpperBar(BoxLayout):
    pass

class BottomBar(GridLayout):
    pass


class GamesLayout(ScrollView):
    pass


class FilterLayout(ScrollView):
    pass