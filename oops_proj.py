class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    def menu(self):
        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_posts()
        elif user_input == '4':
            self.send_message()
        else:
            exit()
    def signup(self):
        email = input("enter your email here : ")
        password = input("setup your password here : ")
        self.username = email
        self.password = password
        print("you have successfully signed up !!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username == '' or self.password == '':
            print("you have not signed up yet, please signup first to press the 1 key  ")
        else:
            uname = input("enter your email here : ")
            pwd = input("enter your password here : ")
            if self.username != uname or self.password != pwd:
                print("invalid credentials, please try again !!")
            else:
                print("you have successfully signed in !!")
                self.loggedin = True
        print("\n")
        self.menu()
    def my_posts(self):
        if self.loggedin == True:
            txt = input("enter you message here : ")
            print(f"following content has been posted {txt}")
        else:
            print("you need to login first to post something !!")
        print("\n")
        self.menu()
    def send_message(self):
        if self.loggedin == True:
            txt = input("enter your message here : ")
            friend = input("whom to you want to send the message to ? : ")
            print(f"following content has been sent to {friend} : {txt}")
        else:
            print("you need to login first to send a message !!")
        print("\n")
        self.menu()

obj = chatbook()