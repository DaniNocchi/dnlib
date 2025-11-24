# dnlib - A lib made by DaniNocchi
## Description
I hate making new UI stuff every time i want to make a fancy menu with python, so I decided to make this lib to help with that.
Also,  I´ve added some other functions that are very useful.

## Documentation
### empty()
This prints an empty line.

Example:
```py
print("this is a text")
empty()
print("this is also a text")
```
Returns:
```
this is a text

this is also a text
```
### bigLine()
This prints a big line. It's size depends on the `wrapWidth` variable size. This variable can be modified with the `setWrapWidth()` function.

Example:
```py
bigLine()
print("Thats a big line, I see")
```
Returns:
```
------------------------------
Thats a big line, I see
```
### clear()
This clears any previous text in the terminal.

Example:
```py
print("This text might disappear")
clear()
print("new text")
```
Returns:
```
new text
```
### setWrapWidth(newWidth)
There is a variable in this lib called `wrapWidth`. It defines the size of the `bigLine()` line and wrapped texts from `printWrap()` function.
This function sets its size. By default, `wrapWidth` is 30 characters.

Arguments:
newWidth (int): The width of the `wrapWidth` variable.

### errorMessage(text, returnTo)
This prints a custom error message.

Arguments:
text (str): The error text.
returnTo (lambda): The function that will be called when enter is pressed.

Example:
```py
errorMessage("Please, insert a valid answer.", lambda : main())
```
Returns:
```
⚠️ An error has occurred: Please, insert a valid answer.
Press enter to continue...
```
(after pressing enter, it will call `main()`)

### printWrap(text, centered = False)
This functions as the normal `print()` function, but it is wrapped using the `wrapWidth` size. 
It uses another lib called `text wrap`. It is required to be installed to use this lib.

Arguments:
text (str): The printed text
centered (bool, False by default): If true, this centers the wrapped text.

Example: 
(wrapWidth = 30 on this example)
```py
printWrap("This is a normal big text, I have to write a lot to make this work lmao")
empty()
printWrap("This other text is also wrapped, but this is centered too", True)
```
Returns:
```
This is a normal big text, I
have to write a lot to make
this work lmao

   This other text is also
wrapped, but this is centered
             too
```


## Menu System
### I´ve also included an entire menu system.

### How to use it:
To create a new menu, do this:
```py
import dnlib

exampleMenu = dnlib.newMenu()
```
A menu contains a title, a description (optional) and options that can be selected.

Here is an example of a main menu for a game:
```py
import dnlib 

mainMenu = dnlib.newMenu()
mainMenu.add_title("Main Menu")
#I will not add description
mainMenu.add_option(1, "Start Game", lambda : startGame())
mainMenu.add_option(2, "Quit Game", lambda : exitGame())
mainMenu.show_menu()
```
This returns:
```
------------------------------

          Main Menu

------------------------------
1 - Start Game
2 - Quit Game

-
```

## Documentation (for the menu class)
### add_title(titleText)
Adds an title for the menu. This is required.

Arguments:
titleText (str): The title text...

### add_description(descText)
Adds an description. This is optional.

Arguments:
descText (str): The text that will become the description.

### add_option(optionIndex, optionName, optionAction)
This adds a new option to the menu.

Arguments:
optionIndex (int): The index for the option. Basically this is the number assigned to the option. When this number is called, the option it is assigned will be called.
optionName (str): The name the option will get. 
optionAction (lambda): The action that will happen when this option is called. This is formatted like this: `lambda : exampleFunction()`.

### show_menu(deleteHistory = True, execute = True)
This will finally print the menu.

Arguments:
deleteHistory (bool, True by default): If true, the menu will call `clear()` before printing the menu.
execute (bool, True by default): If true, it will automatically ask which option the user will choose and automatically execute `select()`.

### select(index)
This selects the option by it's index.

Arguments:
index (int): The option's index that will be called. This is automatically called if the `show_menu()` function has `execute = True`.



