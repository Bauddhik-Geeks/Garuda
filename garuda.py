msg=(
    "                                                                                         __..-' \n"
    "     ________                         ___                                          _.--''       \n"
    "    /  _____/_____  _______ __ __  __| _/____                            _...__..-'             \n"
    "   /   \  ___\__  \ \_  __ \  |  \/ __ |\__  \                         .'                       \n"
    "   \    \_\  \/ __ \_|  | \/  |  / /_/ | / __ \_                   .'                           \n"
    "    \______  /____  /|__|  |____/\____ |(____  /                 .'                             \n"
    "           \/     \/                  \/     \/                .'                               \n"
    "                                                              |                                 \n"
    "                                    .------._                 ;                                 \n"
    '------MENU-------              .-"""`-.<'')    `-._           .                                 \n'
    "                             (.--. _   `._       `'---.__.-'                                    \n"
    "   1) PORT Scannner           `   `;'-.-'         '-    ._                                      \n"
    "                                .--'``  '._      - '   .                                        \n"
    "   2) HoneyPot                   `""'-.    `---'    ,                                           \n"
    "                         ''--..__      `\"                                                      \n"
    "                                 ``''---'`\      .'                                             \n"
    "                                           `'. '                                                \n"
    "                                             `'.                                                \n"
)
class bold_color:               # Change colours according to your need 
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
print(bold_color.GREEN)
print(msg)
if __name__ == "__main__":
    while True:
        menu=int(input("Choose      : "))
        if menu in range(1,3):
            break
    if menu==1:
        import scan
        scan.scanner()
    elif menu==2:
        import Honeypot
        Honeypot.honey()
