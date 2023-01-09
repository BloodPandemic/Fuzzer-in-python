import requests, sys
from colorama import init, Fore, Style
init()
class Fuzzer:
    def __init__(self, domain, wordlist) -> None:
        self.domain = domain
        self.wordlist = wordlist
    def fuzer(self):
        try:
            f = open('word.txt', 'r').read().split('\n') 
            for line in f:
                if not line:
                    break
                address = self.domain.replace('FUZZ', line)
                response = requests.get(address)
                if response.status_code == 200:
                    print(Fore.GREEN + Style.NORMAL + f"[+++] {address} --> valid ")
                else:
                    print(Fore.BLACK + Style.NORMAL + f"[+++] {address} --> INVALID ")
        except requests.exceptions.ConnectionError as c:
            print(f"{c} Connection is Errored")
        except requests.exceptions.HTTPError as e:
            print(" ERROR ".center(80, "-"))
            print(e, file=sys.stderr)
if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--wordlist", required=True)
    args = parser.parse_args()
    fuz = Fuzzer(args.url, args.wordlist)
    fuz.fuzer()
