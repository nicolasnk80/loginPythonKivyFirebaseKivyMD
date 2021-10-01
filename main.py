from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from login_firebase import Accont


class Manager(ScreenManager):
    pass


class LoginScreen(MDScreen):
    def on_pre_enter(self, *args):
        try:
            self.ids.text_email.text = ""
            self.ids.text_password.text = ""

        except:
            pass

    def try_sign_in(self):
        Clock.schedule_once(self.start_sign_in, .5)

    def start_sign_in(self, *args):
        email = self.ids.text_email.text
        password = self.ids.text_password.text

        if accont.sign_in(email, password):
            MDApp.get_running_app().root.current = "home_page"

        else:
            if email and password:
                #self.ids.text_email.text = ""
                self.ids.text_password.text = ""
                self.ids.text_email.focus = True

            elif email and not password:
                self.ids.text_password.focus = True

            elif password and not email:
                self.ids.text_password.text = ""
                self.ids.text_email.focus = True

            else:
                self.ids.text_email.focus = True


class HomePage(MDScreen):
    def callback(self):
        MDApp.get_running_app().root.current = "login"


class ResetPassword(MDScreen):
    def callback(self, *args):
        MDApp.get_running_app().root.current = "login"

    def on_pre_enter(self, *args):
        self.ids.text_redefined.theme_text_color = "Primary"
        self.ids.text_redefined.text = "Send E-mail to reset password."
        self.ids.email_confirm.text = ""

    def send_email_confirm(self):
        email = self.ids.email_confirm.text

        if accont.reset_password(email):
            self.ids.text_redefined.text = "Email successfully sent"
            self.ids.text_redefined.theme_text_color = "Custom"
            self.ids.text_redefined.text_color = (0, 1, 0, 1)

        else:
            self.ids.text_redefined.text = "Failed to send email"
            self.ids.text_redefined.theme_text_color = "Custom"
            self.ids.text_redefined.text_color = (1, 0, 0, 1)

        Clock.schedule_once(self.callback, 3)


class Register(MDScreen):
    def on_pre_enter(self, *args):
        self.ids.email_register.text = ""
        self.ids.password_register.text = ""
        self.ids.password_register_confirm.text = ""
        self.ids.label_register.text = "Enter your data"
        self.ids.label_register.theme_text_color = "Primary"

    def callback(self, *args):
        MDApp.get_running_app().root.current = "login"

    def validate_info(self):
        email = self.ids.email_register.text
        password = self.ids.password_register.text
        password_confirm = self.ids.password_register_confirm.text

        if password == password_confirm and "@" in email and ".com" in email and len(password) >= 6:
            if accont.sing_up(email, password):
                self.ids.label_register.text = "Registration created successfully"
                self.ids.label_register.theme_text_color = "Custom"
                self.ids.label_register.text_color = (0, 1, 0, 1)
                Clock.schedule_once(self.callback, 3)

            else:
                self.ids.label_register.text = "failed to create record"
                self.ids.label_register.theme_text_color = "Custom"
                self.ids.label_register.text_color = (1, 0, 0, 1)

        else:
            if not email or "@" not in email or ".com" not in email:
                self.ids.email_register.focus = True

            elif len(password) < 6:
                self.ids.password_register_confirm.text = ""
                self.ids.password_register.text = ""
                self.ids.password_register.focus = True

            elif  len(password_confirm) < 6:
                self.ids.password_register_confirm.text = ""
                self.ids.password_register_confirm.focus = True

            elif password != password_confirm:
                if password:
                    self.ids.password_register.focus = True
                    self.ids.password_register_confirm.text = ""
                    self.ids.password_register.text = ""
                else:
                    self.ids.password_register_confirm.focus = True
                    self.ids.password_register_confirm.text = ""


class MyApp(MDApp):
    Window.size = (400, 600)

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Manager()#Builder.load_file("myapp.kv")


if __name__ == "__main__":
    accont = Accont()
    MyApp().run()
