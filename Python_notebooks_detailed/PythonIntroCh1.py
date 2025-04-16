# Databricks notebook source
# MAGIC %md
# MAGIC # 1. Very simple 'programs'
# MAGIC ## 1.1 Running Python from the command line
# MAGIC In order to test pieces of code we can run Python from the command line. In this Jupyter Notebook we are going to simulate this. You can type the commands in the fields and execute them.<br>
# MAGIC In the field type:<br>
# MAGIC ```python
# MAGIC print('Hello, World')
# MAGIC ```
# MAGIC Then press `<shift> + <return>` to execute the command.
# MAGIC
# MAGIC

# COMMAND ----------

1+1

# COMMAND ----------

# MAGIC %md
# MAGIC What happened?
# MAGIC
# MAGIC You just created a program, that prints the words 'Hello, World'. The Python environment that you are in immediately compiles whatever you have typed in. This is useful for testing things, e.g. define a few variables, and then test to see if a certain line will work. That will come in a later lesson, though.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1.2 Math in Python
# MAGIC Type<br>
# MAGIC ```python
# MAGIC 1 + 1
# MAGIC ```
# MAGIC and execute the code.

# COMMAND ----------

 + 1

# COMMAND ----------

# MAGIC %md
# MAGIC Now type
# MAGIC ```python
# MAGIC 20 + 80
# MAGIC ```
# MAGIC and execute the code.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC These are additions. We can of course use other mathematical operators.<br>
# MAGIC Try this subtraction:<br>
# MAGIC ```python
# MAGIC 6 - 5
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC and this multiplication:<br>
# MAGIC ```python
# MAGIC 2 * 5
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC Try:
# MAGIC ```python
# MAGIC 5 ** 2
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC `**` is the exponential operator, so we executed 5 squared.

# COMMAND ----------

# MAGIC %md
# MAGIC Type:
# MAGIC ```python
# MAGIC print('1 + 2 is an addition')
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC You see that the `print` statement writes something on the screen.
# MAGIC
# MAGIC Try this:
# MAGIC ```python
# MAGIC print('one kilobyte is 2^10 bytes, or', 2 ** 10, 'bytes')
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC This demonstrates that you can print text and calculations in a sentence. The commas separating each section are a way of separating strings (text) from calculations or variable.

# COMMAND ----------

# MAGIC %md
# MAGIC Now try this:
# MAGIC ```python
# MAGIC 23 / 3
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC And this:<br>
# MAGIC ```python
# MAGIC 23 % 3
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC `%` returns the remainder of the division.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1.3 Order of Operations

# COMMAND ----------

# MAGIC %md
# MAGIC Remember that thing called order of operation that they taught in maths? Well, it applies in Python, too. Here it is, if you need reminding:<br>
# MAGIC 1. Parenthesis `()`
# MAGIC 2. Exponents `**`
# MAGIC 3. Multiplication `*`, division `/` and remainder `%`
# MAGIC 4. Addition `+` and subtraction `-`

# COMMAND ----------

# MAGIC %md
# MAGIC Here are some examples that you might want to try, if you're rusty on this:<br>
# MAGIC ```python
# MAGIC 1 + 2 * 3
# MAGIC (1 + 2) * 3
# MAGIC ```

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ## 1.4 Comments, Please
# MAGIC The final thing you'll need to know to move on to multi-line programs is the comment. Type the following (and yes, the output is shown):
# MAGIC ```python
# MAGIC # I am a comment. Fear my wrath!
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC A comment is a piece of code that is not run. In Python, you make something a comment by putting a hash in front of it. A hash comments everything after it in the line, and nothing before it. So you could type this:
# MAGIC ```python
# MAGIC print("food is very nice") #eat me
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC This results in a normal output, without the smutty comment, thank you very much.
# MAGIC
# MAGIC Now try this:
# MAGIC ```python
# MAGIC # print("food is very nice")
# MAGIC ```

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC Nothing happens, because the code was after a comment.

# COMMAND ----------

# MAGIC %md
# MAGIC Comments are important for adding necessary information for another programmer to read, but not the computer. For example, an explanation of a section of code, saying what it does, or what is wrong with it. You can also comment bits of code by putting a `#` in front of it - if you don't want it to compile, but can't delete it because you might need it later.

# COMMAND ----------

# MAGIC %md
# MAGIC # Assignment 1
# MAGIC
# MAGIC Type in the cell below an expression to find out how many seconds are there in a 365-day year.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Assignment 2
# MAGIC
# MAGIC The Earth can be approximated as a sphere with a radius of 6370 km. Use the cell below to find out the volume of such a shape in cubic meters.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Assignment 3
# MAGIC
# MAGIC Get the answer of the following expression, using the cell below:
# MAGIC
# MAGIC $$\frac{1}{2}+\frac{\frac{1}{3}}{\frac{1}{4}+\frac{1}{5}}$$

# COMMAND ----------

