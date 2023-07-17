from getpass import getuser
from  social_network_classes import SocialNetwork
import social_network_ui


ai_social_network = SocialNetwork()

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = str(social_network_ui.mainMenu())

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
            social_network_ui.manageAccountMenu()

        elif choice == "2":
            print("Type your username to login")
            if ai_social_network.check_user():
                inner_menu_choice = social_network_ui.manageAccountMenu()
            else:
                social_network_ui.mainMenu()
            
            while True:
                if inner_menu_choice == "1":
                    ai_social_network.get_User().edit_details()
                    inner_menu_choice = 0
                elif inner_menu_choice == "2":
                    ai_social_network.add_friend()
                    inner_menu_choice = 0
                elif inner_menu_choice == "3":
                    ai_social_network.view_friends()
                    inner_menu_choice = 0
                elif inner_menu_choice == "4":
                    ai_social_network.get_User().check_messages() 
                    inner_menu_choice = 0
                elif inner_menu_choice == "5":
                    ai_social_network.send_message()
                    inner_menu_choice = 0
                elif inner_menu_choice == "6":
                    ai_social_network.get_User().block_friend()
                    inner_menu_choice = 0
                elif inner_menu_choice == "7": 
                    ai_social_network.get_User().check_blocked()
                    inner_menu_choice = 0
                elif inner_menu_choice == "8": 
                    ai_social_network.remove_friend()
                    inner_menu_choice = 0
                elif inner_menu_choice == "9": 
                    ai_social_network.log_out()
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        choice = social_network_ui.mainMenu()



        
