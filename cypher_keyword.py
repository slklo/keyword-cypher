from prompt_toolkit import prompt

class KeywordCipher: 
    def __init__(self, keyword, alphabet):
        self.keyword = keyword
        self.alphabet = alphabet

    def alphabit_generator(self):
        seen = set()

        new_keyword = ''
        for x in self.keyword.lower():
            if x not in seen and x in self.alphabet:
                seen.add(x)
                new_keyword += x

        new_alphabit = ''.join([ch for ch in self.alphabet if ch not in new_keyword])

        return (new_keyword + new_alphabit)


    def encode(self, msg:str) -> str:
        msg = msg.lower()

        encode_alphabit = self.alphabit_generator()

        encoded = ''
        for st in msg: 
            if st in self.alphabet:
                encoded += encode_alphabit[self.alphabet.index(st)]
            else: 
                encoded += st
        return encoded        
    
    def decode(self, msg:str) -> str: 

        decode_alphabit = self.alphabit_generator()

        decoded = ''
        for st in msg: 
            if st in decode_alphabit:
                decoded += self.alphabet[decode_alphabit.index(st)]
            else: 
                decoded += st
        return decoded

def main():

    eng = 'abcdefghijklmnopqrstuvwxyz'
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    while True: 
        while True:
            mode = prompt('Choose mode (1 - encode, 2 - decode): ').strip()
            if mode in ('1', '2'):
                break
            else:
                print("Incorrect input. Please, input '1' or '2'.\n")

        while True:
            lang_choice = prompt('\nChoose alphabet (1 - eng, 2 - ru): ').strip()
            if lang_choice in ('1', '2'):
                break
            else:
                print("Incorrect input. Please, input '1' or '2'.\n")

        while True:
            keyword = prompt('\nInput keyword: ').strip()
            
            if lang_choice == '1' and any(ch in rus or ch.isdigit() for ch in keyword) :
                print(f'Incorrect input. Enter the key in English\n')
            elif lang_choice == '2' and any(ch in eng or ch.isdigit() for ch in keyword):
                print(f'Incorrect input. Enter the key in Russian\n')
            else: 
                break

        while True:  
            text = prompt("\nInput text: ").strip()

            if lang_choice == '1' and any(ch in rus or ch.isdigit() for ch in text):
                print(f'Incorrect input. Enter the key in English\n')
            elif lang_choice == '2' and any(ch in eng or ch.isdigit() for ch in text):
                print(f'Incorrect input. Enter the key in Russian\n')
            else: 
                break
            
        alphabet = eng if lang_choice == '1' else rus

        cipher = KeywordCipher(keyword, alphabet)
        result = cipher.encode(text) if mode == '1' else cipher.decode(text)

        print("\n\nKeyword:", keyword)
        print("Result:", result)


        while True:
            continue_choice = prompt("\nDo you want to perform another operation? (yes/no): ").strip().lower()
            if continue_choice == 'no':
                print("\nThanks for using it! Goodbye.")
                return 
            elif continue_choice == 'yes':
                break 
            else:
                print("\nIncorrect input. Please enter 'yes' or 'no'.\n")


if __name__ == '__main__':
    main()
