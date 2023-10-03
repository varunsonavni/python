alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# print(len(alphabet))

#! hello
        # new_text = alphabet.index()
def caesar(direction, text, shift):
    answer = ""
    if direction == "decode":
        shift = shift * -1

    for i in text: 
        # 26
        if i not in alphabet:
            answer += i
        else:
            index = alphabet.index(i)
            if index + shift >= len(alphabet):
                new_index = index + shift - len(alphabet)
                answer += alphabet[new_index]
            else: 
                answer += alphabet[index + shift]
        
    print(answer)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'exit' for exit:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)    