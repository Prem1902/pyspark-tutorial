# Databricks notebook source
# MAGIC %md
# MAGIC # 6. For Loop
# MAGIC ## 6.1 Introduction
# MAGIC Well, in the first lesson about loops, I said I would put off teaching you the for loop, until we had reached lists. Well, here it is!
# MAGIC ## 6.2 The `for` Loop
# MAGIC Basically, the `for` loop does something for every value in a list. The way it is set out is a little confusing, but otherwise is very basic. Here is an example of it in code:

# COMMAND ----------

# Example 'for' loop
# First, create a list to loop through:
newList = [45, 'eat me', 90210, "The day has come, the walrus said, \
to speak of many things", -67]

# create the loop:
# Goes through newList, and sequentially puts each bit of information
# into the variable value, and runs the loop
for value in newList:
    print(value)

# COMMAND ----------

# MAGIC %md
# MAGIC As you see, when the loop executes, it runs through all of the values in the list mentioned after `in`. It then puts them into `value`, and executes through the loop, each time with value being worth something different. Let's see it again, in a classic cheerleading call that we all know:

# COMMAND ----------

# cheerleading program
word = input("Who do you go for? ")

for letter in word:
    call = "Gimme a " + letter + "!"
    print(call)
    print(letter + "!")

print("What does that spell?")
print(word + "!")

# COMMAND ----------

# MAGIC %md
# MAGIC A couple of things you've just learnt:
# MAGIC * As you see, strings (remember - strings are lines of text) are just lists with lots of characters.
# MAGIC * The program went through each of the letters (or values) in word, and it printed them onscreen.<br>

# COMMAND ----------

# MAGIC %md
# MAGIC And that is all there is to the for loop.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6.3 Making a Menu Function
# MAGIC Now to the business end of the lesson. Let's start writing programs. So far we have learnt variables, lists, loops, and functions. That is pretty much all we need for quite a bit of programming. So let's set ourselves a task.

# COMMAND ----------

# MAGIC %md
# MAGIC ```Python
# MAGIC # THE MENU FUNCTION
# MAGIC # The program asks for a string with all the menu options in it,
# MAGIC # and a text string asking a question.
# MAGIC # make sure every menu entry is unique.
# MAGIC
# MAGIC def menu(list, question):
# MAGIC     for entry in list:
# MAGIC         print(1 + list.index(entry),end=""))
# MAGIC         print (") " + entry)
# MAGIC
# MAGIC     return eval(input(question)) - 1
# MAGIC
# MAGIC # def menu(list, question): is telling the function to
# MAGIC # ask for two bits of information:
# MAGIC # A list of all the menu entries,
# MAGIC # and the question it will ask when all the options have been printed
# MAGIC
# MAGIC # for entry in list: is pretty much saying;
# MAGIC #'for every entry in the list, do the following:'
# MAGIC
# MAGIC # print list.index(entry) + 1 uses the .index() function to find
# MAGIC # where in the list the entry is in. print function then prints it
# MAGIC # it adds 1 to make the numbers more intelligible.
# MAGIC
# MAGIC # print ") " + entry prints a bracket, and then the entry name
# MAGIC
# MAGIC # after the for loop is finished, eval(input(question) - 1) asks the question,
# MAGIC # and returns the value to the main program (minus 1, to turn it back to
# MAGIC # the number the computer will understand).
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC That wasn't very difficult, was it? The actual program only took up five lines - this is the wonder of how much we have learnt so far! All my comments take up sixteen lines - more than three times the program length. It is a good idea to comment your programs extensively. Remember that if you are going to be publishing your code open-source, there are going to be a lot of people checking out the code that you have written. We'll see the function we just wrote in our first example program.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6.4 Our First 'Game'
# MAGIC What will our first example program be? How about a (very) simple text adventure game? Sounds like fun! It will only encompass one room of a house, and will be extremely simple. There will be five things, and a door. In one of the five things, is a key to the door. You need to find the key, then open the door. I will give a plain-english version first, then do it in Python:<br>
# MAGIC ```
# MAGIC #Plain-english version of our 'game'
# MAGIC
# MAGIC Tell the computer about our menu function
# MAGIC
# MAGIC Print a welcoming message, showing a description of the room.
# MAGIC We will give the player six things to look at: pot plant, painting,\
# MAGIC  vase, lampshade, shoe, and the door
# MAGIC
# MAGIC Tell the computer that the door is locked
# MAGIC Tell the computer where the key is
# MAGIC
# MAGIC present a menu, telling you what things you can 'operate':
# MAGIC     It will give you the six options
# MAGIC     It will ask the question "what will you look at?"
# MAGIC
# MAGIC if the user wanted to look at:
# MAGIC     pot plant:
# MAGIC         If the key is here, give the player the key
# MAGIC         otherwise, tell them it isn't here
# MAGIC     painting:
# MAGIC         same as above
# MAGIC     etc.
# MAGIC     door:
# MAGIC         If the player has the key, let them open the door
# MAGIC         Otherwise, tell them to look harder
# MAGIC
# MAGIC Give the player a well done message, for completing the game.
# MAGIC ```
# MAGIC <br>
# MAGIC From this, we can write a real program. Ready? Here it is:

