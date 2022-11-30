import tkinter as tk
import time

# global variable for the user checking balance
current_balance_checking = 100

# global variable for the user savings balance
current_balance_savings = 200


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'BalanceChecking': tk.IntVar()}
        self.shared_data2 = {'BalanceSavings': tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, AccountMenuPage, CheckingMenuPage, SavingsMenuPage, WithdrawCheckingPage, WithdrawSavingsPage, DepositCheckingPage, DepositSavingsPage, BalanceCheckingPage, BalanceSavingsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")



        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# class that handle the home window
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Securitex')  # Instance of the class StartPage , it display the page title
        self.controller.state('zoomed')

        # design the header of the  page
        '''Start head'''
        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)
        '''End head'''
        # Add space between the header and the  label where the pin input is
        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        '''Start password label'''
        password_label = tk.Label(self,
                                  text='Enter your password',
                                  font=('orbitron', 13),
                                  bg='#3d3d5c',
                                  fg='white')
        password_label.pack(pady=10)
        '''end password label'''

        # password variable from the input
        my_password = tk.StringVar()

        '''Start password input box'''
        password_entry_box = tk.Entry(self,
                                      textvariable=my_password,
                                      font=('orbitron', 12),
                                      width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)
        '''End password input box'''

        # function that changes character in to *
        def handle_focus_in(_):
            password_entry_box.configure(fg='black', show='*')

        password_entry_box.bind('<FocusIn>', handle_focus_in)

        # function to check if password is valid
        def check_password():
            if my_password.get() == '1234':
                my_password.set('')
                incorrect_password_label['text'] = ''


                controller.show_frame('AccountMenuPage')


            elif my_password.get() == '1324':
                my_password.set('')
                incorrect_password_label['text'] = ''


                controller.show_frame('AccountMenuPage')


            else:
                incorrect_password_label['text'] = 'Incorrect Password'

        '''Start input validator botton'''
        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_password,
                                 relief='raised',
                                 borderwidth=3,
                                 width=40,
                                 height=3)
        enter_button.pack(pady=10)
        '''End input validator botton'''

        '''Start incorrect password label'''
        incorrect_password_label = tk.Label(self,
                                            text='',
                                            font=('orbitron', 13),
                                            fg='white',
                                            bg='#33334d',
                                            anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)
        '''End incorrect password label'''


        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')
        '''Start footer page'''
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()

        '''End footer page'''

