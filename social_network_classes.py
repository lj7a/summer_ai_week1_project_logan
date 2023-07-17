class SocialNetwork:
    def __init__(self):
        Logan = Person("Logan", 16)
        Nick = Person("Nick", 17)

        self.list_of_people = [Logan,Nick] 
        self.current_person = []

    def check_user(self):
        input_username = input()
        for x in range(len(self.list_of_people)):
            if input_username == self.list_of_people[x].get_name():
                self.current_person = self.list_of_people[x]
                print("You are now logged into: " + input_username)
                return True
        print("Account invalid")
        return False
                

    def create_account(self):
        print("Enter your username")
        new_user_username = str(input())
        print("Enter your age")
        new_user_age = int(input())
        new_user = Person(new_user_username, new_user_age)
        self.list_of_people.append(new_user)

        pass

    def get_User(self):
        return self.current_person

    def add_friend(self):
        print("Type the name of your friend")
        input_friend = input()
        for x in range(len(self.list_of_people)):
            if input_friend == self.list_of_people[x].get_name():
                self.current_person.friendlist.append(self.list_of_people[x]) 
                self.list_of_people[x].friendlist.append(self.current_person)
                print("You are now friends with: " + input_friend)
                return True
        print("Account invalid")
        return False

    def remove_friend(self):
        print("Type the name of your friend you want to remove")
        removed_friend = input()
        for x in range(len(self.list_of_people)):
            if removed_friend == self.list_of_people[x].get_name():
                self.current_person.friendlist.remove(self.list_of_people[x]) 
                self.list_of_people[x].friendlist.remove(self.current_person)
                print("You are no longer friends with: " + removed_friend)
                return True
        print("Account invalid")
        return False

    def view_friends(self):
        if len(self.current_person.friendlist) == 0:
            print("You have no friends... LOL!")
        else:
            for x in range(len(self.current_person.friendlist)):
                print(self.current_person.friendlist[x].get_name())
        pass

    def send_message(self):
        print("Enter the name of the user you want to send a message to")
        recipiant = input()
        print("Enter your message")
        contents = input()
        for x in range(len(self.list_of_people)):
            if recipiant == self.list_of_people[x].get_name():
                if self.current_person.name in self.list_of_people[x].blockedList:
                    print("Message Blocked")
                else:
                    self.list_of_people[x].messageInbox.append(contents + " From: " + self.current_person.get_name())
                    print("Your message was sent to " + recipiant)
        pass

    def log_out(self):
        self.current_person = [] 
        pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friendlist = []
        self.messageInbox = [] 
        self.blockedList = [] 

    def block_friend(self):
        print("Enter the name of the user you want to block")
        self.blockedList.append(input())
        pass

    def edit_details(self):
        print("You are now editing your details; Enter your age:")
        self.age = input()
        print("Enter your new name")
        self.name = input()
        pass

    def check_messages(self):
        print(self.messageInbox)
        pass

    def check_blocked(self):
        print(self.blockedList)
        pass

    def get_name(self):
        return self.name

