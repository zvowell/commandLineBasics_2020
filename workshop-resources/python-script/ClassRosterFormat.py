#Script to reformat a class roster into output format
#9/26/2019

import pandas as pd
import sys

# declare the function name as 'parser', and establish an argument for parser to take, which is named 'filePath'
def parser(filePath):
    # define a variable called 'df' as the value of the contents defined by filePath, and use pandas to read the contents as a csv
    df = pd.read_csv(filePath)

    # define a variable called 'dfdrop' as the value of 'df', but without (.drop) rows 1-7 of the 'df' csv
    dfdrop = df.drop([0, 1, 2, 3, 4, 5, 6])

    # define a variable called 'dffiltered' as an index (.iloc) of 'dfdrop', which takes from 'dfdrop' csv the a slice of rows 2 - the end of the columns (1:) and a slice of columns 2-4 (1:3) 
    dffiltered = dfdrop.iloc[1:, 1:3]
    # define a variable called 'names' as the value of the column 'Unnamed: 2' from the index stored in the variable 'dffiltered'. Apparently pandas assigns 'Unnamed' columns that don't have headings. In this case, column 'Unnamed: 2' is the "Student Username" column in the original csv, because it is the 3rd column and therefore at position 2 in the 'dffiltered' index.
    names = dffiltered['Unnamed: 2']
    
    # define a variable called 'splitname1' as the value of the column 'Class List' (not sure where this name comes from) from index 'dffiltered', and use the presence of a comma (", ") to split the string values (str.split is its own function, not 2 separate functions) into 2 columns (exand=True) and limit the amount of splits to 1 (n=1)
    splitname1 = dffiltered['Class List'].str.split(", ", n=1,expand=True)
    # label the 2 resulting columns as 'a' (column 1) and 'b' (column 2)
    splitname1.columns = ['a', 'b']
    
    # define a variable 'h' that splits column 'b' from the variable 'splitname1' by the presence of a whitespace character (" "), and split them into 2 columns (expand=True)
    h = splitname1['b'].str.split(" ", expand=True)
    # label the 2 resulting columns as 'c' and 'd'
    h.columns = ['c','d']
    # drop the column 'd' from the index stored in the variable 'h'
    h = h.drop(['d'], axis=1)
    # return the first 5 rows of the index stored in the variable 'h'
    h.head()

    # drop the column 'b' (which was the string value after the comma in the original 'Class List' column values) from the index stored in the variable 'splitname1'
    splitname1 = splitname1.drop(['b'], axis=1)
    # define a variable called 'final' and use pandas to concatenate the indexes stored in 'splitname1' and 'h' (which should be last name (before the comma) in 'Class List', and the first name, stripped of any middle initial, in 'Class List')
    final = pd.concat([splitname1, h], axis=1)
    # use pandas to concatenate to what's aready in 'final' the index that is found in 'names'
    final = pd.concat([final, names], axis=1)
    # label the 3 columns in the index stored in 'final' as 'First', 'Last', and 'User'
    final.columns = ['First', 'Last', 'User']
    # return 'final'?
    final

    # define a variable called 'email' that takes the column 'User' in 'final' and appends the string "@calpoly.edu" to each value in that column
    email = final['User'] + "@calpoly.edu"
    # use pandas to concatenate the index stored in 'email' to the existing index stored in 'final'
    final = pd.concat([final, email], axis=1)
    # label the columns in the new version of 'final' as 'First', 'Last', 'User', and 'Email'
    final.columns = ['First', 'Last', 'User', 'Email']

    # define a variable called 'username' and take the column 'User' in 'final' and append the string "_CalPoly" to each value in that column
    username = final['User'] + "_CalPoly"
    # use pandas to concatenate the index 'username' to the the already existing index stored in 'final'
    final = pd.concat([final, username], axis=1)

    # label the columns in the new version of 'final' as 'Last Name', 'First Name', 'User', 'Email', and 'Username'
    final.columns = ['Last Name', 'First Name', 'User', 'Email', 'Username']
    # take the column 'Role' (not sure where this comes from) and assign the value "Publisher" to each row in that column
    final['Role'] = "Publisher"
    # take the column 'User Type' (not sure where this comes from) and assign the value "Creator" to each row in that column
    final['User Type'] = "Creator"
    # drop the column 'User' from the index 'final'
    final = final.drop('User', axis=1)
    # bring the index from the original dataframe ('df'?) and add it as the first column
    final = final.reset_index()
    # drop the column 'index' (not sure where this comes from, or why this is necessary?) from the index 'final'
    final = final.drop(['index'], axis=1)

    # convert the index 'final' to the csv format, and output this new csv to a file that will be named according the value defined in the argument 'filePath' argument of function 'parser', and append the string "_output.csv" to the file name (not sure where the [:-4] comes into play)
    final.to_csv(filePath[:-4] + "_output.csv") 

# define a function called 'main' that takes no arguments
def main():
    # run the function 'parser' and pass to it through the 'filePath' argument the value of the first argument in the bash command that executes the script ('(sys.argv[1])'). This value will also be used in the occurrences of 'filePath' in the parser function defined above
    parser(sys.argv[1])

# return the output of function 'main'
main()
