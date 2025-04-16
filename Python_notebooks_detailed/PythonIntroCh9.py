# Databricks notebook source
# MAGIC %md
# MAGIC # 9. File I/O
# MAGIC ## 9.1 Introduction
# MAGIC Last lesson we learned how to load external code into our program. Without any introduction (like what I usually have), let's delve into file input and output with normal text files, and later the saving and restoring of instances of classes. (Wow, our lingo power has improved greatly!)
# MAGIC ## 9.2 Opening a file
# MAGIC To open a text file you use, well, the `open()` function. Seems sensible. You pass certain parameters to `open()` to tell it in which way the file should be opened - `r` for read only, `w` for writing only (if there is an old file, it will be written over), `a` for appending (adding things on to the end of the file) and `r+` for both reading and writing. But less talk, let's open a file for reading (you can do this in Spyder later in the course). Open a normal text file. We will then print out what we read inside the file:
# MAGIC ```Python
# MAGIC filename = 'C:\\temp\\readme.txt' # path to file.\ is an escape character, so you need 2 or use / instead.
# MAGIC fl = open(filename, 'r') # Open the file
# MAGIC for line in fl:
# MAGIC     print(line)
# MAGIC fl.close() #close the file 
# MAGIC ```
# MAGIC
# MAGIC A better way to write this is:
# MAGIC ```Python
# MAGIC filename = 'C:\\temp\\readme.txt'
# MAGIC with open(filename, 'r') as fl:
# MAGIC     for line in fl:
# MAGIC         print(line)
# MAGIC ```
# MAGIC
# MAGIC With the second method you don't have to add `fl.close`, it is automagically closed.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 9.3 Seek and You Shall Find
# MAGIC If you want to print the whole file, instead of looping over the lines you can use this:
# MAGIC ```Python
# MAGIC
# MAGIC filename = 'C:\\temp\\readme.txt'
# MAGIC fl = open(filename, 'r')
# MAGIC print(fl.read())
# MAGIC ```
# MAGIC
# MAGIC Did you try to run `print(fl.read())` a second time? Did it fail? It likely did, and reason is because the 'cursor' has changed it's place. Cursor? What cursor? Well, a cursor that you really cannot see, but still a cursor. This invisible cursor tells the read function (and many other I/O functions) where to start from. To set where the cursor is, you use the `seek()` function. It is used in the form `seek(offset, whence)`.
# MAGIC
# MAGIC `whence` is optional, and determines where to seek from. If `whence` is 0, the bytes/letters are counted from the beginning. If it is 1, the bytes are counted from the current cursor position. If it is 2, then the bytes are counted from the end of the file. If nothing is put there, 0 is assumed.
# MAGIC
# MAGIC `offset` decribes how far from `whence` that the cursor moves. for example:
# MAGIC * `fl.seek(45,0)` would move the cursor to 45 bytes/letters after the beginning of the file.
# MAGIC * `fl.seek(10,1)` would move the cursor to 10 bytes/letters after the current cursor position.
# MAGIC * `fl.seek(-77,2)` would move the cursor to 77 bytes/letters before the end of the file (notice the - before the 77)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC We can use `fl.seek()` to go to any spot in the file and then try typing `print(fl.read())`. It will print from the spot you seeked to. But realise that `fl.read()` moves the cursor to the end of the file - you will have to seek again.
# MAGIC
# MAGIC ## 9.4 Other I/O Functions
# MAGIC There are many other functions that help you with dealing with files. They have many uses that empower you to do more, and make the things you can do easier. Let's have a look at `tell()`, `readline()`, `readlines()`, `write()` and `close()`.
# MAGIC
# MAGIC `tell()` returns where the cursor is in the file. It has no parameters, just type it in (like what the example below will show). This is infinitely useful, for knowing what you are referring to, where it is, and simple control of the cursor. To use it, type `fileobjectname.tell()` - where fileobjectname is the name of the file object you created when you opened the file (in `openfile = open('pathtofile', 'r')` the file object name is `openfile`).
# MAGIC
# MAGIC `readline()` reads from where the cursor is till the end of the line. Remember that the end of the line isn't the edge of your screen - the line ends when you press enter to create a new line. This is useful for things like reading a log of events, or going through something progressively to process it. There are no parameters you have to pass to `readline()`, though you can optionally tell it the maximum number of bytes/letters to read by putting a number in the brackets. Use it with `fileobjectname.readline()`.<br>
# MAGIC
# MAGIC `readlines()` is much like `readline()`, however `readlines()` reads all the lines from the cursor onwards, and returns a list, with each list element holding a line of code. Use it with `fileobjectname.readlines()`. For example, if you had the text file:
# MAGIC ```
# MAGIC Line 1
# MAGIC
# MAGIC Line 3
# MAGIC Line 4
# MAGIC
# MAGIC Line 6
# MAGIC ```
# MAGIC then the returned list from `readlines()` would be:<br>
# MAGIC
# MAGIC | Index | Value |
# MAGIC | :--: | :--: |
# MAGIC | 0 | 'Line 1' |
# MAGIC | 1 | " |
# MAGIC | 2 | 'Line 3' |
# MAGIC | 3 | 'Line 4' |
# MAGIC | 4 | " |
# MAGIC | 5 | 'Line 6' |
# MAGIC
# MAGIC The `write()` function, writes to the file. How did you guess??? It writes from where the cursor is, and overwrites text in front of it - like in MS Word, where you press 'insert' and it writes over the top of old text. To utilise this most purposeful function, put a string between the brackets to write e.g. `fileobjectname.write('this is a string')`.
# MAGIC
# MAGIC `close`, you may figure, closes the file so that you can no longer read or write to it until you reopen in again. Simple enough. To use, you would write `fileobjectname.close()`. Simple!
# MAGIC
# MAGIC Later in the course you can try this in the Python command line. Open up a test file (or create a new one...) and play around with these functions. You can do some simple (and very inconvenient) text editing.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 9.5 Mmm, Pickles
# MAGIC Pickles, in Python, are to be eaten. Their flavour is just too good to let programmers leave them in the fridge.
# MAGIC
# MAGIC Ok, just joking there. Pickles, in Python, are objects saved to a file. An object in this case could be a variable, instance of a class, or a list, dictionary, or tuple. Other things can also be pickled, but with limits. The object can then be restored, or unpickled, later on. In other words, you are 'saving' your objects.
# MAGIC
# MAGIC So how do we pickle? With the `dump()` function, which is inside the pickle module - so at the beginning of your program you will have to write `import pickle`. Simple enough? Then open an empty file, and use `pickle.dump()` to drop the object into that file. Let's try that:
# MAGIC
# MAGIC ```Python
# MAGIC ### pickletest.py
# MAGIC ### PICKLE AN OBJECT
# MAGIC
# MAGIC # import the pickle module
# MAGIC import pickle
# MAGIC
# MAGIC # lets create something to be pickled
# MAGIC # How about a list?
# MAGIC picklelist = ['one',2,'three','four',5,'can you count?']
# MAGIC
# MAGIC # now create a file
# MAGIC # replace filename with the file you want to create
# MAGIC # wb means that it's written in a binary file
# MAGIC file = open('filename', 'wb')
# MAGIC
# MAGIC # now let's pickle picklelist
# MAGIC pickle.dump(picklelist,file)
# MAGIC
# MAGIC # close the file, and your pickling is complete
# MAGIC file.close()
# MAGIC ```
# MAGIC
# MAGIC The code to do this is laid out like `pickle.dump(object_to_pickle, file_object)` where:
# MAGIC * `object_to_pickle` is the object you want to pickle (i.e. save it to file)
# MAGIC * `file_object` is the file object you want to write to (in this case, the file object is `file`)

