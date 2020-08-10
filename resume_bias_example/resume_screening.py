# inpiration from:
# 	-	http://gender-decoder.katmatfield.com
# 	-	https://towardsdatascience.com/resume-screening-with-python-1dea360be49b

import re
import string
import os

# CREATE SET OF WORDS CODED BY GENDER
masculine_coded_words, feminine_coded_words = set(), set()

with open("masculine_coded_words.txt", "r") as file:
	for line in file:
		masculine_coded_words.add(line.strip())
file.close()

with open("feminine_coded_words.txt", "r") as file:
	for line in file:
		feminine_coded_words.add(line.strip())
file.close()


# READ IN RESUMES
example_resumes = {}

for filename in os.listdir("resume_examples"):
	path = "resume_examples/" + filename
	text = ""
	with open(path, "r") as f:
		for line in f:
			text += " "
			text += line
		text = text.lower()
		text = re.sub(r'\d+','',text) #removes numbers
		text = text.translate(str.maketrans('','',string.punctuation)) #removes punctuation
		example_resumes[filename] = text
	f.close()


# MEASURE NUMBER OF CODED WORDS IN EACH RESUME
scores = []
for name, resume in example_resumes.items():
	masculine = 0
	feminine = 0
	document = resume.split(" ")
	for word in document:
		word_substring, word_substring_list = "", []
		for letter in word:
			word_substring += letter
			word_substring_list.append(word_substring)

		for substring in word_substring_list:
			if word in masculine_coded_words:
				masculine += 1
				continue
			elif word in feminine_coded_words:
				feminine += 1
				continue

	scores.append((name, masculine, feminine))
		
for i in scores:
	print(f"The number of coded words in the resume called {i[0]} were as follows: {i[1]} words had a masculine encoding and {i[2]} words had a feminine encoding.")
