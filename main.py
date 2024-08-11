def get_file_as_string():
	with open ("books/frankenstein.txt") as f:
		file_string = f.read()
		return file_string

def get_words_in_file(file_string):
	words = file_string.split()
	return words

def get_character_count(file_string):
	lowered_file_contents = file_string.lower()
	character_dict = {}
	
	for char in lowered_file_contents:
		if not char.isalpha():
			continue
		elif char in character_dict:
			character_dict[char] += 1
		else:
			character_dict[char] = 1

	return character_dict


def get_report():
	file_string = get_file_as_string()
	words_in_file = get_words_in_file(file_string)
	character_count = get_character_count(file_string)

	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{len(words_in_file)} words found in document")


	list_of_dicts = []
	for key, value in character_count.items():
		list_of_dicts.append({"char": key, "num": value})

	def sort_on(dict):
		return dict["num"]

	list_of_dicts.sort(reverse=True, key=sort_on)

	print()

	for entry in list_of_dicts:
		print(f"The '{entry["char"]}' character was found {entry["num"]} times")

	print("--- End report ---")




get_report()
