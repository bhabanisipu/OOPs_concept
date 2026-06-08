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
            pass
        elif user_input == '4':
            pass
        else:
            exit()
    def signup(self):
        email = input("enter your email here")
        password = input("setup your password here")
        self.username = email
        self.password = password
        print("you have successfully signed up !!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username == '' or self.password == '':
            print("you have not signed up yet, please signup first to press the 1 key")
        else:
            uname = input("enter your email here")
            pwd = input("enter your password here")
            if self.username != uname or self.password != pwd:
                print("invalid credentials, please try again !!")
            else:
                print("you have successfully signed in !!")
                self.loggedin = True
        print("\n")
        self.menu()

obj = chatbook()