from tkinter import *
from tkinter.ttk import *
import login
import changepassword
import managecontacts

class HomeWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title('Home')
        self.state('zoomed')

        s = Style()

        s.configure('Header.TFrame', background = 'blue')
        s.configure('Content.TFrame', background = 'white')
        s.configure('Header.TLabel', background = 'blue', foreground = 'white', font = ('Arial', 25))

        header_frame = Frame(self, style = 'Header.TFrame')
        header_frame.pack(fill = X)

        header_label = Label(header_frame, text = 'My Contact Book', style = 'Header.TLabel')
        header_label.pack(pady = 10)

        navigation_frame = Frame(self, style = 'Header.TFrame')
        navigation_frame.pack(side = LEFT, fill = Y)

        s.configure('Navigation.TButton', width = 15, font = ('Arial', 12))

        manage_contacts_button = Button(navigation_frame, text = 'Manage Contacts',
        style = 'Navigation.TButton', command = self.manage_contacts_button_click)
        manage_contacts_button.pack(ipady = 10, pady = 1)

        change_password_button = Button(navigation_frame, text = 'Change Password',
        style = 'Navigation.TButton', command = self.change_password_button_click)
        change_password_button.pack(ipady = 10, pady = 1)

        logout_button = Button(navigation_frame, text = 'Logout',
        style = 'Navigation.TButton', command = self.logout_button_click)
        logout_button.pack(ipady = 10, pady = 1)

        self.content_frame = Frame(self, style = 'Content.TFrame')
        self.content_frame.pack(fill = BOTH, expand = TRUE)

        managecontacts.ManageContactsFrame(self.content_frame)

    def logout_button_click(self):
        self.destroy()
        login.LoginWindow()

    def change_password_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        changepassword.ChangePasswordFrame(self.content_frame)

    def manage_contacts_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        managecontacts.ManageContactsFrame(self.content_frame)
        

        

        
