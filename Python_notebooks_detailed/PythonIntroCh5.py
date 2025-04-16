# Databricks notebook source
# MAGIC %md
# MAGIC # 5.	Tuples, Lists, and Dictionaries
# MAGIC ## 5.1	Introduction
# MAGIC Your brain still hurting from the last lesson? Never worry, this one will require a little less thought. We're going back to something simple - variables - but a little more in depth.
# MAGIC
# MAGIC Think about it - variables store one bit of information. They may regurgitate (just not on the carpet...) that information at any point, and their bit of information can be changed at any time. Variables are great at what they do - storing a piece of information that may change over time.
# MAGIC
# MAGIC But what if you need to store a long list of information, which doesn't change over time? Say, for example, the names of the months of the year. Or maybe a long list of information that does change over time? Say, for example, the names of all your cats. You might get new cats, some may die, some may become your dinner (we should trade recipies!). What about a phone book? For that you need to do a bit of referencing - you would have a list of names, and attached to each of those names, a phone number. How would you do that?

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5.2	The Solution - Lists, Tuples, and Dictionaries
# MAGIC For these three problems, Python uses three different solutions - Tuples, Lists, and Dictionaries:
# MAGIC * **Lists** are what they seem - a list of values. Each one of them is numbered, starting from zero - the first one is numbered zero, the second 1, the third 2, etc. You can remove values from the list, and add new values to the end. Example: Your many cats' names.
# MAGIC * **Tuples** are just like lists, but you can't change their values. The values that you give it first up, are the values that you are stuck with for the rest of the program. Again, each value is numbered starting from zero, for easy reference. Example: the names of the months of the year.
# MAGIC * **Dictionaries** are similar to what their name suggests - a dictionary. In a dictionary, you have an 'index' of words, and for each of them a definition. In Python, the word is called a 'key', and the definition a 'value'. The values in a dictionary aren't numbered - they aren't in any specific order, either - the key does the same thing. You can add, remove, and modify the values in dictionaries. Example: telephone book.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5.2.1 Tuples
# MAGIC Tuples are pretty easy to make. You give your tuple a name, then after that the list of values it will carry. For example, the months of the year:

# COMMAND ----------

months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')

# COMMAND ----------

# MAGIC %md
# MAGIC * Note that the `\` thingy at the end of the first line carries over that line of code to the next line. It is useful way of making big lines more readable.
# MAGIC * Technically you don't have to put those parentheses there (the `(` and `)` thingies) but it stops Python from getting things confused.
# MAGIC * You may have spaces after the commas if you feel it necessary - it doesn't really matter

# COMMAND ----------

# MAGIC %md
# MAGIC Python then organises those values in a handy, numbered index - starting from zero, in the order that you entered them in. It would be organised like this:<br>
# MAGIC
# MAGIC | Index | Value |
# MAGIC | :---: | :---: |
# MAGIC | 0 | January |
# MAGIC | 1 | February |
# MAGIC | 2 | March |
# MAGIC | 3 | April |
# MAGIC | 4 | May |
# MAGIC | 5 | June |
# MAGIC | 6 | July |
# MAGIC | 7 | August |
# MAGIC | 8 | September |
# MAGIC | 9 | October |
# MAGIC | 10 | November |
# MAGIC | 11 | December |
# MAGIC And that is tuples! Really easy...

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5.2.2 Lists
# MAGIC Lists are extremely similar to tuples. Lists are modifiable (or 'mutable', as a programmer may say), so their values can be changed. Most of the time we use lists, not tuples, because we want to easily change the values of things if we need to.
# MAGIC
# MAGIC Lists are defined very similarly to tuples. Say you have FIVE cats, called Tom, Snappy, Kitty, Jessie and Chester. To put them in a list, you would do this:<br>

# COMMAND ----------

cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']

# COMMAND ----------

# MAGIC %md
# MAGIC As you see, the code is exactly the same as a tuple, EXCEPT that all the values are put between square brackets, not parentheses. Again, you don't have to have spaces after the comma.
# MAGIC
# MAGIC You recall values from lists exactly the same as you do with tuples. For example, to print the name of your 3rd cat you would do this:

# COMMAND ----------

print(cats[2])

# COMMAND ----------

# MAGIC %md
# MAGIC You can also recall a range of examples, like above, for example - `cats[0:2]` would recall your 1st and 2nd cats. Try it in the field above.
# MAGIC
# MAGIC Where lists come into their own is how they can be modified. To add a value to a list, you use the `append()` function. Let's say you got a new cat called Catherine. To add her to the list you'd do this:

# COMMAND ----------

cats.append('Catherine')

# COMMAND ----------

