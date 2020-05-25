
# https://www.youtube.com/watch?v=JbnjusltDHk
import sys

def main():
    print("Gob's Program:  Y/N?")
    user_input = input("?")
    if user_input.lower() == 'y':
        while True:
            sys.stdout.write('Penus ')
    elif user_input.lower() == 'n':
        exit()
    else:
        print(chr(27) + "[2J")
        main()

if __name__ == '__main__':
    sys.stdout.write('\033[92m')
    try:
        main()
    except:
        pass
    sys.stdout.write('\033[0m')

