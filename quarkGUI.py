from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from Buttons.searchbutton import SearchButton
from Buttons.MainPageButton import MainPageButton
from Buttons.FavouritePageButton import FavouritePageButton
from Buttons.FavouriteButton import FavouriteButton
from Inputs.Inputs import SearchInput, FromPriceInput, ToPriceInput
from Layouts.Layouts import UpperBar, BottomBar, GamesLayout, FilterLayout
from Inputs.Inputs import FromPriceInput,ToPriceInput
from GameTabs.GameTab import GameTab



Builder.load_file("quarkGUIkivy.kv")


class MainLayout(GridLayout):
    pass



class Quark(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    Quark().run()