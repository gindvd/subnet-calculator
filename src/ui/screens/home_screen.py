from ui.color import Color

from ui.terminal import get_terminal_width

class HomeScreen:

    def __init__(self, app) -> None:
        self._app = app
    
    def render(self) -> None:
        """
        Renders the home screen, 
        shows choices to open different pages and functionality
        """
        width = get_terminal_width()

        print("\n\n" + Color.BOLD + "======== Home ========".center(width) + Color.RESET + "\n")
        print("1. Subnet Calculator".center(width))
        print("2. Network Identification".center(width))
        print()
        print("0. Exit".center(width))
    
    def handle_input(self, event: str) -> None:
        if event == "1":
            self._app.navigate("subnet")

        elif event == "2":
            self._app.navigate("network")

        elif event == "0":
            self._app.quit()

        else:
            print("Invalid option!")
            input("Press Enter to continue...")
