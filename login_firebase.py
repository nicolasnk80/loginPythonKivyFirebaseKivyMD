import pyrebase


class Accont:
    def __init__(self):
        firebaseConfig = {
            "apiKey": "AIzaSyBniiXUdMN3CfbsvEMnF3HRpuLNB-YpVZY",
            "authDomain": "amigo-virtual-6960b.firebaseapp.com",
            "projectId": "amigo-virtual-6960b",
            "databaseURL": "https://amigo-virtual-6960b.firebaseio.com",
            "storageBucket": "amigo-virtual-6960b.appspot.com",
            "messagingSenderId": "924780726622",
            "appId": "1:924780726622:web:38694cd80c1024d3a6a7cf",
            "measurementId": "G-T0PYHDD2RB"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()

    def sign_in(self, email, password):
        try:
            self.auth.sign_in_with_email_and_password(email, password)
            return True

        except:
            return False

    def sing_up(self, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
            return True

        except:
            return False

    def reset_password(self, email):
        try:
            self.auth.send_password_reset_email(email)
            return True

        except:
            return False