# class that handle the account menu window
class AccountMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 23),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        # function to redirect to the checking withdraw page
        def checkingMenu():
            controller.show_frame('CheckingMenuPage')

        '''Start checking withdraw page botton'''
        checking_menu_button = tk.Button(button_frame,
                                    text='Checking menu',
                                    command=checkingMenu,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        checking_menu_button.grid(row=0, column=0, pady=5)
        '''End checking withdraw page botton'''

        # function to redirect to the savings withdraw page
        def savingsMenu():
            controller.show_frame('SavingsMenuPage')

        '''Start savings withdraw page botton'''
        savings_menu_button = tk.Button(button_frame,
                                    text='Savings menu',
                                    command=savingsMenu,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        savings_menu_button.grid(row=0, column=6, pady=5, padx=600)
        '''End savings withdraw page botton'''



        # function to exit the program
        #get back to start page
        def exit():
            controller.show_frame('StartPage')

        '''Start exit button botton'''
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=3, column=0, pady=5)
        '''End exit button botton'''

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        '''Start footer page'''
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()
        '''End footer page'''




# class that handle the checking account menu window
class CheckingMenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 23),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        # function to redirect to the checking withdraw page
        def withdrawChecking():
            controller.show_frame('WithdrawCheckingPage')

        '''Start checking withdraw page botton'''
        withdraw_button = tk.Button(button_frame,
                                    text='Withdraw from checking account',
                                    command=withdrawChecking,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        withdraw_button.grid(row=0, column=0, pady=5)
        '''End checking withdraw page botton'''



        # function to redirect to the checking deposit page
        def depositChecking():
            controller.show_frame('DepositCheckingPage')

        '''Start checking deposit page botton'''
        deposit_button = tk.Button(button_frame,
                                   text='Deposit to checking acount',
                                   command=depositChecking,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        '''End checking deposit page botton'''



        # function to redirect to the checking balance page
        def balanceChecking():
            controller.show_frame('BalanceCheckingPage')

        '''Start checking balance page botton'''
        balance_button = tk.Button(button_frame,
                                   text='Balance checking account',
                                   command=balanceChecking,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        balance_button.grid(row=2, column=0, pady=5)
        '''End balance page botton'''



        # function to exit the program
        #get back to start page
        def exit():
            controller.show_frame('StartPage')

        '''Start exit button botton'''
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=3, column=0, pady=5)
        '''End exit button botton'''

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        '''Start footer page'''
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()
        '''End footer page'''


# class that handle the savings account menu window
class SavingsMenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 23),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)


        # function to redirect to the savings withdraw page
        def withdrawSavings():
            controller.show_frame('WithdrawSavingsPage')

        '''Start savings withdraw page botton'''
        withdraw_button = tk.Button(button_frame,
                                    text='Withdraw from savings account',
                                    command=withdrawSavings,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        withdraw_button.grid(row=0, column=6, pady=5, padx=600)
        '''End savings withdraw page botton'''


        # function to redirect to the savings deposit page
        def depositSavings():
            controller.show_frame('DepositSavingsPage')

        '''Start savings deposit page botton'''
        deposit_button = tk.Button(button_frame,
                                   text='Deposit to saving acount',
                                   command=depositSavings,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        deposit_button.grid(row=1, column=6, pady=5, padx=600)

        '''End savings deposit page botton'''


        # function to savings redirect to the balance page
        def balanceSavings():
            controller.show_frame('BalanceSavingsPage')

        '''Start savings balance page botton'''
        balance_button = tk.Button(button_frame,
                                   text='Balance savings account',
                                   command=balanceSavings,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        balance_button.grid(row=2, column=6, pady=5, padx=600)
        '''End savings balance page botton'''


        # function to exit the program
        #get back to start page
        def exit():
            controller.show_frame('StartPage')

        '''Start exit button botton'''
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=3, column=0, pady=5)
        '''End exit button botton'''

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        '''Start footer page'''
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()
        '''End footer page'''




# class to display checking Withdraw Page
class WithdrawCheckingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        '''Start choose amount label'''
        choose_amount_label = tk.Label(self,
                                       text='Choose the amount you want to withdraw',
                                       font=('orbitron', 13),
                                       fg='white',
                                       bg='#3d3d5c')
        choose_amount_label.pack()
        '''End choose amount label'''

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        '''Start incorrect password label'''
        insufficient_balance_label = tk.Label(self,
                                              text='',
                                              font=('orbitron', 23),
                                              fg='white',
                                              bg='#33334d',
                                              anchor='n')
        insufficient_balance_label.pack(fill='both', expand=True)
        '''End incorrect password label'''
        # function to get the amount choosen by the use
        # And subtract the withdraw amount from the use balance
        def withdraw(amount):
            global current_balance_checking

            if amount < 5:
                insufficient_balance_label['text'] = 'Withdrawal amount has to be greater than 4$'
            else:
                if amount > current_balance_checking:
                    insufficient_balance_label['text'] = 'Insufficient balance'
                else:
                    current_balance_checking -= amount
                    controller.shared_data['BalanceChecking'].set(current_balance_checking)
                    controller.show_frame('CheckingMenuPage')

        '''Start withdraw amount button 0f 20'''
        twenty_button = tk.Button(button_frame,
                                  text='20',
                                  command=lambda: withdraw(20),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        twenty_button.grid(row=0, column=0, pady=5)
        '''End withdraw amount button 0f 20'''

        '''Start withdraw amount button 0f 40'''
        forty_button = tk.Button(button_frame,
                                 text='40',
                                 command=lambda: withdraw(40),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        forty_button.grid(row=1, column=0, pady=5)
        '''End withdraw amount button 0f 40'''

        '''Start withdraw amount button 0f 60'''
        sixty_button = tk.Button(button_frame,
                                 text='60',
                                 command=lambda: withdraw(60),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        sixty_button.grid(row=2, column=0, pady=5)
        '''End withdraw amount button 0f 60'''

        '''Start withdraw amount button 0f 80'''
        eighty_button = tk.Button(button_frame,
                                  text='80',
                                  command=lambda: withdraw(80),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        eighty_button.grid(row=3, column=0, pady=5)
        '''End withdraw amount button 0f 80'''

        '''Start withdraw amount button 0f 100'''
        one_hundred_button = tk.Button(button_frame,
                                       text='100',
                                       command=lambda: withdraw(100),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        one_hundred_button.grid(row=0, column=1, pady=5, padx=555)
        '''End withdraw amount button 0f 100'''

        '''Start withdraw amount button 0f 200'''
        two_hundred_button = tk.Button(button_frame,
                                       text='200',
                                       command=lambda: withdraw(200),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        two_hundred_button.grid(row=1, column=1, pady=5)
        '''End withdraw amount button 0f 200'''

        '''Start withdraw amount button 0f 300'''
        three_hundred_button = tk.Button(button_frame,
                                         text='300',
                                         command=lambda: withdraw(300),
                                         relief='raised',
                                         borderwidth=3,
                                         width=50,
                                         height=5)
        three_hundred_button.grid(row=2, column=1, pady=5)
        '''End withdraw amount button 0f 300'''

        # varaible to store the withdraw amount entered manually
        cash = tk.StringVar()

        '''Start label for cash box entry'''
        other_amount_entry = tk.Entry(button_frame,
                                      textvariable=cash,
                                      width=59,
                                      justify='right')
        other_amount_entry.grid(row=3, column=1, pady=5, ipady=30)
        '''End label for cash box entry'''

        # function to get the manually entered amount by the use
        # And subtract that amount from the use balance
        def other_amount(_):
            global current_balance_checking
            if int(cash.get()) < 5:
                insufficient_balance_label['text'] = 'Withdrawal amount has to be greater than 4$'
            else:
                if int(cash.get()) > current_balance_checking:
                    insufficient_balance_label['text'] = 'Insufficient balance'
                else:
                    current_balance_checking -= int(cash.get())
                    controller.shared_data['BalanceChecking'].set(current_balance_checking)
                    cash.set('')
                    controller.show_frame('CheckingMenuPage')


        other_amount_entry.bind('<Return>', other_amount)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        # function to get back to the  menu page
        def menu():
            controller.show_frame('CheckingMenuPage')

        '''Start menu button'''
        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=3)
        menu_button.grid(row=4, column=1, pady=5)
        '''End menu button'''



        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')



        '''Start footer page'''
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()
        '''End footer page'''


# class to display savings Withdraw Page
class WithdrawSavingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        '''Start choose amount label'''
        choose_amount_label = tk.Label(self,
                                       text='Choose the amount you want to withdraw',
                                       font=('orbitron', 13),
                                       fg='white',
                                       bg='#3d3d5c')
        choose_amount_label.pack()
        '''End choose amount label'''

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        '''Start incorrect password label'''
        insufficient_balance_label = tk.Label(self,
                                              text='',
                                              font=('orbitron', 23),
                                              fg='white',
                                              bg='#33334d',
                                              anchor='n')
        insufficient_balance_label.pack(fill='both', expand=True)
        '''End incorrect password label'''
        # function to get the amount choosen by the use
        # And subtract the withdraw amount from the use balance
        def withdraw(amount):
            global current_balance_savings

            if amount < 5:
                insufficient_balance_label['text'] = 'Withdrawal amount has to be greater than 4$'
            else:
                if amount > current_balance_savings:
                    insufficient_balance_label['text'] = 'Insufficient balance'
                else:
                    current_balance_savings -= amount
                    controller.shared_data2['BalanceSavings'].set(current_balance_savings)
                    controller.show_frame('SavingsMenuPage')

        '''Start withdraw amount button 0f 20'''
        twenty_button = tk.Button(button_frame,
                                  text='20',
                                  command=lambda: withdraw(20),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        twenty_button.grid(row=0, column=0, pady=5)
        '''End withdraw amount button 0f 20'''

        '''Start withdraw amount button 0f 40'''
        forty_button = tk.Button(button_frame,
                                 text='40',
                                 command=lambda: withdraw(40),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        forty_button.grid(row=1, column=0, pady=5)
        '''End withdraw amount button 0f 40'''

        '''Start withdraw amount button 0f 60'''
        sixty_button = tk.Button(button_frame,
                                 text='60',
                                 command=lambda: withdraw(60),
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        sixty_button.grid(row=2, column=0, pady=5)
        '''End withdraw amount button 0f 60'''

        '''Start withdraw amount button 0f 80'''
        eighty_button = tk.Button(button_frame,
                                  text='80',
                                  command=lambda: withdraw(80),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        eighty_button.grid(row=3, column=0, pady=5)
        '''End withdraw amount button 0f 80'''

        '''Start withdraw amount button 0f 100'''
        one_hundred_button = tk.Button(button_frame,
                                       text='100',
                                       command=lambda: withdraw(100),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        one_hundred_button.grid(row=0, column=1, pady=5, padx=555)
        '''End withdraw amount button 0f 100'''

        '''Start withdraw amount button 0f 200'''
        two_hundred_button = tk.Button(button_frame,
                                       text='200',
                                       command=lambda: withdraw(200),
                                       relief='raised',
                                       borderwidth=3,
                                       width=50,
                                       height=5)
        two_hundred_button.grid(row=1, column=1, pady=5)
        '''End withdraw amount button 0f 200'''

        '''Start withdraw amount button 0f 300'''
        three_hundred_button = tk.Button(button_frame,
                                         text='300',
                                         command=lambda: withdraw(300),
                                         relief='raised',
                                         borderwidth=3,
                                         width=50,
                                         height=5)
        three_hundred_button.grid(row=2, column=1, pady=5)
        '''End withdraw amount button 0f 300'''

        # varaible to store the withdraw amount entered manually
        cash = tk.StringVar()

        '''Start label for cash box entry'''
        other_amount_entry = tk.Entry(button_frame,
                                      textvariable=cash,
                                      width=59,
                                      justify='right')
        other_amount_entry.grid(row=3, column=1, pady=5, ipady=30)
        '''End label for cash box entry'''

        # function to get the manually entered amount by the use
        # And subtract that amount from the use balance
        def other_amount(_):
            global current_balance_savings
            if int(cash.get()) < 5:
                insufficient_balance_label['text'] = 'Withdrawal amount has to be greater than 4$'
            else:
                if int(cash.get()) > current_balance_savings:
                    insufficient_balance_label['text'] = 'Insufficient balance'
                else:
                    current_balance_savings -= int(cash.get())
                    controller.shared_data2['BalanceSavings'].set(current_balance_savings)
                    cash.set('')
                    controller.show_frame('SavingsMenuPage')


        other_amount_entry.bind('<Return>', other_amount)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        # function to get back to the  menu page
        def menu():
            controller.show_frame('SavingsMenuPage')

        '''Start menu button'''
        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=3)
        menu_button.grid(row=4, column=1, pady=5)
        '''End menu button'''



        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')



        '''Start footer page'''
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()
        '''End footer page'''


# class that handle checking deposit operations
class DepositCheckingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        '''Start incorrect password label'''
        incorrect_amount_label = tk.Label(self,
                                              text='',
                                              font=('orbitron', 13),
                                              fg='white',
                                              bg='#33334d',
                                              anchor='n')
        incorrect_amount_label.pack(fill='both', expand=True)
        '''End incorrect password label'''

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        enter_amount_label = tk.Label(self,
                                      text='Enter amount',
                                      font=('orbitron', 13),
                                      bg='#3d3d5c',
                                      fg='white')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 font=('orbitron', 12),
                                 width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance_checking
            if int(cash.get()) < 10:
                incorrect_amount_label['text'] = 'Input an amount greater than 9$'
            else:
                current_balance_checking += int(cash.get())
                controller.shared_data['BalanceChecking'].set(current_balance_checking)
                controller.show_frame('BalanceCheckingPage')
                cash.set('')

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=deposit_cash,
                                 relief='raised',
                                 borderwidth=3,
                                 width=40,
                                 height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self, bg='#33334d')
        two_tone_label.pack(fill='both', expand=True)

        # function to get back to the  menu page
        def menu():
            controller.show_frame('CheckingMenuPage')

        '''Start menu button'''
        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=3)
        menu_button.grid(row=4, column=1, pady=5)
        '''End menu button'''

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


# class that handle savings deposit operations
class DepositSavingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        '''Start incorrect password label'''
        incorrect_amount_label = tk.Label(self,
                                              text='',
                                              font=('orbitron', 13),
                                              fg='white',
                                              bg='#33334d',
                                              anchor='n')
        incorrect_amount_label.pack(fill='both', expand=True)
        '''End incorrect password label'''

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        enter_amount_label = tk.Label(self,
                                      text='Enter amount',
                                      font=('orbitron', 13),
                                      bg='#3d3d5c',
                                      fg='white')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 font=('orbitron', 12),
                                 width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance_savings
            if int(cash.get()) < 10:
                incorrect_amount_label['text'] = 'Input an amount greater than 9$'
            else:
                current_balance_savings += int(cash.get())
                controller.shared_data2['BalanceSavings'].set(current_balance_savings)
                controller.show_frame('BalanceSavingsPage')
                cash.set('')

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=deposit_cash,
                                 relief='raised',
                                 borderwidth=3,
                                 width=40,
                                 height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self, bg='#33334d')
        two_tone_label.pack(fill='both', expand=True)

        # function to get back to the  menu page
        def menu():
            controller.show_frame('SavingsMenuPage')

        '''Start menu button'''
        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=3)
        menu_button.grid(row=4, column=1, pady=5)
        '''End menu button'''

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        # function to get the current time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


# class to display checking Balance Page
class BalanceCheckingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        # get the user balance
        global current_balance_checking
        controller.shared_data['BalanceChecking'].set(current_balance_checking)

        '''Start balance label'''
        balance_label = tk.Label(self,

                                 textvariable=controller.shared_data['BalanceChecking'],
                                 font=('orbitron', 53),
                                 fg='white',
                                 bg='#3d3d5c',
                                 anchor='w')
        balance_label.pack(fill='x')
        '''End balance label'''



        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=False)

        # function to get back to the  menu page
        def menu():
            controller.show_frame('CheckingMenuPage')

        '''Start menu button'''
        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=0, column=0, pady=5)
        '''End menu button'''

        # exit program and get back to start page windows
        def exit():
            controller.show_frame('StartPage')

        '''Start exit button'''
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=1, column=0, pady=5)
        '''End exit button'''

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()

# class to display checking Balance Page
class BalanceSavingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='MOST SECURED ATM',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        # get the user balance
        global current_balance_savings
        controller.shared_data2['BalanceSavings'].set(current_balance_savings)


        '''Start balance label'''
        balance_label = tk.Label(self,

                                 textvariable=controller.shared_data2['BalanceSavings'],
                                 font=('orbitron', 53),
                                 fg='white',
                                 bg='#3d3d5c',
                                 anchor='w')
        balance_label.pack(fill='x')
        '''End balance label'''


        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        # function to get back to the  menu page
        def menu():
            controller.show_frame('SavingsMenuPage')

        '''Start menu button'''
        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=0, column=0, pady=5)
        '''End menu button'''

        # exit program and get back to start page windows
        def exit():
            controller.show_frame('StartPage')

        '''Start exit button'''
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=1, column=0, pady=5)
        '''End exit button'''

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()