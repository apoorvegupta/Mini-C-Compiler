import sys

operators = {'+':'ADD', '-':'SUB', '*':'MUL', '/':'DIV', '<':'LT', '>': 'GT', '<=':'LTE', '>=':'GTE', '==':'EQ', '!=':'NE'}

register_values = {}
register_available = [0, 1, 2, 3, 4, 5, 6, 7]
register_occupied  = []
memory = []

def get_register(operand):
    for key in register_values.keys():
        if(operand == register_values[key]):
            register = key
            register_occupied.remove(register)
            register_occupied.append(register)
            return register, ""
    print("Registers: ", register_values)
    print("Memory: ", memory)
    print("Getting a new register for ", operand)
    if register_available:
        register = register_available.pop(0)
        register_occupied.append(register)
        if operand in memory:
            print("The variable", operand, "was stored in memory")
            assembly = "LDR R" + str(register) + ", " + operand + "\n"
        else:
            print("Stored in register")
            assembly = ""
    else:
        print("Register was not available")
        register = register_occupied.pop(0)
        variable = register_values.pop(register)
        register_occupied.append(register)
        print("Storing", variable, "in memory")
        assembly = "STR " + variable + ", R" + str(register) + "\n"
        if operand in memory:
            assembly += "LDR R" + str(register) + ", " + operand + "\n"
        else:
            memory.append(operand)
    register_values[register] = operand
    print()
    return register, assembly

