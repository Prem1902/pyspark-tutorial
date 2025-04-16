# Databricks notebook source
# MAGIC %md
# MAGIC # 3. Loops, Loops, Loops, Loops...
# MAGIC ## 3.1 Introduction
# MAGIC (Our final lesson before we get into interacting with human input. Can't wait, can you?)
# MAGIC
# MAGIC Just imagine you needed a program to do something 20 times. What would you do? You could copy and paste the code 20 times, and have a virtually unreadable program, not to mention slow and pointless. Or, you could tell the computer to repeat a bit of code between point A and point B, until the time comes that you need it to stop. Such a thing is called a loop.
# MAGIC
# MAGIC ## 3.2 The 'While' loop
# MAGIC The following are examples of a type of loop, called the 'while' loop:
# MAGIC

# COMMAND ----------

a = 0
while a < 10:
    a = a + 1
    print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC How does this program work? Lets go through it in English:
# MAGIC ```
# MAGIC 'a' now equals 0
# MAGIC As long as 'a' is less than 10, do the following:
# MAGIC    Make 'a' one larger than what it already is.
# MAGIC    Print on-screen what 'a' is now worth.
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC What does this do? Let's go through what the computer would be 'thinking' when it is in the 'while' loop:

# COMMAND ----------

# MAGIC %md
# MAGIC ```
# MAGIC #JUST GLANCE OVER THIS QUICKLY
# MAGIC #(It looks fancy, but is really simple)
# MAGIC Is 'a' less than 10? YES (its 0)
# MAGIC Make 'a' one larger (now 1)
# MAGIC print on-screen what 'a' is (1)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 1)
# MAGIC Make 'a' one larger (now 2)
# MAGIC print on-screen what 'a' is (2)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 2)
# MAGIC Make 'a' one larger (now 3)
# MAGIC print on-screen what 'a' is (3)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 3)
# MAGIC Make 'a' one larger (now 4)
# MAGIC print on-screen what 'a' is (4)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 4)
# MAGIC Make 'a' one larger (now 5)
# MAGIC print on-screen what 'a' is (5)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 5)
# MAGIC Make 'a' one larger (now 6)
# MAGIC print on-screen what 'a' is (6)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 6)
# MAGIC Make 'a' one larger (now 7)
# MAGIC print on-screen what 'a' is (7)
# MAGIC
# MAGIC Is 'a' less than 10? YES (are you still here?)
# MAGIC Make 'a' one larger (now 8)
# MAGIC print on-screen what 'a' is (8)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 8)
# MAGIC Make 'a' one larger (now 9)
# MAGIC print on-screen what 'a' is (9)
# MAGIC
# MAGIC Is 'a' less than 10? YES (its 9)
# MAGIC Make 'a' one larger (now 10)
# MAGIC print on-screen what 'a' is (10)
# MAGIC
# MAGIC Is 'a' less than 10? NO (its 10, therefore isn't less than 10)
# MAGIC Don't do the loop
# MAGIC There's no code left to do, so the program ends
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC So in short, try to think of it that way when you write 'while' loops. This is how you write them, by the way (syntax):
# MAGIC ```
# MAGIC while {condition that the loop continues}:
# MAGIC     {what to do in the loop}
# MAGIC     {have it indented, usually four spaces}
# MAGIC the code here is not looped
# MAGIC because it isn't indented
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC Now try to understand this example and run to see if it is what you expected.

# COMMAND ----------

x = 10
while x != 0:
    print(x)
    x = x - 1
    print("wow, we've counted x down, and now it equals", x)
print("And now the loop has ended.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3.3 Boolean Expressions (Boolen... what?!?)
# MAGIC What do you type in the area marked `{conditions that the loop continues}`? The answer is a boolean expression.<br>
# MAGIC What? A forgotten concept for the non-math people here. Never mind, boolean expression just means a question that can be answered with a TRUE or FALSE response. For example, if you wanted to say your age is the same as the person next to you, you would type:
# MAGIC
# MAGIC `My age == the age of the person next to me`
# MAGIC
# MAGIC And the statement would be TRUE. If you were younger than the person opposite, you'd say:
# MAGIC `My age < the age of the person opposite me`
# MAGIC
# MAGIC And the statement would be TRUE. If, however, you were to say the following, and the person opposite of you was younger than you:
# MAGIC
# MAGIC `My age < the age of the person opposite me`
# MAGIC
# MAGIC The statement would be FALSE - the truth is that it is the other way around. This is how a loop thinks - if the expression is true, keep looping. If it is false, don't loop. With this in mind, let's have a look at the operators (symbols that represent an action) that are involved in boolean expressions:<br>
# MAGIC
# MAGIC | Expression | Function  |
# MAGIC |   :---:    |   :---:   |
# MAGIC |    `<`     | Less than |
# MAGIC | `<=` | Less than or equal to |
# MAGIC | `>` | Greater than |
# MAGIC | `>=` | Greater than or equal to |
# MAGIC | `!=` | Not equal to |
# MAGIC | `==` | Equal to |
# MAGIC
# MAGIC Don't get `=` and `==` mixed up - the `=` operator makes what is on the left equal to what is on the right. the `==` operator says whether the thing on the left is the same as what is on the right, and returns True or False.
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3.4 Conditional Statements
# MAGIC OK! We've (hopefully) covered 'while' loops. Now let's look at something a little different - conditionals.<br>
# MAGIC Conditionals are where a section of code is only run if certain conditions are met. This is similar to the 'while' loop you just wrote, which only runs when x doesn't equal 0. However, Conditionals are only run once. The most common conditional in any program language, is the 'if' statement. Here is how it works:<br>
# MAGIC ```
# MAGIC if {conditions to be met}:
# MAGIC     {do this}
# MAGIC     {and this}
# MAGIC     {and this}
# MAGIC {but this happens regardless}
# MAGIC {because it isn't indented}
# MAGIC ```
# MAGIC <br>
# MAGIC Now some examples in Python:

# COMMAND ----------

#EXAMPLE 1
y = 1
if y == 1:
    print("y still equals 1, I was just checking")

# COMMAND ----------

#EXAMPLE 2
print("We will show the even numbers up to 20")
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n)
    n = n + 1
