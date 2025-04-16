# Databricks notebook source
# MAGIC %md
# MAGIC # 8. Modules
# MAGIC ## 8.1 Introduction
# MAGIC Last lesson we covered the killer topic of Classes. As you can remember, classes are neat combinations of variables and functions in a nice, neat package. Programming lingo calls this feature encapsulation, but regardless of what it is called, it's a really cool feature for keeping things together so the code can be used in many instances in lots of places. Of course, you've got to ask, "how do I get my classes to many places, in many programs?". The answer is to put them into a module, to be imported into other programs.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8.2 Module? What's a Module?
# MAGIC A module is a Python file that (generally) has only definitions of variables, functions, and classes. For example, a module might look like this, which we store in a file `moduletest.py`:
# MAGIC ```Python
# MAGIC ### EXAMPLE PYTHON MODULE
# MAGIC # Define some variables:
# MAGIC numberone = 1
# MAGIC ageofqueen = 78
# MAGIC
# MAGIC # define some functions
# MAGIC def printhello():
# MAGIC     print("hello")
# MAGIC     
# MAGIC def timesfour(input):
# MAGIC     print(eval(input) * 4)
# MAGIC     
# MAGIC # define a class
# MAGIC class Piano:
# MAGIC     def __init__(self):
# MAGIC         self.type = input("What type of piano? ")
# MAGIC         self.height = input("What height (in feet)? ")
# MAGIC         self.price = input("How much did it cost? ")
# MAGIC         self.age = input("How old is it (in years)? ")
# MAGIC 	
# MAGIC     def printdetails(self):
# MAGIC         print("This piano is a/an " + self.height + " foot", end=" ")
# MAGIC         print(self.type, "piano, " + self.age, "years old and costing\
# MAGIC          " + self.price + " dollars.")
# MAGIC ```
# MAGIC
# MAGIC As you see, a module looks pretty much like your normal Python program.
# MAGIC
# MAGIC So what do we do with a module? We `import` bits of it (or all of it) into other programs.
# MAGIC
# MAGIC To import all the variables, functions and classes from `moduletest.py` into another program you are writing, we use the `import` operator. For example, to import `moduletest.py` into your main program (`mainprogram.py`), you would have this:
# MAGIC
# MAGIC ```Python
# MAGIC ### mainprogam.py
# MAGIC ### IMPORTS ANOTHER MODULE
# MAGIC import moduletest
# MAGIC ```
# MAGIC
# MAGIC This assumes that the module is in the same directory as `mainprogram.py`, or is a default module that comes with Python. You leave out the `.py` at the end of the file name - it is ignored. You normally put all `import` statements at the beginning of the Python file, but technically they can be anywhere. In order to use the items in the module in your main program, you use the following:
# MAGIC
# MAGIC ```Python
# MAGIC ### USING AN IMPORTED MODULE
# MAGIC # Use the form modulename.itemname
# MAGIC # Examples:
# MAGIC print(moduletest.ageofqueen)
# MAGIC cfcpiano = moduletest.Piano()
# MAGIC cfcpiano.printdetails()
# MAGIC ```
# MAGIC
# MAGIC As you see, the modules that you import act very much like the classes we looked at last lesson - anything inside them must be preceded with `modulename.` for it to work.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8.3 More module thingummyjigs (in lack of a better title)
# MAGIC Wish you could get rid of the `modulename.` part that you have to put before every item you use from a module? No? Never? Well, I'll teach it to you anyway.
# MAGIC
# MAGIC One way to avoid this hassle is to import only the wanted objects from the module. To do this, you use the `from` operator. You use it in the form of `from modulename import itemname`. Here is an example:
# MAGIC
# MAGIC ```Python
# MAGIC ### IMPORT ITEMS DIRECTLY INTO YOUR PROGRAM
# MAGIC
# MAGIC # import them
# MAGIC from moduletest import ageofqueen
# MAGIC from moduletest import printhello
# MAGIC
# MAGIC # now try using them
# MAGIC print(ageofqueen)
# MAGIC printhello()
# MAGIC ```
# MAGIC
# MAGIC What is the point of this? Well, maybe you could use it to make your code a little more readable. If we get into heaps of modules inside modules, it could also remove that extra layer of crypticness.
# MAGIC
# MAGIC If you wanted to, you could import everything from a module in this way by using `from modulename import *`. Of course, this can be troublesome if there are objects in your program with the same name as some items in the module. With large modules, this can easily happen, and can cause many a headache. A better way to do this would be to import a module in the normal way (without the `from` operator) and then assign items to a local name:
# MAGIC
# MAGIC ```Python
# MAGIC ### ASSIGNING ITEMS TO A LOCAL NAME
# MAGIC
# MAGIC # Assigning to a local name
# MAGIC timesfour = moduletest.timesfour
# MAGIC
# MAGIC # Using the local name
# MAGIC print(timesfour(565))
# MAGIC ```
# MAGIC
# MAGIC This way, you can remove some crypticness, AND have all of the items from a certain module.
# MAGIC
# MAGIC A final handy way to import modules is with an alias. Maybe you want to change a name because you've already used the same name for something else in your program, another module you imported uses the same name, or maybe you want to abbreviate a longer name that you use a lot. We can then use the `as` operator. That looks like this:
# MAGIC
# MAGIC ```Python
# MAGIC ### IMPORT A MODULE WITH AN ALIAS
# MAGIC # import module
# MAGIC import moduletest as mt
# MAGIC
# MAGIC # use module
# MAGIC print(mt.age)
# MAGIC cfcpiano = mt.Piano()
# MAGIC cfcpiano.printdetails()
# MAGIC ```
# MAGIC
# MAGIC ## 8.4 Conclusion
# MAGIC That's it! A very simple lesson, but now you can organise your programs very neatly. In fact, now it is incredibly easy to make programs that can grow in complexity without ending up with one cryptic file that is full of bugs.
# MAGIC Modules are great for importing code. Next lesson, we learn about file input and output, and the saving of information inside classes, to be retrieved later. Will be great!