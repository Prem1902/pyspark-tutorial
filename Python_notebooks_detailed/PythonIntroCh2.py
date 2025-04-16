# Databricks notebook source
# MAGIC %md
# MAGIC # 2. Programs in a file, variables and strings
# MAGIC ## 2.1 Introduction
# MAGIC Well, we can make one-liner programs. So What? You want to send programs to other people, so that they can use them, without knowing how to write them.
# MAGIC ## 2.2 Writing scripts
# MAGIC Writing programs in Python to a file is VERY easy. Python programs are simply text documents - you can open them up in notepad, and have a look at them, just like that.
# MAGIC In practice, however, you will use a so called __[Integrated Development Environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment)__ to develop your scripts.
# MAGIC
# MAGIC In this tutorial we'll use the Jupyter Notebook interactive fields as an IDE and simulate how we use pythons scripts in files.
# MAGIC
# MAGIC Have a look at the program (`mary.py`) below:

# COMMAND ----------

#A simple program.
print("Mary had a little lamb")
print("it's fleece was white as snow;")
print("and everywhere that Mary went", end = " ")
print("her lamb was sure to go.")

# COMMAND ----------

# MAGIC %md
# MAGIC If you run the script (`<shift> + <Return>`) it will execute lines 1 to 5 after each other. In an IDE there's always a screen where you can type the code with syntax highlighting (like in the cells of this Jupyter Notebook), a window where you can see the output and a button to run the script. The scripts are saved as `.py` files. These can be run from your command line - Open the terminal window, go to the folder and then type `Python mary.py`. Your program will now execute in the command line.
# MAGIC
# MAGIC In line 4 `end = " "` inserts a space instead of a new line at the end of the `print` operator.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2.3 Variables
# MAGIC Now let's start introducing variables. Variables store a value, that can be looked at or changed at a later time. Let's make a program that uses variables:

# COMMAND ----------

#variables demonstrated
print("This program is a demo of variables")
v = 1
print("The value of v is now", v)
v = v + 1
print("v now equals itself plus one, making it worth", v)
v = 51
print("v can store any numerical value, to be used elsewhere.")
print("for example, in a sentence. v is now worth", v)
print("v times 5 equals", v * 5)
print("but v still only remains", v)
print("to make v five times bigger, you would have to type v = v * 5")
v = v * 5
print("there you go, now v equals", v, "and not", v / 5)

# COMMAND ----------

# MAGIC %md
# MAGIC Run the script and try to understand the results.

# COMMAND ----------

# MAGIC %md
# MAGIC Note that we can also write `v = v + 1` as `v += 1`. This can be used for all operators (e.g. `-=`, `*=`,`/=`). Try it in the code above.
# MAGIC
# MAGIC It is good practice to use lowercase for variables. Don't use special characters and don't start with a number!

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2.5 Strings
# MAGIC As you can see, variables store values, for use at a later time. You can change them at any time. You can put in more than numbers, though. Variables can hold things like text. A variable that holds text is called a string. Try this program:

# COMMAND ----------

#giving variables text, and adding text.
word1 = "Good"
word2 = "morning"
word3 = "to you too!"
print(word1, word2)
sentence = word1 + " " + word2 + " " + word3
print(sentence)

# COMMAND ----------

# MAGIC %md
# MAGIC As you see, the variables above were holding text. Variable names can also be longer than one letter - here, we had `word1`, `word2`, and `word3`. As you can also see, strings can be added together to make longer words or sentences. However, it doesn't add spaces in between the words - hence me putting in the `" "` things (there is one space between those).
# MAGIC
# MAGIC Often we need to manipulate strings. For example if we want to edit file names or make selections from text. Strings are similar to `lists` that you will learn later. So similar operations (called *list slicing*) apply to strings.
# MAGIC
# MAGIC Try the following code and explain what it does:

# COMMAND ----------

text = "abcdefghij"
len(text)

# COMMAND ----------

# MAGIC %md
# MAGIC Yes, it shows us the amount of characters in a string.
# MAGIC
# MAGIC Now try this:

# COMMAND ----------

print(text[4])

# COMMAND ----------

