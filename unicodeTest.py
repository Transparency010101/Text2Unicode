from colorama import init
from colorama import Fore, Back
init()

def enCodeUc(text = ""):
    return text.encode("utf-8")


def deCodeUc(text ="" ):
    return text.decode("utf-8")


if __name__ == "__main__":
	# Это для того чтобы было
    print("Start!")

inpText = input(Back.MAGENTA + "Str: ")

end = enCodeUc(inpText)
print(Back.GREEN + "Перекодировано: ", end)
print(Back.RED + "Для убедительности: ", deCodeUc(end))

input()
