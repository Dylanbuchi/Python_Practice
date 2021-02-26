class FileHandler():
    """Class to perform operations on files"""
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def write_a_list_to_a_file(
        self,
        filename: str,
        a_list: list,
        sep='\n',
    ) -> None:
        """Takes a list and write it on a file, sep is the separator for the join method default is "\\n"
        
        """
        with open(filename, 'w') as f:
            f.write(sep.join(a_list))