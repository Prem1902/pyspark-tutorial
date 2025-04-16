# Databricks notebook source
# MAGIC %md
# MAGIC # 4. Functions
# MAGIC ## 4.1 Introduction
# MAGIC Last lesson I said that we would delve into purposeful programming. That involves user input, and user input requires a thing called functions.
# MAGIC
# MAGIC What are functions? Well, in effect, functions are little self-contained programs that perform a specific task, which you can incorporate into your own, larger programs. After you have created a function, you can use it at any time, in any place. This saves you the time and effort of having to retell the computer what to do every time it does a common task, for example getting the user to type something in.
# MAGIC
# MAGIC ## 4.2 Using a Function
# MAGIC Python has lots of pre-made functions, that you can use right now, simply by 'calling' them. 'Calling' a function involves you giving a function input, and it will return a value (like a variable would) as output. Don't understand? Here is the general form that calling a function takes:<br>
# MAGIC `function_name(parameters)`
# MAGIC
# MAGIC See? Easy.
# MAGIC
# MAGIC - `Function_name` identifies which function it is you want to use (You'd figure...). For example, the function `raw_input`, which will be the first function that we will use.
# MAGIC - `Parameters` are the values you pass to the function to tell it what is should do, and how to do it... for example, if a function multiplied any given number by five, the stuff in parameters tells the function which number it should multiply by five. Put the number 70 into parameters, and the function will do 70 x 5.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4.3 Parameters and Returned Values - Communicating with Functions
# MAGIC Well, that's all well and good that the program can multiply a number by five, but what does it have to show for it? A warm fuzzy feeling? Your program needs to see the results of what happened, to see what 70 x 5 is, or to see if there is a problem somewhere (like you gave it a letter instead of a number). So how does a function show what is does?
# MAGIC
# MAGIC Well, in effect, when a computer runs a function, it doesn't actually see the function name, but the result of what the function did. Variables do the exact same thing - the computer doesn't see the variable name, it sees the value that the variable holds. Let's call this program that multiplied any number by five, `multiply()`. You put the number you want multiplied in the brackets. So if you typed this:
# MAGIC
# MAGIC `a = multiply(70)`
# MAGIC
# MAGIC The computer would actually see this:
# MAGIC
# MAGIC `a = 350`
# MAGIC
# MAGIC Note: don't bother typing in this code - `multiply()` isn't a real function, unless you create it.
# MAGIC
# MAGIC The function ran itself, then returned a number to the main program, based on what parameters it was given.
# MAGIC
# MAGIC Now let's try this with a real function, and see what it does. The function is called `input`, and asks the user to type in something. It then turns it into a string of text. Try the code below:

# COMMAND ----------

# this line makes 'a' equal to whatever you type in
a = input("Type in something, and it will be repeated on screen: ")
# this line prints what 'a' is now worth
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC Say in the above program, you typed in `hello` when it asked you to type something in. To the computer, this program would look like this:
# MAGIC
# MAGIC ```Python
# MAGIC a = "hello"
# MAGIC print("hello")
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Remember, a variable is just a stored value. To the computer, the variable `a` doesn't look like `a` - it looks like the value that is stored inside it. Functions are similar - to the main program (that is, the program that is running the function), they look like the value of what they give in return of running.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4.4 A Calculator Program
# MAGIC Let's write another program, that will act as a calculator. This time it will do something more adventurous than what we have done before. There will be a menu, that will ask you whether you want to multiply two numbers together, add two numbers together, divide one number by another, or subtract one number from another. Only problem - the `input` function returns what you type in as a string - we want the number 1, not the letter 1 (and yes, in Python, there is a difference).
# MAGIC
# MAGIC Luckily, somebody wrote the function `eval`, which returns what you typed in, to the main program - but this time, it puts it in as a number. If you type an integer (a whole number), what comes out of input is an integer. And if you put that integer into a variable, the variable will be an integer-type variable, which means you can add and subtract, etc.

# COMMAND ----------

