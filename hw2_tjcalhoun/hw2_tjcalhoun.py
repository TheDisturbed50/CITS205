# Thomas Calhoun 
# homework #2
# tjcalhoun@alaska.edu 21 Jan 2016
# Python 3.5.1

# define variables
poem = '''sweet spring is your
time is my time is our
time for springtime is lovetime
and viva sweet love'''

print("> Here is Jeanette's Poem:\n"+poem,"\n")# print the poem

print("> This poem contains",len(poem),"characters.\n")# print how many characters the poem contains

print("> First line of Poem challenge:\n",poem[0:20],"\n")# using slice (chapter 2, page 33 in paper book), print first line of poem

print("> Slice Challenge:\n",poem[44:59]+"!","\n") # using slice, print the line "time for spring" and add a bang/exclamation point(!)

print("> Split Challenge:\n",poem.split(),"\n") # print the result of using the string method split()

print("> Replace Challenge:\n",poem.replace("is","was"),"\n") # print the poem and replace the word 'is' with 'was'

print("> Capitalize Every Word Challenge:\n",poem.title(),"\n") # print the poem and capitalize each word of the poem

# for each of the previous sections, print a line that explains the output that follows

input("**Press Enter to Close Program**") # I figured this out to keep the prompt open,
# so you could review the output before window is terminated (great if executed by python itself,
# you probably notice the benefit if ran from command prompt).


