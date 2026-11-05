from ui.screens.home_screen import HomeScreen
from ui.screens.subnet_screen import SubnetScreen
from ui.screens.network_screen import NetworkScreen

from ui.terminal import clear_terminal

class App:

    def __init__(self):
        self._running: bool = True

        self._screens = {
            "home": HomeScreen(self),
            "subnet": SubnetScreen(self),
            "network": NetworkScreen(self)
        }

        self._current_window = self._screens["home"]
    
    def navigate(self, screen: str):
        self._current_window = self._screens[screen]
        self.render()

    def render(self):
        clear_terminal()
        self._current_window.render()

    def run(self):
        self.render()

        while self._running:
            choice: str = input("\nSelect: ").strip()
            self._current_window.handle_input(choice)
    
    def quit(self):
        self._running = False
        clear_terminal()


if __name__ == "__main__":
    app = App()
    app.run()