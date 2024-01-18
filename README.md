# OP_CAT
Script possibly utilising OP_CAT -> "[Utilising_OP_CAT](https://github.com/BRbtc/OP_CAT/blob/main/Utilising_OP_CAT)"

## OP_CAT Basics
Bitcoin script basics
https://www.youtube.com/watch?v=6Fa04MnURhw

## OP_CAT Basics

    Opcode (decimal): 126
    Opcode (hex): 0x7e

`OP_CAT` takes two byte arrays from the stack, concatenates(links) them and pushes the result back to the stack.

    x1 x2 OP_CAT → out

Example:

* `0x69 0x420 OP_CAT → 0x69420`

