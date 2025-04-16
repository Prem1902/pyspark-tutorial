# Databricks notebook source
# MAGIC %md
# MAGIC # 10. Exception Handling
# MAGIC ## 10.1 Introduction
# MAGIC If you haven't seen them before, you're not trying hard enough. What are they? Errors. Exceptions. Problems. Know what I'm talking about? I got it with this program:<br>

# COMMAND ----------

def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end="")
        print(") " + entry)

    return input(question) - 1

# running the function
# remember what the backslash does
answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')

print('You picked answer ' + str(answer + 1))

# COMMAND ----------

# MAGIC %md
# MAGIC This is just an example of the menu program we made earlier. Appears perfectly fine to me. At least until when I first tried it. Run the program, and what happens?

# COMMAND ----------

# MAGIC %md
# MAGIC ## 10.2 Bugs - Human Errors
# MAGIC The most common problems with your code are of your own doing. Sad, but true. What do we see when we try to run our crippled program?
# MAGIC ```Python
# MAGIC ---------------------------------------------------------------------------
# MAGIC TypeError                                 Traceback (most recent call last)
# MAGIC <ipython-input-2-1502b4586513> in <module>()
# MAGIC       8 # running the function
# MAGIC       9 # remember what the backslash does
# MAGIC ---> 10 answer = menu(['A','B','C','D','E','F','H','I'],'Which letter is your favourite? ')
# MAGIC      11 
# MAGIC      12 print('You picked answer ' + str(answer + 1))
# MAGIC
# MAGIC <ipython-input-2-1502b4586513> in menu(list, question)
# MAGIC       4         print(") " + entry)
# MAGIC       5 
# MAGIC ----> 6     return input(question) - 1
# MAGIC       7 
# MAGIC       8 # running the function
# MAGIC
# MAGIC TypeError: unsupported operand type(s) for -: 'str' and 'int'
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Say what? What Python is trying to tell you (but struggling to find a good word for it) is that you can't join a string of letters and a number into one string of text. Let's go through the error message and have a look at how it tells us that:
# MAGIC * `--->` shows the lines where the error is detected. You can see that it first points out line 10 (the string) and then line 6 (the calculation where we subtract an integere from a string). Note that line 6 was in the function.
# MAGIC * `TypeError: unsupported operand type(s) for -: 'str' and 'int'` tells you the error. In this case, it is a 'TypeError', where you tried to subtract incompatible variables

# COMMAND ----------

# MAGIC %md
# MAGIC There are multiple file and code listings for a single error, because the error occurred with the interaction of two lines of code (e.g. when using a function, the error occurred on the line where the function was called, AND the line in the function where things went wrong).
# MAGIC
# MAGIC Now that we know what the problem is, how do we fix it. Well, the error message has isolated where the problem is, so we'll only concentrate on that bit of code.
# MAGIC ```Python
# MAGIC answer = menu(['A','B','C','D','E','F','H','I'],\
# MAGIC 'Which letter is your favourite? ')
# MAGIC ```
# MAGIC This is a call to a function. The error occured in the function in the following line:
# MAGIC ```Python
# MAGIC     return input(question) - 1
# MAGIC ```
# MAGIC `input` always returns a string, hence our problem. Let's change it to `eval(input())`, which, when you type in a number, it returns a number:
# MAGIC ```Python
# MAGIC     return eval(input(question)) - 1
# MAGIC ```
# MAGIC Bug fixed!

# COMMAND ----------

# MAGIC %md
# MAGIC ## 10.3 Exceptions - Limitations of the Code
# MAGIC OK, the program works when you do something normal. But what if you try something weird? Type in a letter (lets say, 'm') instead of a number? Whoops!

# COMMAND ----------

def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end="")
        print(") " + entry)

    return eval(input(question)) - 1

# running the function
# remember what the backslash does
answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')

print('You picked answer ' + str(answer + 1))

# COMMAND ----------

# MAGIC %md
# MAGIC An error occurs in line 10, and the other in line 6. What this is telling us is that when we called the menu function in line 10, an error occured in line 6 (where we take away 1). This makes sense if you know what the `input()` function does - I did a bit of reading and testing, and realised that if you type in a letter or word, it will assume that you are mentioning a variable! so in line 6, we are trying to take 1 away from the variable 'm', which doesn't exist.<br>
# MAGIC
# MAGIC Have no clue on how to fix this? One of the best and easiest ways is to use the `try` and `except` operators.<br>
# MAGIC
# MAGIC Here is an example of `try` being used in a program:
# MAGIC ```Python
# MAGIC try:
# MAGIC     function(world,parameters)
# MAGIC except:
# MAGIC     print(world.errormsg)
# MAGIC ```
# MAGIC This is an example of a really messy bit of code that I was trying to fix. First, the code under `try:` is run. If there is an error, the compiler jumps to the except section and prints `world.errormsg`. The program doesn't stop right there and crash, it runs the code under `except:` then continues on.<br>
# MAGIC
# MAGIC Lets try that where the error occured in our code (line 6). The menu function now is:

# COMMAND ----------

def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end="")
        print(") " + entry)
    try:
        return eval(input(question)) - 1
    except NameError:
        print("Enter a correct number")

# running the function
# remember what the backslash does
answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')

print('You picked answer ' + str(answer + 1))

# COMMAND ----------

# MAGIC %md
# MAGIC Try entering a letter when you're asked for a number and see what happens. Dang. We fixed one problem, but now it has caused another problem further down the track. This happens all the time. (Sometimes you end up going around in circles, because your code is an absolute mess). Let's have a look at the error.<br>
# MAGIC
# MAGIC What has happened this time is that the menu function has returned no value - it only printed an error message. When, at the end of the program, we try to print the returned value plus 1, what is the returned value? There is no returned value? So what is 1 + ... well, we have no clue what we are adding 1 to!<br>
# MAGIC
# MAGIC We could just return any old number, but that would be lying. What we really should to is rewrite the program to cope with this exception. With what? `try` and `except`!

# COMMAND ----------

def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end="")
        print(") " + entry)
    try:
        return eval(input(question)) - 1
    except NameError:
        print("Enter a correct number")

answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')
try:
    print("You picked answer", (answer + 1))
    # you can put stuff after a comma in the 'print' statement,
    # and it will continue as if you had typed in 'print' again
except:
    print("\nIncorrect answer.")
    # the '\n' is for formatting reasons. Try without it and see.

# COMMAND ----------

# MAGIC %md
# MAGIC Problem solved again.
# MAGIC ## 10.4 Endless Errors
# MAGIC The approach that we used above is not recomended. Why? Because apart from the error that we know can happen, `except:` catches every other error too. What if this means we never see an error that could cause problems down the track? If `except:` catches every error under the sun, we have no hope of controlling what errors we deal with, and the other ones that we want to see, because so far we haven't dealt with them. We also have little hope of dealing with more than one type of error in the same block of code. What should one do, when all is hopeless? Here is an example of code with such a situation:

# COMMAND ----------

print("Subtraction program, v0.0.1 (beta)")
a = eval(input('Enter a number to subtract from > '))
b = eval(input('Enter the number to subtract > '))
print(a - b)

# COMMAND ----------

# MAGIC %md
# MAGIC Ok, you enter your two numbers and it works. Enter a letter, and it gives you a `NameError`. Lets rewrite the code to deal with a `NameError` only. We'll put the program in a loop, so it restarts if an error occurs (using `continue`, which starts the loop from the top again, and `break`, which leaves the loop):

# COMMAND ----------

print("Subtraction program, v0.0.2 (beta)")
loop = 1
while loop == 1:
    try:
        a = eval(input('Enter a number to subtract from > '))
        b = eval(input('Enter the number to subtract > '))
    except NameError:
        print("\nYou cannot subtract a letter")
        continue
    print(a - b)
    try:
        loop = eval(input('Press 1 to try again > '))
    except NameError:
        loop = 0

# COMMAND ----------

# MAGIC %md
# MAGIC Here, we restarted the loop if you typed in something wrong. In line 12 we assumed you wanted to quit the program if you didn't press 1, so we quit the program.<br>
# MAGIC
# MAGIC But there are still problems. If we leave something blank, or type in an unusual character like ! or ;, the program gives us a `SyntaxError`. Let's deal with this. When we are asking for the numbers to subtract, we will give a different error message. When we ask to press 1, we will again assume the user wants to quit.

# COMMAND ----------

print("Subtraction program, v0.0.2 (beta)")
loop = 1
while loop == 1:
    try:
        a = eval(input('Enter a number to subtract from > '))
        b = eval(input('Enter the number to subtract > '))
    except NameError:
        print("\nYou cannot subtract a letter")
        continue
    except SyntaxError:
        print("\nPlease enter a number only.")
        continue
    print(a - b)
    try:
        loop = eval(input('Press 1 to try again > '))
    except (NameError,SyntaxError):
        loop = 0

# COMMAND ----------

# MAGIC %md
# MAGIC As you can see, you can have multiple except uses, each dealing with a different problem. You can also have one except to deal with multiple exceptions, by putting them inside parentheses and separating them with commas.<br>
# MAGIC
# MAGIC Now we have a program that is very difficult, to crash by an end user. As a final challenge, see if you can crash it. There is one way I have thought of - if you read the chapter on Human Error carefully, you might know what it is.
# MAGIC
# MAGIC ## 10.5 Conclusion, Sweet Conclusion
# MAGIC There you go! The final lesson on Python! Finally we are finished.