# COMMAND ----------

# TEXT ADVENTURE GAME

#the menu function:
def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end="")
        print (") " + entry)

    return eval(input(question)) - 1

#Give the computer some basic information about the room:
items = ["pot plant","painting","vase","lampshade","shoe","door"]

#The key is in the vase (or entry number 2 in the list above):
keylocation = 2

#You haven't found the key:
keyfound = 0

loop = 1

#Give some introductary text:
print("Last night you went to sleep in the comfort of your own home.")

print("Now, you find yourself locked in a room. You don't know how")
print("you got there, or what time it is. In the room you can see")
print(len(items), "things:")
for x in items:
    print(x)
print("")
print("The door is locked. Could there be a key somewhere?")
#Get your menu working, and the program running until you find the key:
while loop == 1:
    choice = menu(items,"What do you want to inspect? ")
    if choice == 0:
        if choice == keylocation:
            print("You found a small key in the pot plant.")

            print("")
            keyfound = 1
        else:
            print("You found nothing in the pot plant.")
            print("")
    elif choice == 1:
        if choice == keylocation:
            print("You found a small key behind the painting.")
            print("")

            keyfound = 1
        else:
            print("You found nothing behind the painting.")
            print("")
    elif choice == 2:
        if choice == keylocation:
            print("You found a small key in the vase.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the vase.")

            print("")
    elif choice == 3:
        if choice == keylocation:
            print("You found a small key in the lampshade.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the lampshade.")
            print("")

    elif choice == 4:
        if choice == keylocation:
            print("You found a small key in the shoe.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the shoe.")
            print("")
    elif choice == 5:
        if keyfound == 1:
            loop = 0
            print("You put in the key, turn it, and hear a click")

            print("")
        else:
            print("The door is locked, you need to find a key.")
            print("")

# Remember that a backslash continues
# the code on the next line
print("Light floods into the room as \
you open the door to your freedom.")


# COMMAND ----------