# MAGIC %md
# MAGIC Here we want to print the character at position 4. Note that the first character "a" is at position 0! So position 4 gives us back "e".
# MAGIC
# MAGIC Now try:

# COMMAND ----------

print(text[:4])

# COMMAND ----------

print(text[4:])

# COMMAND ----------

# MAGIC %md
# MAGIC Here you see that `[:4]` selects characters 0,1,2,3, which is "abcd". With `[4:]` we start with position 4 (counting from 0!) until the end of the string, which results in "efghij".
# MAGIC
# MAGIC We can also specify a range. Try this:

# COMMAND ----------

print(text[4:8])

# COMMAND ----------

# MAGIC %md
# MAGIC Was it what you expected?
# MAGIC With ranges, the maximum value is not included in the selection.
# MAGIC
# MAGIC We still have the variable `sentence` available. Write code below to select the second word of the sentence using the correct range.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC Now try this:

# COMMAND ----------

print(text[-2])

# COMMAND ----------

# MAGIC %md
# MAGIC What did it do?
# MAGIC
# MAGIC Right, you have selected the second character from the right! Note that here we start counting with -1 for the first character on the right.
# MAGIC
# MAGIC Try this:

# COMMAND ----------

print(text[-4:])

# COMMAND ----------

# MAGIC %md
# MAGIC In human language: start with the 4th character from the right and give me all characters from that position to the end of the string.
# MAGIC
# MAGIC Now try this and find out what it does:

# COMMAND ----------

print(text[::2])

# COMMAND ----------

# MAGIC %md
# MAGIC We can also add the results of the *list slicing* to variables and insert this into strings using the format operation:

# COMMAND ----------

nrOfCharacters = len(sentence)
lastWord = sentence[-4:-1]
print("The sentence has {} characters and the last word is: {}".format(nrOfCharacters,lastWord))

# COMMAND ----------

# MAGIC %md
# MAGIC So you can easily insert variables at the places of the accolades (`{}`). They will be substituted in the same order of the variables in `.format()`

# COMMAND ----------

# MAGIC %md
# MAGIC This can also be written as:

# COMMAND ----------

print(f"The sentence has {nrOfCharacters} characters and the last word is: {lastWord}")

# COMMAND ----------

# MAGIC %md
# MAGIC Besides *list slicing* there are also other operations that we can apply to strings.
# MAGIC We can count the number of occurences of a specific character in a string:

# COMMAND ----------

print(sentence.count('o'))

# COMMAND ----------

# MAGIC %md
# MAGIC We can also find the position of character:

# COMMAND ----------

print(text.find('e'))

# COMMAND ----------

sometext = "Hey you, how are you doing?"
print(sometext.rfind("you"))

# COMMAND ----------

# MAGIC %md
# MAGIC `rfind` returns the lasts occurance of a string. So in `sometext` we have the word "you" twice. `rfind` returns `17` meaning that the last time that it found "you" is starting at position 17 (counting from 0).
# MAGIC
# MAGIC There are a few other useful string operations. Run the code below and will be obvious what it does:

# COMMAND ----------

# Changes the string to upper case
print(sometext.upper())

# Splits the string on a character and returns it as list items. You'll learn about lists later
print(sometext.split(","))

# Replaces strings
print(sometext.replace("?","!"))

# COMMAND ----------

# MAGIC %md
# MAGIC There are also some special characters:
# MAGIC
# MAGIC `\n` jumps to a new line
# MAGIC
# MAGIC `\` is an escape character. You can put it before another character that has a meaning in the code and is not considered a string. This is often used to have strings with backslashes for file names on Windows (e.g. `"C:\\folder\\filename.txt"`). Because `\` is already an escape character we need to use it twice to escape the escape character!
# MAGIC
# MAGIC Examples:

# COMMAND ----------

print("This is a very long sentence and I want to split it into two lines.")
print("This is a very long sentence\nand I want to split it into two lines.")

print("This sentence contains a quote and I don't want the string to end (yet)\"")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2.6 Conclusion
# MAGIC Well done! We now understand longer programs, and know the use of variables. We can also manipulate strings. Next lesson, we look at loops, what they are, and how to use them.