print("there, done.")

# COMMAND ----------

# MAGIC %md
# MAGIC Example 2 there looks tricky. But all we have done is run an `if` statement every time the `while` loop runs. Remember that the `%` just means the remainder from a division - just checking that there is nothing left over if the number is divided by two - showing it is even. If it is even, it prints what `n` is.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3.5 `else` and `elif` - When it Ain't True
# MAGIC There are many ways you can use the `if` statement to deal with situations where your boolean expression ends up FALSE. They are `else` and `elif`.<br>
# MAGIC `else` simply tells the computer what to do if the conditions of `if` aren't met. For example, read the following:

# COMMAND ----------

a = 1
if a > 5:
    print("This shouldn't happen.")
else:
    print("This should happen.")

# COMMAND ----------

# MAGIC %md
# MAGIC `a` is not greater than five, therefore what is under `else` is done.
# MAGIC
# MAGIC `elif` is just a shortened way of saying `else if`. When the `if` statement fails to be true, `elif` will do what is under it IF the conditions are met. For example:

# COMMAND ----------

z = 4
if z > 70:
    print("Something is very wrong")
elif z < 7:
    print("This is normal")

# COMMAND ----------

# MAGIC %md
# MAGIC The `if` statement, along with `else` and `elif` follow this form:
# MAGIC ```Python
# MAGIC if {conditions}:
# MAGIC     {run this code}
# MAGIC elif {conditions}:
# MAGIC     {run this code}
# MAGIC elif {conditions}:
# MAGIC     {run this code}
# MAGIC else:
# MAGIC     {run this code}
# MAGIC #You can have as many or as little elif statements as you need
# MAGIC #anywhere from zero to the sky.
# MAGIC #You can have at most one else statement
# MAGIC #and only after all other ifs and elifs.
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ***One of the most important points to remember is that you MUST have a colon `:` at the end of every line with an `if`, `elif`, `else` or `while` in it.***

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3.6 Indentation
# MAGIC One other point is that the code to be executed if the conditions are met, MUST BE INDENTED. That means that if you want to loop the next five lines with a `while` loop, you must put a set number of spaces at the beginning of each of the next five lines. This is good programming practice in any language, but Python requires that you do it. Here is an example of both of the above points:

# COMMAND ----------

a = 10
while a > 0:
    print(a)
    if a > 5:
        print("Big number!")
    elif a % 2 != 0:
        print("This is an odd number")
        print("It isn't greater than five, either")
    else:
        print("this number isn't greater than 5")
        print("nor is it odd")
        print("feeling special?")
    a = a - 1
    print("we just made 'a' one less than what it was!")
    print("and unless a is not greater than 0, we'll do the loop again.")
print("well, it seems as if 'a' is now no bigger than 0!")
print("the loop is now over, and without furthur adue, so is this program!")

# COMMAND ----------

# MAGIC %md
# MAGIC Notice the three levels of indents there:
# MAGIC 1. Each line in the first level starts with no spaces. It is the main program, and will always execute.
# MAGIC 2. Each line in the second level starts with four spaces. When there is an `if` or loop on the first level, everything on the second level after that will be looped/'ifed', until a new line starts back on the first level again.
# MAGIC 3.	Each line in the third level starts with eight spaces. When there is an `if` or loop on the second level, everything on the third level after that will be looped/'ifed', until a new line starts back on the second level again.
# MAGIC 4.	This goes on infinitely, until the person writing the program has an internal brain explosion, and cannot understand anything he/she has written.

# COMMAND ----------

# MAGIC %md
# MAGIC There is another loop, called the 'for' loop, but we will cover that in a later lesson, after we have learnt about lists.
# MAGIC ## 3.7 Conclusion
# MAGIC And that is lesson 3! In lesson 4, we get into user interaction, and writing programs that actually serve a purpose. Can't wait!