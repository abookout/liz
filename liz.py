import json
import re
import pronouncing


def get_phones(word):
    """ 
    word is a string (e.g. "liz")
    return a list of phonemes (e.g. ['L','IH','Z']) or an empty list if
        there were no phonemes found
    """
    phones = pronouncing.phones_for_word(word)
    if len(phones) == 0: return []
    if isinstance(phones, list):
        phones = phones[0]  # for now only use the first dialect

    # remove all numbers and separate into a list by whitespace
    return [re.sub(r"\d+", "", x) for x in phones.split(" ")]


def check_sublist(sub, super):
    """
    return true if the list sub is a sublist of super, false otherwise.
    """
    if len(super) < len(sub): return False

    for i in range(len(super)-len(sub)+1):
        if super[i:i+len(sub)] == sub:
            return True

    return False


def main():
    results = set()
    name = input("Please enter a nickname to find full names for (e.g. 'liz')\n")
    name_phones = get_phones(name)
    if len(name_phones) == 0:
        print(f"No pronouciations found for the name '{name}'.")
        return
    print("pronunciations for name: ", name_phones)
    
    with open("dictionary.json", "r") as f:
        for line in f:
            word = json.loads(line)["word"]
            try:
                word_phones = get_phones(word)
                if len(word_phones) == 0: continue

                if check_sublist(name_phones, word_phones):
                    if word not in results:
                        print(word)
                        results.add(word)
            except KeyError:
                continue

    print(f"DONE! Found {len(results)} unique words.")


if __name__ == "__main__":
    main()