def generate(icg):
    assembly_code = []
    for line in icg:
        tokens = line.split()
        if len(tokens) == 5:
            op_str = operators[tokens[3]]
            temp_lhs, dest = get_register(tokens[0])
            if tokens[2].isnumeric():
                if tokens[4].isnumeric():
                    assembly = dest + "CMP #" + tokens[2] + ", #" + tokens[4] + "\n"
                    if (op_str == 'EQ'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #1" + "\n" + "MOVNE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'NE'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #0" + "\n" + "MOVNE R" + str(temp_lhs) + ", #1"
                    if (op_str == 'LT'):
                        assembly += "MOVLT R" + str(temp_lhs) + ", #1" + "\n" + "MOVGE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'GT'):
                        assembly += "MOVGT R" + str(temp_lhs) + ", #1" + "\n" + "MOVLE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'LTE'):
                        assembly += "MOVLE R" + str(temp_lhs) + ", #1" + "\n" + "MOVGT R" + str(temp_lhs) + ", #0"
                    if (op_str == 'GTE'):
                        assembly += "MOVGE R" + str(temp_lhs) + ", #1" + "\n" + "MOVLT R" + str(temp_lhs) + ", #0"
                    else:
                        assembly = dest + op_str + " R" + str(temp_lhs) + ", #" + tokens[2] + ", #" + tokens[4]
                else:
                    reg2, src2 = get_register(tokens[4])
                    assembly = dest + src2 + "CMP #" + tokens[2] + ", R" + str(reg2) + "\n"
                    if (op_str == 'EQ'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #1" + "\n" + "MOVNE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'NE'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #0" + "\n" + "MOVNE R" + str(temp_lhs) + ", #1"
                    if (op_str == 'LT'):
                        assembly += "MOVLT R" + str(temp_lhs) + ", #1" + "\n" + "MOVGE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'GT'):
                        assembly += "MOVGT R" + str(temp_lhs) + ", #1" + "\n" + "MOVLE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'LTE'):
                        assembly += "MOVLE R" + str(temp_lhs) + ", #1" + "\n" + "MOVGT R" + str(temp_lhs) + ", #0"
                    if (op_str == 'GTE'):
                        assembly += "MOVGE R" + str(temp_lhs) + ", #1" + "\n" + "MOVLT R" + str(temp_lhs) + ", #0"
                    else:
                        assembly = dest + src + op_str + " R" + str(temp_lhs) + ", #" + tokens[2] + ", R" + str(reg2)
            else:
                reg1, src1 = get_register(tokens[2])
                if tokens[4].isnumeric():
                    assembly = dest + src1 + "CMP R" + str(reg1) + ", #" + tokens[4] + "\n"
                    if (op_str == 'EQ'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #1" + "\n" + "MOVNE R" + str(temp_lhs) + ", #0"
                    elif (op_str == 'NE'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #0" + "\n" + "MOVNE R" + str(temp_lhs) + ", #1"
                    elif (op_str == 'LT'):
                        assembly += "MOVLT R" + str(temp_lhs) + ", #1" + "\n" + "MOVGE R" + str(temp_lhs) + ", #0"
                    elif (op_str == 'GT'):
                        assembly += "MOVGT R" + str(temp_lhs) + ", #1" + "\n" + "MOVLE R" + str(temp_lhs) + ", #0"
                    elif (op_str == 'LTE'):
                        assembly += "MOVLE R" + str(temp_lhs) + ", #1" + "\n" + "MOVGT R" + str(temp_lhs) + ", #0"
                    elif (op_str == 'GTE'):
                        assembly += "MOVGE R" + str(temp_lhs) + ", #1" + "\n" + "MOVLT R" + str(temp_lhs) + ", #0"
                    else:
                        assembly = dest + src1 + op_str + " R" + str(temp_lhs) + ", R" + str(reg1) + ", #" + tokens[4]
                else:
                    reg2, src2 = get_register(tokens[4])
                    assembly = dest + src1 + src2 + "CMP R" + str(reg1) + ", R" + str(reg2) + "\n"
                    if (op_str == 'EQ'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #1" + "\n" + "MOVNE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'NE'):
                        assembly += "MOVEQ R" + str(temp_lhs) + ", #0" + "\n" + "MOVNE R" + str(temp_lhs) + ", #1"
                    if (op_str == 'LT'):
                        assembly += "MOVLT R" + str(temp_lhs) + ", #1" + "\n" + "MOVGE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'GT'):
                        assembly += "MOVGT R" + str(temp_lhs) + ", #1" + "\n" + "MOVLE R" + str(temp_lhs) + ", #0"
                    if (op_str == 'LTE'):
                        assembly += "MOVLE R" + str(temp_lhs) + ", #1" + "\n" + "MOVGT R" + str(temp_lhs) + ", #0"
                    if (op_str == 'GTE'):
                        assembly += "MOVGE R" + str(temp_lhs) + ", #1" + "\n" + "MOVLT R" + str(temp_lhs) + ", #0"
                    else:
                        assembly = dest + src1 + src2 + op_str + " R" + str(temp_lhs) + ", R" + str(reg1) + ", R" + str(reg2)
            assembly_code.append(assembly)
        elif len(tokens) == 4:
            if 'if' in tokens:
                temp, assembly = get_register(tokens[1])
                assembly += "CMP R" + str(temp) + ", #1\nBEQ " + tokens[3]
                assembly_code.append(assembly)
            else:
                temp_lhs, dest = get_register(tokens[0])
                reg, src = get_register(tokens[3])
                assembly = "NOT R" + str(temp_lhs) + ", R" + str(reg)
                assembly_code.append(assembly)
        elif len(tokens) == 3:
            if tokens[2].isnumeric():
                temp, assembly = get_register(tokens[0])
                assembly += "MOV R" + str(temp) + ", #" + tokens[2]
                assembly_code.append(assembly)
            else:
                temp_lhs, dest = get_register(tokens[0])
                reg, src = get_register(tokens[2])
                assembly = dest + src + "MOV R" + str(temp_lhs) + ", R" + str(reg)
                assembly_code.append(assembly)
        elif len(tokens) == 1:
            assembly = tokens[0]
            assembly_code.append(assembly)
        elif 'goto' in tokens:
            assembly = "B " + tokens[1]
            assembly_code.append(assembly)
    return assembly_code


f = open(str(sys.argv[1]), "r")
icg = [line for line in f]
f.close()
print("ICG:")
for line in icg:
    print(line.strip())
print("Assembly code:")
for line in generate(icg):
    print(line)