# MAGIC %md
# MAGIC Well, a very simple, but fun, game. Don't get daunted by the amount of code there, 53 of the lines are just the `if` statements, which is the easiest thing to read there (Once you comprehend all the indentation. Soon you'll make your own game, and you can make it as simple (or as complex) as you like. I'll post quite a few, later.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6.5 Making the Game Better
# MAGIC The first question you should ask is "does this program work?". The answer here is yes. Then you should ask "does this program work well?" - not quite. The `menu()` function is great - it reduces a lot of typing. The `while` loop that we have, however, is a little messy - four levels of indents, for a simple program. We can do better!
# MAGIC
# MAGIC Now, this will become much MUCH more straightforward when we introduce classes. But that will have to wait. Until then, let's make a function that reduces our mess. It we will pass two things to it - the menu choice we made, and the location of the key. It will return one thing - whether or not the key has been found. Lets see it:
# MAGIC
# MAGIC ```Python
# MAGIC def inspect(choice,location):
# MAGIC     if choice == location:
# MAGIC         print("")
# MAGIC         print("You found a key!")
# MAGIC         print("")
# MAGIC         return 1
# MAGIC     else:
# MAGIC         print("")
# MAGIC         print("Nothing of interest here.")
# MAGIC         print("")
# MAGIC         return 0
# MAGIC ```
# MAGIC
# MAGIC
# MAGIC Now the main program can be a little simpler.
# MAGIC
# MAGIC In the field below:
# MAGIC
# MAGIC 1. Insert the `inspect` function
# MAGIC 2. Replace the `while` loop with:
# MAGIC
# MAGIC ```Python
# MAGIC while loop == 1:
# MAGIC     keyfound = inspect(menu(items,"What do you want to inspect? "),keylocation)
# MAGIC     if keyfound == 1:
# MAGIC         print("You put the key in the lock of the door, and turn it. It opens!")
# MAGIC         loop = 0
# MAGIC ```

# COMMAND ----------

# TEXT ADVENTURE GAME

#the menu function:
def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end="")
        print (") " + entry)

    return eval(input(question)) - 1

#Give the computer some basic information about the room:
items = ["pot plant","painting","vase","lampshade","shoe","door"]

#The key is in the vase (or entry number 2 in the list above):
keylocation = 2

#You haven't found the key:
keyfound = 0

loop = 1

#Give some introductary text:
print("Last night you went to sleep in the comfort of your own home.")

print("Now, you find yourself locked in a room. You don't know how")
print("you got there, or what time it is. In the room you can see")
print(len(items), "things:")
for x in items:
    print(x)
print("")
print("The door is locked. Could there be a key somewhere?")
#Get your menu working, and the program running until you find the key:
while loop == 1:
    choice = menu(items,"What do you want to inspect? ")
    if choice == 0:
        if choice == keylocation:
            print("You found a small key in the pot plant.")

            print("")
            keyfound = 1
        else:
            print("You found nothing in the pot plant.")
            print("")
    elif choice == 1:
        if choice == keylocation:
            print("You found a small key behind the painting.")
            print("")

            keyfound = 1
        else:
            print("You found nothing behind the painting.")
            print("")
    elif choice == 2:
        if choice == keylocation:
            print("You found a small key in the vase.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the vase.")

            print("")
    elif choice == 3:
        if choice == keylocation:
            print("You found a small key in the lampshade.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the lampshade.")
            print("")

    elif choice == 4:
        if choice == keylocation:
            print("You found a small key in the shoe.")
            print("")
            keyfound = 1
        else:
            print("You found nothing in the shoe.")
            print("")
    elif choice == 5:
        if keyfound == 1:
            loop = 0
            print("You put in the key, turn it, and hear a click")

            print("")
        else:
            print("The door is locked, you need to find a key.")
            print("")

# Remember that a backslash continues
# the code on the next line
print("Light floods into the room as \
you open the door to your freedom.")

# COMMAND ----------

# MAGIC %md
# MAGIC Now the program becomes massively shorter - from a cumbersome 83 lines, to a very shapely 50 lines! Of course, you lose quite a bit of versatility - all the items in the room do the same thing. You automatically open the door when you find the key. The game becomes a little less interesting. It also becomes a little harder to change.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6.6 Conclusion
# MAGIC Now I said you would write some programs now. Here is your chance! Your task, if you choose to accept it, is to post a better text adventure game. You can use any of the code I have given you here. Remember to check back on previous lessons we have done - they are priceless tools. Do a search for some simple text adventure games - if you find some nice, fun text adventure games, have a look at them.