# MAGIC %md
# MAGIC Use the field below to check if the cat has been added to the list.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC That's a little weird, isn't it? I'll explain. That function is in a funny spot - after a period `.` after the list name. You'll get to see those things more in a later lesson. For the meanwhile, this is the form of the function that adds a new value to a list:
# MAGIC ```Python
# MAGIC #add a new value to the end of a list:
# MAGIC list_name.append(value-to-add)
# MAGIC
# MAGIC #e.g. to add the number 5038 to the list 'numbers':
# MAGIC numbers.append(5038)
# MAGIC ```
# MAGIC
# MAGIC Clears things up? Good!
# MAGIC Now to a sad situation - Snappy was shot by a neighbour, and eaten for their dinner (good on 'em!). You need to remove him (or her) from the list. Removing that sorry cat is an easy task, thankfully, so you have to wallow in sadness for as short a time as possible:

# COMMAND ----------

#Remove your 2nd cat, Snappy. Woe is you.
del cats[1]

# COMMAND ----------

# MAGIC %md
# MAGIC Check again which cats are in the list:

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC You've just removed the 2nd cat in your list - poor old Snappy.
# MAGIC And with that morbid message, lets move on to...

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5.3 Dictionaries
# MAGIC Okay, so there is more to life than the names of your cats. You need to call your sister, mother, son, the fruit man, and anyone else who needs to know that their favourite cat is dead. For that you need a telephone book.
# MAGIC
# MAGIC Now, the lists we've used above aren't really suitable for a telephone book. You need to know a number based on someone's name - not the other way around, like what we did with the cats. In the examples of months and cats, we gave the computer a number, and it gave us a name. This time we want to give the computer a name, and it gives us a number. For this we need *Dictionaries*.
# MAGIC
# MAGIC So how do we make a dictionary? Put away your binding equipment, it isn't that advanced.
# MAGIC Remember, dictionaries have keys, and values. In a phone book, you have people's names, then their numbers. See a similarity?
# MAGIC
# MAGIC When you initially create a dictionary, it is very much like making a tuple or list. Tuples have `(` and `)` things, lists have `[` and `]` things. Guess what! Dictionaries have `{` and `}` things - curly braces. Here is an example below, showing a dictionary with four phone numbers in it:

# COMMAND ----------

#Make the phone book:
phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}
print(phonebook['Lewis Lame'])

# COMMAND ----------

# MAGIC %md
# MAGIC When you run it you see that Lewis Lame's number is printed onscreen. Notice how instead of identifying the value by a number, like in the cats and months examples, we identify the value, using another value - in this case the person's name.
# MAGIC
# MAGIC Ok, you've created a new phone book. Now you want to add new numbers to the book. What do you do? A very simple line of code:

# COMMAND ----------

#Add the person 'Gingerbread Man' to the phonebook:

phonebook['Gingerbread Man'] = 1234567

# Didn't think I would give you
# my real number now, would I?

# COMMAND ----------

# MAGIC %md
# MAGIC All that line is saying is that there is a person called Gingerbread Man in the phone book, and his number is `1234567`. In other words - the key is `Gingerbread Man`, and the value is `1234567`.

# COMMAND ----------

# MAGIC %md
# MAGIC Check if it's added using the field below.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC You delete entries in a dictionary just like in a list. Let's say Andrew Parson is your neighbour, and shot your cat. You never want to talk to him again, and therefore don't need his number. Just like in a list, you'd do this:

# COMMAND ----------

del phonebook['Andrew Parson']

# COMMAND ----------

# MAGIC %md
# MAGIC Again, very easy. the `del` operator deletes any function, variable, or entry in a list or dictionary (An entry in a dictionary is just a variable with a number or text string as a name. This comes in handy later on.)

# COMMAND ----------

# MAGIC %md
# MAGIC Check if the number is gone using the field below.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC Remember that append function that we used with the list? Well, there are quite a few of those that can be used with dictionaries. Below, I will write you a program, and it will incorporate some of those functions in. It will have comments along the way explaining what it does. Experiment as much as you like with it.

# COMMAND ----------

#A few examples of a dictionary

#First we define the dictionary
#it will have nothing in it this time
ages = {}

#Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

#Use an 'if' statement to find a key in the list.
#Remember - this is how 'if' statements work -
#they run if something is true
#and they don't when something is false.
if 'Sue' in ages:
    print("Sue is in the dictionary. She is", \
ages['Sue'], "years old")

else:
    print("Sue is not in the dictionary")

#Use the function keys() - 
#This function returns a list
#of all the names of the keys.
#E.g.
print("The following people are in the dictionary:")
print(ages.keys())

#You could use this function to
#put all the key names in a list:
keys = ages.keys()

#You can also get a list
#of all the values in a dictionary.
#You use the values() function:
print("People are aged the following:", \
ages.values())

#Put it in a list:
values = ages.values()

#You can sort lists, with the sorted() function
#It will sort all values in a list
#alphabetically, numerically, etc...
#You can't sort dictionaries - 
#they are in no particular order
print(keys)
sortedkeys = sorted(keys)
print(sortedkeys)

print(values)
sortedvalues = sorted(values)
print(sortedvalues)

#You can find the number of entries
#with the len() function:
print("The dictionary has", \
len(ages), "entries in it")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5.4 Conclusion
# MAGIC There are many other functions you can use to work with lists and dictionaries - too many to go through right now. We'll leave the lesson at this point - you have learnt enough for one lesson.