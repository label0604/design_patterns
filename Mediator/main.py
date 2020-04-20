import sys
from abc import ABCMeta, abstractmethod
from distutils.util import strtobool


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def create_colleagues(self):
        pass

    @abstractmethod
    def colleague_changed(self):
        pass


class Colleague(metaclass=ABCMeta):
    @abstractmethod
    def set_mediator(self, mediator):
        pass

    @abstractmethod
    def set_colleague_enabled(self, enabled):
        pass


class ColleagueButton(Colleague):
    def __init__(self):
        self.mediator = None
        self.enabled = False

    def set_mediator(self, mediator):
        self.mediator = mediator

    def set_colleague_enabled(self, enabled):
        self.enabled = enabled

    def do_click(self):
        if self.enabled:
            print('Success login')
        else:
            print('Failure login')


class ColleagueTextField(Colleague):
    def __init__(self):
        self.mediator = None
        self.enabled = False
        self.text = ''

    def set_mediator(self, mediator):
        self.mediator = mediator

    def set_colleague_enabled(self, enabled):
        self.enabled = enabled

    def text_value_changed(self):
        self.mediator.colleague_changed()

    def change(self, text):
        self.text = text
        self.text_value_changed()


class ColleagueCheckBox(Colleague):
    def __init__(self):
        self.mediator = None
        self.enabled = False
        self.is_guest = False

    def set_mediator(self, mediator):
        self.mediator = mediator

    def set_colleague_enabled(self, enabled):
        self.enabled = enabled

    def check_value_changed(self):
        self.mediator.colleague_changed()

    def change(self, is_guest):
        self.is_guest = is_guest
        self.check_value_changed()


class AuthMediator(Mediator):
    def __init__(self):
        self.create_colleagues()

    def create_colleagues(self):
        self.username_field = ColleagueTextField()
        self.username_field.set_mediator(self)

        self.password_field = ColleagueTextField()
        self.password_field.set_mediator(self)

        self.check_field = ColleagueCheckBox()
        self.check_field.set_mediator(self)

        self.click_button = ColleagueButton()
        self.click_button.set_mediator(self)

    def colleague_changed(self):
        if self.check_field.is_guest:
            self.username_field.set_colleague_enabled(False)
            self.password_field.set_colleague_enabled(False)
            self.click_button.set_colleague_enabled(True)
        else:
            self.username_field.set_colleague_enabled(True)
            self._user_pass_changed()

    def _user_pass_changed(self):
        if len(self.username_field.text) > 0:
            self.password_field.set_colleague_enabled(True)
            if len(self.password_field.text) > 0:
                self.click_button.set_colleague_enabled(True)
            else:
                self.click_button.set_colleague_enabled(False)
        else:
            self.password_field.set_colleague_enabled(False)
            self.click_button.set_colleague_enabled(False)


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('Usage with guest: python main.py True')
        print('USage with user: python main.py False [username] [password]')
        sys.exit()

    args += ['', '', '']
    is_guest = strtobool(args[1])
    username = args[2]
    password = args[3]

    mediator = AuthMediator()
    mediator.check_field.change(is_guest)
    mediator.username_field.change(username)
    mediator.password_field.change(password)
    mediator.click_button.do_click()
