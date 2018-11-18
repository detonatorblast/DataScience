#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions
# 
# Regular expressions are text-matching patterns described with a formal syntax. You'll often hear regular expressions referred to as 'regex' or 'regexp' in conversation. Regular expressions can include a variety of rules, from finding repetition, to text-matching, and much more.

# In[17]:


import re

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')


# This **Match** object returned by the search() method is more than just a Boolean or None, it contains information about the match, including the original input string, the regular expression that was used, and the location of the match. Let's see the methods we can use on the match object:

# In[18]:


matchstr = re.search('Mukul', 'muktesh Mukul')


# In[19]:


matchstr.start()


# In[15]:


matchstr.end()


# # Split with regular expressions
# Let's see how we can split with the re syntax. This should look similar to how you used the split() method with strings.

# In[20]:


split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

re.split(split_term, phrase)


# # Finding all instances of a pattern
# You can use re.findall() to find all the instances of a pattern in a string. For example:

# In[26]:


# Returns a list of all matches
re.findall('match','test phrase match is in middle. There is one more match')


# # re Pattern Syntax
# 
# Regular expressions support a huge variety of patterns beyond just simply finding where a single string occurred. 
# 
# We can use metacharacters along with re to find specific types of patterns.
# 
# Since we will be testing multiple re syntax forms, let's create a function that will print out results given a list of various regular expressions and a phrase to parse

# In[27]:


def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')


# # Repetition Syntax
# There are five ways to express repetition in a pattern:
# 
# 1. A pattern followed by the meta-character * is repeated zero or more times.
# 2. Replace the * with + and the pattern must appear at least once.
# 3. Using ? means the pattern appears zero or one time.
# 4. For a specific number of occurrences, use {m} after the pattern, where m is replaced with the number of times the pattern should repeat.
# 5. Use {m,n} where m** is the minimum number of repetitions and **n is the maximum. Leaving out n** {m,} means the value appears at least **m times, with no maximum.
# 

# In[39]:


# Now we will see an example of each of these using our multi_re_find function:
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)


# # Character Sets
# Character sets are used when you wish to match any one of a group of characters at a point in the input. Brackets are used to construct character set inputs. For example: the input [ab] searches for occurrences of either a** or **b. Let's see some examples:

# In[40]:


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)


# # Exclusion
# We can use ^ to exclude terms by incorporating it into the bracket syntax notation. For example: [^...] will match any single character not in the brackets. Let's see some examples:

# In[41]:


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

re.findall('[^!.? ]+',test_phrase)


# In[42]:


print(re.search('[^!.? ]+',test_phrase))


# # Character Ranges
# As character sets grow larger, typing every character that should (or should not) match could become very tedious. A more compact format using character ranges lets you define a character set to include all of the contiguous characters between a start and stop point. The format used is [start-end].
# 
# Common use cases are to search for a specific range of letters in the alphabet. For instance, [a-f] would return matches with any occurrence of letters between a and f.
# 
# Let's walk through some examples:

# In[43]:


test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)


# # Escape Codes
# You can use special escape codes to find specific types of patterns in your data, such as digits, non-digits, whitespace, and more. For example:
# 
# | Code  | Meaning |
# | ----- | ------  |
# | \d	| a digit |
# | \D	| a non-digit |
# | \s	| whitespace (tab, space, newline, etc.) |
# | \S	| non-whitespace |
# | \w	| alphanumeric |
# | \W	| non-alphanumeric |
# Escapes are indicated by prefixing the character with a backslash r, eliminates this problem and maintains readability.
# 
# Personally, I think this use of r to escape a backslash is probably one of the things that block someone who is not familiar with regex in Python from being able to read regex code at first. Hopefully after seeing these examples this syntax will become clear.

# In[44]:


test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)


# In[ ]:





# In[ ]:




