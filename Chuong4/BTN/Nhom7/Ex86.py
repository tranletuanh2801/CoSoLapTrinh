def display_verse(num):
    verses = [
        "a partridge in a pear tree.",
        "two turtle doves,",
        "three French hens,",
        "four calling birds,",
        "five gold rings,",
        "six geese a-laying,",
        "seven swans a-swimming,",
        "eight maids a-milking,",
        "nine ladies dancing,",
        "ten lords a-leaping,",
        "eleven pipers piping,",
        "twelve drummers drumming,"]
    ordinal_numbers = [
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    index = num - 1
    print("On the", ordinal_numbers[index]," day of Christmas my true love sent to me:")
    if index == 0:
        print(verses[index])
    else:
        for i in range(index, 0, -1):
            print(verses[i])
        print("And",verses[0])
    print()
for i in range(1, 13):
    display_verse(i)