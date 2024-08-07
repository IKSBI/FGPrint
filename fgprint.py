class FGPrintInterpreter:
    def __init__(self):
        self.variables = {}
    
    def parse_line(self, line):
        line = line.strip()
        if line.startswith('#') or not line:
            return  # Это комментарий или пустая строка
        
        if line.startswith('PRINT'):
            self.handle_print(line)
        elif line.startswith('SET'):
            self.handle_set(line)
        elif line.startswith('GET'):
            self.handle_get(line)
        else:
            print(f"Неизвестная команда: {line}")
    
    def handle_print(self, line):
        # Ожидаем формат: PRINT "текст"
        parts = line.split(' ', 1)
        if len(parts) > 1:
            print(parts[1].strip('"'))
        else:
            print("Ошибка: команда PRINT должна содержать текст.")
    
    def handle_set(self, line):
        # Ожидаем формат: SET var = "значение"
        parts = line.split('=', 1)
        if len(parts) == 2:
            var_part = parts[0].strip()
            value_part = parts[1].strip().strip('"')
            if var_part.startswith('SET'):
                var_name = var_part[3:].strip()
                self.variables[var_name] = value_part
            else:
                print("Ошибка: некорректная команда SET.")
        else:
            print("Ошибка: команда SET должна быть в формате SET var = \"значение\".")
    
    def handle_get(self, line):
        # Ожидаем формат: GET var
        parts = line.split(' ', 1)
        if len(parts) == 2:
            var_name = parts[1].strip()
            value = self.variables.get(var_name)
            if value is not None:
                print(value)
            else:
                print(f"Ошибка: переменная {var_name} не найдена.")
        else:
            print("Ошибка: команда GET должна содержать имя переменной.")
    
    def run(self, code):
        for line in code.splitlines():
            self.parse_line(line)