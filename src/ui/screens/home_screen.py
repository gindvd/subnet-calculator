from ui.color import Color

class HomeScreen:

    def __init__(self, app) -> None:
        self._app = app
    
    def render(self) -> None:
        """
        Renders the home screen, 
        shows choices to open different pages and functionality
        """

        print(Color.BOLD + "========Home========" + Color.RESET)
        print("1. Subnet Calculator")
        print("2. Network Identification")
        print("0. Exit")
    
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
