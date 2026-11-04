from ui.color import Color

class SubnetScreen:

    def __init__(self, app):
        self._app = app

    def render(self) -> None:
        print(Color.BOLD + "====Subnet Calculator====" + Color.RESET)
        print("0. Return Home")
    
    def handle_input(self, event: str) -> None:
        if event == "0":
            self._app.navigate("home")
        
        else:
            print("Invalid option!")
            input("Press Enter to continue...")