# COMMAND ----------

# MAGIC %md
# MAGIC Now to re-open, or unpickle, your file we would use `pickle.load()`:<br>
# MAGIC ```Python
# MAGIC ### unpickletest.py
# MAGIC ### unpickle file
# MAGIC
# MAGIC # import the pickle module
# MAGIC import pickle
# MAGIC
# MAGIC # now open a file for reading
# MAGIC # replace filename with the path to the file you created in pickletest.py
# MAGIC unpicklefile = open('filename', 'rb')
# MAGIC
# MAGIC # now load the list that we pickled into a new object
# MAGIC unpickledlist = pickle.load(unpicklefile)
# MAGIC
# MAGIC # close the file, just for safety
# MAGIC unpicklefile.close()
# MAGIC
# MAGIC # Try out using the list
# MAGIC for item in unpickledlist:
# MAGIC     print(item)
# MAGIC ```
# MAGIC Nifty, eh?<br>
# MAGIC
# MAGIC Of course, the limitation above is that we can only put in one object to a file. We could get around this by putting lots of picklable objects in a list or dictionary, and then pickling that list or dictionary. This is the quickest and easiest way, but you can do some pretty advanced stuff if you have advanced knowledge of pickle.<br>
# MAGIC     
# MAGIC Which we won't cover.