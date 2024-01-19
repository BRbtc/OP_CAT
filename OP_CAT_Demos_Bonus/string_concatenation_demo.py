
def string_concatenation_demo():
    script = Script()

    input1 = input("Whisper the first secret: ").encode()
    input2 = input("Whisper the second secret: ").encode()

    script.push(input1)
    script.push(input2)
    script.op_cat()

    result = script.pop()
    print("The united secret:", result.decode())

string_concatenation_demo()
