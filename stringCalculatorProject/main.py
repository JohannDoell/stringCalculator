def Add(numbers):
    result = 0
    delimiters = [","]
    base_delimiter = ","
    list_of_addable_numbers = []
    list_of_negative_numbers = []

    def extract_substrings_between_delimiters(string):
        list_of_substrings = []
        last_delimiter_index = 0
        for i in range(len(string)):
            if string[i] == base_delimiter:
                # print(numbers_minus_delimiter[last_delimiter_index:x])
                list_of_substrings.append(string[last_delimiter_index:i])
                last_delimiter_index = i + 1
        # print(numbers_minus_delimiter[last_delimiter_index:])
        list_of_substrings.append(string[last_delimiter_index:])
        # print(list_of_addable_numbers)
        return list_of_substrings

    if numbers == "":
        return result
    else:
        # If the first two characters are "//", find the delimiter
        if numbers[0] == '/' and numbers[1] == '/':
            numbers = numbers.replace('//', '')
            for i in range(len(numbers)):
                if numbers[i] == "\n":
                    delimiters = extract_substrings_between_delimiters(numbers[:i])
                    numbers_minus_delimiter = numbers[i:]
        else:
            numbers_minus_delimiter = numbers

        # We should sanitize out any possible remaining new lines.
        numbers_minus_delimiter = numbers_minus_delimiter.replace('\n', '')
        # print(numbers_minus_delimiter)
        # We should replace each part of the string that is the delimiter with an easier to manipulate substring.
        for i in range(len(delimiters)):
            numbers_minus_delimiter = numbers_minus_delimiter.replace(delimiters[i], base_delimiter)

        # Now extract every number from the string.
        list_of_addable_numbers = extract_substrings_between_delimiters(numbers_minus_delimiter)

        # Add all the numbers we got together.
        for i in range(len(list_of_addable_numbers)):
            number_to_check = int(list_of_addable_numbers[i])
            # Check for negative input.
            if number_to_check < 0:
                list_of_negative_numbers.append(number_to_check)
            # Ignore the number if it's >1000
            elif number_to_check <= 1000:
                result += int(list_of_addable_numbers[i])

        # Throw exception if we found negative input.
        if list_of_negative_numbers:
            raise Exception("Negative input is not allowed. Numbers that caused the error: " +
                            str(list_of_negative_numbers))

        return result


if __name__ == '__main__':
    inputs_and_expected_output = [["", 0], ["1,2,5", 8], ["1\n,2,3", 6], ["1,\n2,4", 7],
                                  ["//;\n1;3;4", 8], ["//$\n1$2$3", 6], ["//@\n2@3@8", 13],
                                  ["2,1001", 2], ["//***\n1***2***3", 6], ["//$,@\n1$2@3", 6],
                                  ["//***,@\n1***2@3", 6]]
    for x in range(len(inputs_and_expected_output)):
        string_input = inputs_and_expected_output[x]
        print(string_input[0] + " => " + str(Add(string_input[0])) + " Expected Output: " + str(string_input[1]) + "\n")

    print(("-1,-2,5 => " + str(Add("-1,-2,5")) + " Expected Output: Exception \n"))
