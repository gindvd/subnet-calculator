from ui.color import Color

class Home:

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
    
    def select_option(self) -> None:
        choice = input("\nSelect: ")

        
        if choice == "1":
            pass

        elif choice == "2":
            pass

        elif choice == "0":
            pass

        else:
            pass