# this line makes 'a' equal to the value that you type. It doesn't accept strings
a = eval(input("Type in something, and it will be repeated on screen: "))
# this line prints what 'a' is now worth
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC Now, let's design this calculator properly. We want a menu that is returned to every time you finish adding, subtracting, etc. In other words, to loop (HINT!!!) while (BIG HINT!!!) you tell it the program should still run.
# MAGIC We want it to do an option in the menu if you type in that number. That involves you typing in a number (a.k.a. input) and an `if` loop.<br>
# MAGIC Let's write it out in understandable English first (pseudocode):
# MAGIC
# MAGIC ```
# MAGIC START PROGRAM
# MAGIC print opening message
# MAGIC
# MAGIC while we let the program run, do this:
# MAGIC     #Print what options you have
# MAGIC     print Option 1 - add
# MAGIC     print Option 2 - subtract
# MAGIC     print Option 3 - multiply
# MAGIC     print Option 4 - divide
# MAGIC     print Option 5 - quit program
# MAGIC
# MAGIC     ask for which option it is you want
# MAGIC     if it is option 1:
# MAGIC         ask for first number
# MAGIC         ask for second number
# MAGIC         add them together
# MAGIC         print the result onscreen
# MAGIC     if it is option 2:
# MAGIC         ask for first number
# MAGIC         ask for second number
# MAGIC         subtract one from the other
# MAGIC         print the result onscreen
# MAGIC     if it is option 3:
# MAGIC         ask for first number
# MAGIC         ask for second number
# MAGIC         multiply!
# MAGIC         print the result onscreen
# MAGIC     if it is option 4:
# MAGIC         ask for first number
# MAGIC         ask for second number
# MAGIC         divide one by the other
# MAGIC         print the result onscreen
# MAGIC     if it is option 5:
# MAGIC         tell the loop to stop looping
# MAGIC Print onscreen a goodbye message
# MAGIC END PROGRAM
# MAGIC ```
# MAGIC Let's put this in something that Python can understand:

# COMMAND ----------

#calculator program

#this variable tells the loop whether it should loop or not.
#1 means loop. Anything else means don't loop.

loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:
    #print what options you have
    print("Welcome to calculator.py")

    print("your options are:")
    print(" ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit calculator.py")
    print(" ")

    choice = eval(input("Choose your option: "))
    if choice == 1:
        add1 = eval(input("Add this: "))
        add2 = eval(input("to this: "))
        print(add1, "+", add2, "=", add1 + add2)
    elif choice == 2:
        sub2 = eval(input("Subtract this: "))
        sub1 = eval(input("from this: "))
        print(sub1, "-", sub2, "=", sub1 - sub2)
    elif choice == 3:
        mul1 = eval(input("Multiply this: "))
        mul2 = eval(input("with this: "))
        print(mul1, "*", mul2, "=", mul1 * mul2)
    elif choice == 4:
        div1 = eval(input("Divide this: "))
        div2 = eval(input("by this: "))
        print(div1, "/", div2, "=", div1 / div2)
    elif choice == 5:
        loop = 0
        
print("Thank you for using calculator.py!")

# COMMAND ----------

