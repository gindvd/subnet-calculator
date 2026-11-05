from ui.color import Color

from ui.terminal import get_terminal_width

class SubnetScreen:

    def __init__(self, app):
        self._app = app

    def render(self) -> None:
        width = get_terminal_width()

        print("\n\n" + Color.BOLD + "==== Subnet Calculator ====".center(width) + Color.RESET + "\n")
        print("0. Return Home".center(width))
    
    def handle_input(self, event: str) -> None:
        if event == "0":
            self._app.navigate("home")
        
        else:
            print("Invalid option!")
            input("Press Enter to continue...")
