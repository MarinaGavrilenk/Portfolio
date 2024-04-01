# Номер успешной посылки 110928840

def decoded_instruction(encoded: str, index: int = 0) -> str:
    """Декодирует закодированное сообщение."""
    result = ""
    numbers = ""
    while index < len(encoded):
        element = encoded[index]
        if element.isdigit():
            numbers += element
        elif element == "[":
            inner_command, j = decoded_instruction(encoded, index + 1)
            result += inner_command * int(numbers)
            numbers = ""
            index = j
        elif element == "]":
            return result, index
        else:
            result += element
        index += 1
    
    return result

if __name__ == "__main__":
    print(decoded_instruction(input()))
