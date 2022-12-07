import aoc_api


class Path:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None
        self.children = {}


class FileSystem:
    def __init__(self):
        self.root = Path('/', 0)
        self.current = self.root

    def execute_command(self, command):
        if command.startswith('$ cd'):
            self.__change_directory(command.split()[2])
        elif not command.startswith('$'):
            self.__add_sub_path(command.split()[1], command.split()[0])

    def __change_directory(self, name):
        match name:
            case '..':
                self.current = self.current.parent
            case '/':
                self.current = self.root
            case _:
                self.current = self.current.children[name]

    def __add_sub_path(self, name, prefix):
        if name in self.current.children:
            return
        sub_path = Path(name, int(prefix) if prefix.isnumeric() else 0)
        sub_path.parent = self.current
        self.current.children[name] = sub_path
        self.__update_size(self.current, sub_path.size)

    def __update_size(self, path, size):
        path.size += size
        if path.parent is not None:
            self.__update_size(path.parent, size)


def solve():
    terminal_output = aoc_api.fetch_input(7)
    file_system = build_file_system(terminal_output)
    directory_sizes = get_directory_sizes(file_system.root)
    print('Total size of directories below 100000: {}'.format(get_small_directories_total_size(directory_sizes)))
    print('Size of smallest directory to delete: {}'.format(
        get_size_of_directory_to_delete(file_system.root, directory_sizes)))


def get_size_of_directory_to_delete(root, directory_sizes):
    required_space = 30000000 - (70000000 - root.size)
    return min(filter(lambda size: size >= required_space, directory_sizes))


def get_small_directories_total_size(directory_sizes):
    return sum(filter(lambda size: size <= 100000, directory_sizes))


def get_directory_sizes(path):
    directory_sizes = [path.size] if len(path.children) > 0 else []
    for sub_path in path.children.values():
        directory_sizes += get_directory_sizes(sub_path)
    return directory_sizes


def build_file_system(terminal_output):
    file_system = FileSystem()
    for command in terminal_output:
        file_system.execute_command(command)
    return file_system
