import sys
from fgprint import FGPrintInterpreter

def main():
    if len(sys.argv) != 2:
        print("Использование: python run_fgp.py <имя_файла>.fgp")
        return

    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        return
    
    interpreter = FGPrintInterpreter()
    interpreter.run(code)

if __name__ == "__main__":
    main()