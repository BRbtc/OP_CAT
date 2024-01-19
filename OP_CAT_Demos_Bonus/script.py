
# Quantum Cats' Rescue of OP_CAT - Script Class
class ScriptError(Exception):
    pass

class Script:
    MAX_SCRIPT_ELEMENT_SIZE = 520

    def __init__(self):
        self.stack = []

    def push(self, element):
        if not isinstance(element, bytes):
            raise ScriptError("Stack elements must be bytes")
        self.stack.append(element)

    def pop(self):
        if not self.stack:
            raise ScriptError("Stack underflow")
        return self.stack.pop()

    def top(self, index):
        if abs(index) > len(self.stack):
            raise ScriptError("Invalid stack access")
        return self.stack[index]

    def op_cat(self):
        if len(self.stack) < 2:
            raise ScriptError("OP_CAT requires at least two elements on the stack")
        vch1 = self.top(-2)
        vch2 = self.top(-1)
        if len(vch1) + len(vch2) > self.MAX_SCRIPT_ELEMENT_SIZE:
            raise ScriptError(f"Result too large (>{self.MAX_SCRIPT_ELEMENT_SIZE} bytes)")
        self.stack[-2] = vch1 + vch2
        self.stack.pop()
