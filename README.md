# Concatenation and interpolation
Welcome to this short demonstration of concatenation and interpolation

To make things organised this task has been split in to 3 files;
- `concatenation.py` which demonstrates concatenation in python
- `interpolation.py` which demonstrates interpolation in python
- `refactor.py` takes the code from the past two files and adds the refactoring specifications

There are comments that walk you along the code to help you better understand what's going on!

## `title()`
So why am I using `title()` over `capitalize()`? Well, `title()` has support for capitalising each word in a sentence. This automatically makes it a lot more useful for full names since I don't have to use loops to split up the word!

## `concatenation.py`
Concatenation is when you add two strings together, this task will do that in a fairly simple manner

First we'll ask the user for their name
```python
name = input("Please input your first name: ")
```
Then we'll generate two messages that we want to display on either side of the user's name
```python
welcome_message_1 = "Hi there, "
welcome_message_2 = ". Welcome to python!"
```
Then we'll bring it all together by concatenating the above messages
```python
print(welcome_message_1 + name + welcome_message_2)
```
That is all there is to concatenation

## `interpolation.py`
Interpolation is similar, except we use commas instead, this produces a slightly different result since spaces are automatically added in between the strings
First we'll ask the user for their name
```python
full_name = input("Please input your full name: ") # Asking the user for their full name
```
Then we'll generate two messages that we want to display on either side of the user's name
```python
welcome_message_1 = "Hi there,"
welcome_message_2 = "welcome to python!"
```
Then we'll bring it all together by interpolating the above messages. Since this method automatically adds spaces, we don't have to account for that above
```python
print(welcome_message_1, full_name, welcome_message_2)
```

## `refactor.py`
Finally, we want to allow the user to input their full name and have the program automatically adjust to it. Therefore the only major change in this program over the previous two is this line:
```python
name_refactor = name.strip().title()
```
What this does is take any string that is entered, remove any additional whitespaces that may have been entered in and then capitalises each word. So `joe bloggs          ` will become `Joe Bloggs`, and it automatically adjusts up and down so if someone has more than one name it's no problem for the program.