# MAGIC %md
# MAGIC Play around with it - try all options, entering in integers (numbers without decimal points), and numbers with stuff after the decimal point (known in programming as a floating point). Try typing in text, and see how the program chucks a minor fit, and stops running (that can be dealt with, using error handling, which we can address later).

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4.5 Define Your Own Functions
# MAGIC Well, it is all well and good that you can use other people's functions, but what if you want to write your own functions, to save time, and maybe use them in other programs? This is where the `def` operator comes in. (An operator is just something that tells Python what to do, e.g. the `+` operator tells Python to add things, the `if` operator tells Python to do something if conditions are met.)
# MAGIC
# MAGIC This is how the `def` operator works:
# MAGIC
# MAGIC ```
# MAGIC def function_name(parameter_1,parameter_2):
# MAGIC     {this is the code in the function}
# MAGIC     {more code}
# MAGIC     {more code}
# MAGIC     return {value to return to the main program}
# MAGIC {this code isn't in the function}
# MAGIC {because it isn't indented}
# MAGIC #remember to put a colon ":" at the end
# MAGIC #of the line that starts with 'def'
# MAGIC ```
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC `function_name` is the name of the function. You write the code that is in the function below that line, and have it indented. (We will worry about `parameter_1` and `parameter_2` later, for now imagine there is nothing between the parentheses.
# MAGIC
# MAGIC Functions run completely independent of the main program. Remember when I said that when the computer comes to a function, it doesn't see the function, but a value, that the function returns? Here's the quote:
# MAGIC
# MAGIC To the computer, the variable 'a' doesn't look like 'a' - it looks like the value that is stored inside it. Functions are similar - to the main program (that is, the program that is running the function), they look like the value of what they give in return of running.

# COMMAND ----------

# MAGIC %md
# MAGIC A function is like a miniature program that some parameters are given to - it then runs itself, and then returns a value. Your main program sees only the returned value. If that function flew to the moon and back, and then at the end had:
# MAGIC
# MAGIC `return "hello"`
# MAGIC
# MAGIC then all your program would see is the string `"hello"`, where the name of the function was. It would have no idea what else the program did.
# MAGIC
# MAGIC Because it is a separate program, a function doesn't see any of the variables that are in your main program, and your main program doesn't see any of the variables that are in a function. For example, here is a function that prints the words `"hello"` onscreen, and then returns the number `'1234'` to the main program:

# COMMAND ----------

# Below is the function
def hello():
    print("hello")
    return 1234

# And here is the function being used
print(hello())

# COMMAND ----------

# MAGIC %md
# MAGIC So what happened?
# MAGIC 1.	when `def hello()` was run, a function called `hello` was created
# MAGIC 2.	When the line `print(hello())` was run, the function `hello` was executed (The code inside it was run)
# MAGIC 3.	The function `hello` printed `"hello"` onscreen, then returned the number `1234` back to the main program
# MAGIC 4.	The main program now sees the line as `print("1234")` and as a result, printed `1234`

# COMMAND ----------

# MAGIC %md
# MAGIC That accounts for everything that happened. Remember, that the main program had NO IDEA that the words `hello` were printed onscreen. All it saw was `1234`, and printed that onscreen.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4.6 Passing Parameters to functions
# MAGIC There is one more thing we will cover in this (monstrously huge) lesson - passing parameters to a function. Think back to how we defined functions:<br>
# MAGIC ```
# MAGIC def function_name(parameter_1,parameter_2):
# MAGIC     {this is the code in the function}
# MAGIC     {more code}
# MAGIC     {more code}
# MAGIC     return {value (e.g. text or number) to return to the main program}
# MAGIC ```
# MAGIC
# MAGIC Where `parameter_1` and `parameter_2` are (between the parentheses), you put the names of variables that you want to put the parameters into. Put as many as you need, just have them seperated by commas. When you run a function, the first value you put inside the parentheses would go into the variable where `parameter_1` is. The second one (after the first comma) would go to the variable where `parameter_2` is. This goes on for however many parameters there are in the function (from zero, to the sky). For example:

# COMMAND ----------

def funnyfunction(first_word,second_word,third_word):
    print("The word created is: " + first_word + second_word + third_word)
    return first_word + second_word + third_word

# COMMAND ----------

# MAGIC %md
# MAGIC When you run the function above, you would type in something like this: `funnyfunction("meat","eater","man")`. The first value (that is, "meat") would be put into the variable called first_word. The second value inside the brackets (that is, "eater") would be put into the variable called second_word, and so on. This is how values are passed from the main program to functions - inside the parentheses, after the function name.
# MAGIC
# MAGIC Add a new line to the script above that invokes the function.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4.7 A Final Program
# MAGIC Think back to that calculator program. Did it look a bit messy to you? I think it did, so let's re-write it, with functions.
# MAGIC
# MAGIC To design - First we will define all the functions we are going to use with the `def` operator (still remember what an operator is ;) ). Then we will have the main program, with all that messy code replaced with nice, neat functions. This will make it so much easier to look at again in the future.

# COMMAND ----------

# calculator program

# NO CODE IS REALLY RUN HERE, IT IS ONLY TELLING US WHAT WE WILL DO LATER
# Here we will define our functions
# this prints the main menu, and prompts for a choice
def menu():
    #print what options you have
    print("Welcome to calculator.py")
    print("your options are:")
    print(" ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit calculator.py")
    print(" ")
    return eval(input("Choose your option: "))
    
# this adds two numbers given
def add(a,b):
    print(a, "+", b, "=", a + b)
    
# this subtracts two numbers given
def sub(a,b):
    print(b, "-", a, "=", b - a)
    
# this multiplies two numbers given
def mul(a,b):
    print(a, "*", b, "=", a * b)
    
# this divides two numbers given
def div(a,b):
    print(a, "/", b, "=", a / b)
    
# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(eval(input("Add this: ")),eval(input("to this: ")))
    elif choice == 2:
        sub(eval(input("Subtract this: ")),eval(input("from this: ")))
    elif choice == 3:
        mul(eval(input("Multiply this: ")),eval(input("by this: ")))
    elif choice == 4:
        div(eval(input("Divide this: ")),eval(input("by this: ")))
    elif choice == 5:
        loop = 0

print("Thank you for using calculator.py!")

# NOW THE PROGRAM REALLY FINISHES

# COMMAND ----------

# MAGIC %md
# MAGIC The initial program had 34 lines of code. The new one actually had 35 lines of code! It is a little longer, but if you look at it the right way, it is actually simpler.
# MAGIC
# MAGIC You defined all your functions at the top. This really isn't part of your main program - they are just lots of little programs that you will call upon later. You could even re-use these in another program if you needed them, and didn't want to tell the computer how to add and subtract again.
# MAGIC
# MAGIC If you look at the main part of the program (between the line `loop = 1` and `print("Thank you for...")`), it is only 15 lines of code. That means that if you wanted to write this program differently, you would only have to write 15 or so lines, as opposed to the 34 lines you would normally have to without functions.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4.8 Tricky Ways You Can Pass Parameters
# MAGIC Finally, as a bit of an interlude, I will explain what the line `add(eval(input("Add this: ")),eval(input("to this: ")))` means.
# MAGIC
# MAGIC I wanted to fit everything onto one line, with as few variables as possible. Remember what functions look like to the main program? Whatever value they return. If the numbers you passed to the add() function were 2 and 30, the main program would see this:
# MAGIC
# MAGIC `add(2,30)`
# MAGIC
# MAGIC The add program would then run, adding 2 and 30, then printing the result. The add program has no `return` operator - it doesn't return anything to the main program. It simply adds two numbers and prints them onscreen, and the main program doesn't see anything of it.
# MAGIC
# MAGIC Instead of `(eval(input("Add this: ")),eval(input("to this: ")))` as the parameters for the add program you could have variables. E.g.
# MAGIC
# MAGIC ```
# MAGIC num1 = 45
# MAGIC num2 = 7
# MAGIC add(num1,num2)
# MAGIC ```
# MAGIC
# MAGIC For the above, remember that the function you are passing the variables to cannot change the variables themselves - they are simply used as values. You could even put the values straight into the function:
# MAGIC
# MAGIC `add(45,7)`
# MAGIC
# MAGIC This is because the only thing the function sees are the values that are passed on as parameters. Those values are put into the variables that are mentioned when `add` is defined (the line `def add(a,b)`). The function then uses those parameters to do its job.
# MAGIC
# MAGIC In short:
# MAGIC * The only thing functions see of the main program is the parameters that are passed to it
# MAGIC * The only thing the main program sees of functions is the returned value that it passes back