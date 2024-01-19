
def byte_array_concatenation_demo():
    script = Script()

    def hex_to_bytes(hex_string):
        return bytes.fromhex(hex_string)

    input1 = hex_to_bytes(input("Cast the first byte array in hex (e.g., '01ff'): "))
    input2 = hex_to_bytes(input("Cast the second byte array in hex (e.g., 'a1b2'): "))

    script.push(input1)
    script.push(input2)
    script.op_cat()

    result = script.pop()
    print("The forged byte array in Hex:", result.hex())

byte_array_concatenation_demo()
