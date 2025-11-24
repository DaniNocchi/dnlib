import os
import textwrap
wrapWidth = 30
tw = textwrap.TextWrapper(width=wrapWidth)
#region Public Functions (This contains the function description and will be used by the public)
def empty():
    """This prints an empty line."""
    _empty()
def bigLine():
    """This prints a big line, useful to separate stuff. Also the width is managed by the wrapWidth variable that can be changed with setWrapWidth()."""
    _bigLine()
def clear():
    """This clears the terminal history. Everything that was in the terminal until now is deleted.
    
    Notice: Only the text is deleted, but everything done above still remains the same, like functions or variables. This just deletes the print history."""
    _clear()
def setWrapWidth(newWidth : int):
    """Sets a new wrap width.
    
    Basically, this sets how long is the line from bigLine() and how long a text can be like in the menus description and titles."""
    _setWrapWidth(newWidth)
def codeErrorMessage(code : str):
    """Pre-Made Coded Error Messages

    Insert the code as string.

    Code List:

    - 001: Invalid Option
    
    """
    _codeErrorMessage(code)
def printWrap(text : str, centered = False):
    """Prints the text wrapped.
    
    The wrap width is controlled by the wrapWidth variable. You can modify it using the setWrapWidth() function.
    
    text (str): The text you want to print.
    centered (bool): This makes the text centered between the wrapWidth lenght. If the text exceeds the wrapWidth lenght, it will be divided in lines that are also centered, like this:
    
           This is a
         centered text"""
    _printWrap(text, centered)
#endregion
#region Private Functions (This contains the function actual code and will be called by the public functions)
def _empty(): 
    print()
def _bigLine(): 
    print("-"*wrapWidth)
def _clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')
def _setWrapWidth(newWidth : int):
    global wrapWidth
    wrapWidth = newWidth
    tw.width = wrapWidth
def _codeErrorMessage(code : str):
    #Notice: Add new codes into the public codeErrorMessage() function description.
    txt = f"⚠️ Error Code ({code}): "
    def add(msg): txt = txt + msg
    match code:
        case "001": add("Invalid Option. Try Again.")
        case "002": pass
    print(txt)
def _printWrap(text : str, centered = False):
    if centered: 
        wrappedText = tw.wrap(text)
        for i in wrappedText:
            print(i.center(wrapWidth))
        
    else: print(tw.fill(text))
#endregion
class _Option:
    def __init__(self, index, name, action):
        self.index = index
        self.name = name
        self.action = action
class newMenu:
    def __init__(self):
        """Creates a new menu.
        
        A menu contains a Title, a description (optional) and options that can be selected for actions."""
        self.title = ""
        self.description = ""
        self.options = []
    #region Public Functions (This contains the function description and will be used by the public)
    def add_title(self, titleText:str):
        """Adds a title to the menu.
        
        - titleText (str): The string that will become the title.
        """
        self._add_title(titleText)
    def add_description(self, descText : str):
        """Adds a description to the menu.
        
        - descText (str): The string that will become the description.
        
        Notice: If no description is added, the description part will be ignored when the menu is shown."""
        self._add_description(descText)
    def add_option(self, optionIndex : int, optionName : str, optionAction):
        """Adds an option that can be selected.
        
        - optionIndex (int): The index for the option, like the 1 in '1 - Start Game'.
        - optionName (str): The name for the option, like the 'Start Game' in the example above.
        - optionAction (lambda): The action that will happen if the option is selected. It needs to be a lambda.
        
        Example:
        
        exampleMenu.add_option(1, "print hello world", lambda : print('Hello World'))"""
        self._add_option(optionIndex, optionName, optionAction)
    def show_menu(self, deleteHistory : bool = True, execute : bool = True):
        """When called, the menu will be printed.
        
        - deleteHistory (bool, True by default): If true, all stuff printed above will be deleted. Useful to make a clean terminal.
        - execute (bool, True by default): If true, at the end of the printed menu, it will ask which option to choose and use the select() function automatically."""
        self._showMenu(deleteHistory, execute)
    def select(self, index : int):
        """Selects an option from this menu.
        
        index (int): The index of the option."""
        self._select(index)
    #endregion
    #region Private Functions (This contains the function actual code and will be called by the public functions)
    def _add_title(self, titleText : str):
        self.title = titleText
    def _add_description(self, descText : str):
        self.description = descText
    def _add_option(self, optionIndex : int, optionName : str, optionAction):
        option = _Option(optionIndex, optionName, optionAction)
        self.options.append(option)
    def _showMenu(self, deleteHistory : bool = True, execute : bool = True):
        if deleteHistory:
            clear()
        bigLine()
        empty()
        printWrap(self.title, True)
        empty()
        bigLine()
        if self.description != "":
            printWrap(self.description)
            bigLine()
        for option in self.options:
            optionText = f"{option.index} - {option.name}"
            printWrap(optionText)
        empty()
        if execute:
            chosen = input("- ")
            self.select(chosen)
    def _select(self, index : int):
        for option in self.options:
            if str(option.index) == index:
                option.action()
                return
        codeErrorMessage("001")
        self.select(index)
    #endregion


