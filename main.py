from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image  # Added Image import for logo

KV = '''
ScreenManager:
    LoginScreen:
    WelcomeScreen:
    DashboardScreen:
    ComplaintScreen:

<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        Image:
            source: 'C:/Users/Baffa/Desktop/kivy/logo.png'  # Replace with the actual path to your logo image
            size_hint: None, None
            size: dp(100), dp(100)  # Adjust the size as needed
            pos_hint: {"center_x": .5}

        MDLabel:
            text: 'Login Page'
            font_style: 'H5'
            halign: 'center'

        MDTextField:
            id: username_input
            hint_text: 'Username'

        MDTextField:
            id: password_input
            hint_text: 'Password'
            password: True

        MDRaisedButton:
            text: 'Sign-In'
            on_release: app.login()
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": .5}

        MDRaisedButton:
            text: 'Sign-up'
            on_release: app.register()
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": .5}

        MDLabel:
            id: message_label
            text: ''
            theme_text_color: "Secondary"
            halign: 'center'

<WelcomeScreen>:
    name: 'welcome'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: 'Hello ABUSITE!! feel free to Complain'
            font_style: 'H3'
            halign: 'center'
            color: 0, 1, 0, 1  # Green color in RGBA format (R, G, B, A)
        MDLabel:
            text: 'the freedom to complain as a student is an important aspect of ensuring a safe, fair, and respectful learning environment. By following the appropriate procedures and providing accurate and relevant information, you can help address issues and improve the quality of education for yourself and others. Filing a complaint can be a useful tool to express dissatisfaction and seek solutions to problems. There are different ways to file a complaint, depending on the nature of the issue and the policies of the institution.'
            font_style: 'H6'
            halign: 'center'
            color: 0, 0, 1, 1  # Green color in RGBA format (R, G, B, A)

        MDLabel:
            id: complain_label
            text: ''
            font_style: 'Body1'
            halign: 'center'

        MDRaisedButton:
            text: 'Dashboard'
            on_release: app.show_dashboard()
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"x": 0, "top": 1}

        MDRaisedButton:
            text: 'Complain'
            on_release: app.show_complaint()
            md_bg_color: app.theme_cls.primary_color

        MDRaisedButton:
            text: 'Logout'
            on_release: app.logout()
            md_bg_color: app.theme_cls.primary_color
            bold: True

<DashboardScreen>:
    name: 'dashboard'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: 'Dashboard'
            font_style: 'H3'
            halign: 'center'
            text_color: 1, 0, 0, 1

        MDRaisedButton:
            text: 'Profile'
            on_release: app.show_profile()
            md_bg_color: app.theme_cls.primary_color

        MDRaisedButton:
            text: 'Latest News in Campus'
            on_release: app.show_latest_news()
            md_bg_color: app.theme_cls.primary_color

        MDRaisedButton:
            text: 'Tell a Friend'
            on_release: app.tell_a_friend()
            md_bg_color: app.theme_cls.primary_color

        MDRaisedButton:
            text: 'Logout'
            on_release: app.logout()
            md_bg_color: app.theme_cls.primary_color
            bold: True

<ComplaintScreen>:
    name: 'complaint'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: 'Enter Complaint'
            font_style: 'H3'
            halign: 'center'
            text_color: 0, 0, 1, 1  # Blue color in RGBA format (R, G, B, A)

        MDTextField:
            id: complaint_input
            hint_text: 'Type your complaint here'
            multiline: True

        MDRaisedButton:
            text: 'Submit'
            on_release: app.submit_complaint()
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": .5}

        MDLabel:
            id: complain_label
            text: ''
            theme_text_color: "Secondary"
            halign: 'center'

'''


class LoginScreen(Screen):
    pass


class WelcomeScreen(Screen):
    pass


class DashboardScreen(Screen):
    pass


class ComplaintScreen(Screen):
    pass


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def login(self):
        username = self.root.get_screen('login').ids.username_input.text
        password = self.root.get_screen('login').ids.password_input.text

        # Removed authentication logic, always consider it successful
        self.root.get_screen('login').ids.message_label.text = 'Login Successful'
        self.root.current = 'welcome'  # Switch to the welcome screen

    def register(self):
        username = self.root.get_screen('login').ids.username_input.text
        password = self.root.get_screen('login').ids.password_input.text

        # Add your user registration logic here
        if self.register_user(username, password):
            self.root.get_screen('login').ids.message_label.text = 'Registration Successful'
        else:
            self.root.get_screen('login').ids.message_label.text = 'Registration Failed'

    def register_user(self, username, password):
        # Replace this with your actual user registration logic (e.g., database insertion)
        return True  # Return True for successful registration

    def logout(self):
        self.root.current = 'login'  # Switch back to the login screen

    def show_dashboard(self):
        self.root.current = 'dashboard'

    def show_profile(self):
        # Add logic to show the profile screen here
        pass

    def show_latest_news(self):
        # Add logic to show the latest news screen here
        pass

    def tell_a_friend(self):
        # Add logic to tell a friend here
        pass

    def show_complaint(self):
        self.root.current = 'complaint'

    def submit_complaint(self):
        complaint = self.root.get_screen('complaint').ids.complaint_input.text
        if complaint:
            self.root.get_screen('welcome').ids.complain_label.text = 'You have submitted, and your request is being processed. Thank you'
            self.root.current = 'welcome'  # Switch back to the welcome screen
        else:
            self.root.get_screen('complaint').ids.complain_label.text = 'Please enter a complaint'


if __name__ == '__main__':
    LoginApp().run()
