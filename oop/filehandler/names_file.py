from .file_handler import FileHandler


class NamesFile(FileHandler):
    """Class to perform operations on a file that contains names"""
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        self.names = self.get_names_from_file(filename)

    def get_names_from_file(self, filename: str) -> list[str]:
        with open(filename) as f:
            return f.read().splitlines()

    def get_names_lengths(self) -> list[int]:
        return list(map(lambda x: len(x), self.names))

    def get_longest_name(self) -> str:
        return max(self.names, key=len)

    def get_total_sum_of_names_length(self) -> int:
        return sum(self.get_names_lengths())

    def get_average_names_length(self) -> float:
        total_sum = self.get_total_sum_of_names_length()
        length = len(self.names)
        return f"{total_sum / length:.2f}"

    def get_shortest_name(self) -> str:
        names_lengths = self.get_names_lengths()
        min_length = min(names_lengths)
        shortest_names = list(
            filter(lambda x: len(x) == min_length, self.names))
        return shortest_names

    def print_shortest_names(self) -> None:
        print('\n'.join([name for name in self.get_shortest_name()]))

    def create_names_lengths_file(self, filename: str) -> None:
        self.write_a_list_to_a_file(filename,
                                    list(map(str, self.get_names_lengths())))

    def create_sorted_names_file(self, filename: str) -> None:
        sorted_names = sorted(self.names)
        self.write_a_list_to_a_file(filename, list(map(str, sorted_names)))

    def create_sorted_names_by_length_file(self, filename: str) -> None:
        sorted_names_by_length = sorted(self.names, key=len)
        self.write_a_list_to_a_file(filename,
                                    list(map(str, sorted_names_by_length)))
