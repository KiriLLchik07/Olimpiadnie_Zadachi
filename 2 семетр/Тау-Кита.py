def read_input(file_name):
    with open(file_name, 'r') as f:
        return f.readline()

def generate_circular_word_list(words):
    circular_list = []
    if len(words) % 2 == 0:
        mid_idx = len(words) // 2
        circular_list.append(words[mid_idx])
        for i in range(1, mid_idx + 1):
            circular_list.append(words[mid_idx - i])
            if i < mid_idx:
                circular_list.append(words[mid_idx + i])
    else:
        mid_idx = (len(words) - 1) // 2
        circular_list.append(words[mid_idx])
        for i in range(1, mid_idx + 1):
            circular_list.append(words[mid_idx - i])
            circular_list.append(words[mid_idx + i])
    return circular_list

def generate_palindrome(word):
    palindrome = ""
    if len(word) % 2 == 0:
        middle_idx = len(word) // 2
        palindrome += word[middle_idx]
        for i in range(1, middle_idx + 1):
            palindrome += word[middle_idx - i]
            if i < middle_idx:
                palindrome += word[middle_idx + i]
    else:
        middle_idx = (len(word) - 1) // 2
        palindrome += word[middle_idx]
        for i in range(1, middle_idx + 1):
            palindrome += word[middle_idx - i]
            palindrome += word[middle_idx + i]
    return palindrome

def main():
    input_line = read_input('input_s1_01.txt')
    words = input_line.split(' ')
    circular_word_list = generate_circular_word_list(words)
    palindrome_list = [generate_palindrome(word) for word in circular_word_list]
    output_line = " ".join(palindrome_list)
    print(output_line)

if __name__ == "__main__":
    main()
