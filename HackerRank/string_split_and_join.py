def split_and_join(line):
    # write your code here
    word_list = line.split()
    joined_words = "-".join(word_list)
    return joined_words

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
