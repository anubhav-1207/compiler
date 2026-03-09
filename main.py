from core.interpreter import source_line_interpreter

while True:
    command_line: list = input("~$ : ").strip().split()

    def file_path_extractor(command_line) -> str:
        file_path: str = command_line[2]
        return file_path
    
    def source_file_reader(file_name):
        try:
            with open(file_name,'r') as source_file:
                source_code = source_file.read()
                yield source_code
               
                

        except FileNotFoundError:
            print(f"File Not Found: Please make sure {file_path} is a valid file/directory!")

    def source_line_iterator(source_code):
        for source_line in source_code:
            source_line_interpreter(source_line)
            


    
    file_path = file_path_extractor(command_line)
    source_code = source_file_reader(file_path)
    source_line_iterator(source_code)

    
    