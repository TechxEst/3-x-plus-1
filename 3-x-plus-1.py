import matplotlib.pyplot as plt


def even_action(sequence_int):				# Function to deal with even numbers
    if sequence_int % 2 == 0:
        return sequence_int / 2


def odd_action(sequence_int):				# Function to deal with odd numbers
    if sequence_int % 2 == 1:
        return (sequence_int * 3) + 1


def collatze_conjecture():
    sequence_int = int(input("Enter a number: "))
    collection_array = [sequence_int]

    while sequence_int > 1:
        if (sequence_int % 2) == 0:
            sequence_int = even_action(sequence_int)
        else:
            sequence_int = odd_action(sequence_int)

        collection_array.append(int(sequence_int))

    print(collection_array)

    sequence_start = collection_array[0]
    sequence_length = len(collection_array)
    sequence_max = max(collection_array)

    plt.plot(collection_array)
    plt.ylabel('3 X + 1')
    plt.title('Starting Number: {}\nSequence Length: {}\nLargest Number:{}' .format(
        (((sequence_start))),
        ((sequence_length)),
        (((sequence_max)))))
    plt.show()


if __name__ == "__main__":
    collatze_conjecture()
