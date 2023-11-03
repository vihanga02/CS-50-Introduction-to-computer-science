#first install emoji with pip
import emoji
#prompt user for an input
a = input("Input:")
#print the emojize version
print(emoji.emojize(f'Output: {a}' ,language='alias'))