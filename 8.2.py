alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# print(len(alphabet))

#! hello
def encrypt(text, shift):
    answer = ""
    for i in text: 
        # 26
        index = alphabet.index(i)
        if index + shift >= len(alphabet):
            new_index = index + shift - len(alphabet)
            answer = answer + alphabet[new_index]
        else:
            answer = answer + alphabet[index + shift]
          
    print(answer)

def decrypt(text, shift):
    answer = ""
    for i in text: 
        # 26
        # if alphabet.index(i):
        index = alphabet.index(i)
        if index - shift >= 0:              # 3 - 2 = 1
            new_index = index - shift
            answer = answer + alphabet[new_index]
        else:
            answer = answer + alphabet[index - shift]
    # else:
    #     answer = answer + i
          
    print(answer)
        # new_text = alphabet[index + shift]
        # print(new_text)
        # new_text = alphabet.index()
        
        # new_text = alphabet[index + shift]
        # print(new_text)
        # new_text = alphabet.index()

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    elif direction == "exit":
        print("Exitting...")
        exit(1)
    else:
        print("Invalid input")
        exit(1)