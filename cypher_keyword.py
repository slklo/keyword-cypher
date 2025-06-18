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
            mode = prompt('Выберите режим (1 - Шифровать, 2 - Дешифровать): ').strip()
            if mode in ('1', '2'):
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите '1' или '2'.\n")

        while True:
            lang_choice = prompt('\nВыберите алфабит (1 - eng, 2 - ru): ').strip()
            if lang_choice in ('1', '2'):
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите '1' или '2'.\n")

        while True:
            keyword = prompt('\nВведите ключевое слово: ').strip()
            
            if lang_choice == '1' and any(ch in rus or ch.isdigit() for ch in keyword) :
                print(f'Некорректный ввод. Введите ключ на английском\n')
            elif lang_choice == '2' and any(ch in eng or ch.isdigit() for ch in keyword):
                print(f'Некорректный ввод. Введите ключ на русском\n')
            else: 
                break

        while True:  
            text = prompt("\nВведите текст: ").strip()

            if lang_choice == '1' and any(ch in rus or ch.isdigit() for ch in text):
                print(f'Некорректный ввод. Введите текст на английском\n')
            elif lang_choice == '2' and any(ch in eng or ch.isdigit() for ch in text):
                print(f'Некорректный ввод. Введите текст на русском\n')
            else: 
                break
            
        alphabet = eng if lang_choice == '1' else rus

        cipher = KeywordCipher(keyword, alphabet)
        result = cipher.encode(text) if mode == '1' else cipher.decode(text)

        print("\n\nКлюч:", keyword)
        print("Результат:", result)


        while True:
            continue_choice = prompt("\nХотите выполнить еще одну операцию? (да/нет): ").strip().lower()
            if continue_choice == 'нет':
                print("\nСпасибо за использование! До свидания.")
                return 
            elif continue_choice == 'да':
                break 
            else:
                print("\nНекорректный ввод. Пожалуйста, введите 'да' или 'нет'.\n")


if __name__ == '__main__':
    main()
