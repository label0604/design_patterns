import os
import shutil
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass


class CreateCommand(Command):
    def __init__(self, path, contents):
        self.path = path
        self.contents = contents

    def execute(self):
        with open(self.path, mode='w', encoding='utf-8') as f:
            f.write(self.contents)

    def unexecute(self):
        os.remove(self.path)


class DeleteCommand(Command):
    def __init__(self, path):
        self.path = path
        self.contents = None

    def execute(self):
        with open(self.path, mode='r') as f:
            self.contents = f.read()
        os.remove(self.path)

    def unexecute(self):
        if self.contents is not None:
            with open(self.path, mode='w', encoding='utf-8') as f:
                f.write(self.contents)


class CopyCommand(Command):
    def __init__(self, path_from, path_to):
        self.path_from = path_from
        self.path_to = path_to

    def execute(self):
        shutil.copyfile(self.path_from, self.path_to)

    def unexecute(self):
        os.remove(self.path_to)


class CompositeCommand(Command):
    def __init__(self):
        self.commands = []

    def append_command(self, cmd):
        self.commands.append(cmd)

    def execute(self):
        for cmd in self.commands:
            cmd.execute()

    def unexecute(self):
        for cmd in reversed(self.commands):
            cmd.unexecute()


if __name__ == '__main__':
    folder1 = "__temp1"
    folder2 = "__temp2"

    print('--- copy file ---')
    print('step1: do nothing')
    print('folder1: ', os.listdir(folder1))
    print('folder2: ', os.listdir(folder2))

    copy_from = folder1 + '/hello1.txt'
    copy_to = folder2 + '/hello1.txt'
    command_mv = CompositeCommand()
    command_mv.append_command(CopyCommand(copy_from, copy_to))

    print('step2: do copy')
    command_mv.execute()
    print('folder1: ', os.listdir(folder1))
    print('folder2: ', os.listdir(folder2))

    print('step3: undo copy')
    command_mv.unexecute()
    print('folder1: ', os.listdir(folder1))
    print('folder2: ', os.listdir(folder2))

    print('--- make and backup ---')
    print('step1: do nothing')
    print('folder1: ', os.listdir(folder1))
    print('folder2: ', os.listdir(folder2))

    create_path = folder1 + '/hello3.txt'
    backup_path = folder2 + '/hello3.txt.backup'
    command_make_and_backup = CompositeCommand()
    command_make_and_backup.append_command(
        CreateCommand(create_path, "hello2"))
    command_make_and_backup.append_command(
        CopyCommand(create_path, backup_path))

    print('step2: do make and backup')
    command_make_and_backup.execute()
    print('folder1: ', os.listdir(folder1))
    print('folder2: ', os.listdir(folder2))

    print('step3: undo make and backup')
    command_make_and_backup.unexecute()
    print('folder1: ', os.listdir(folder1))
    print('folder2: ', os.listdir(folder2))
