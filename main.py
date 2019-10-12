import sys
import csv
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import cross_val_score


# Read in the *.csv files from cmd ln.
first_input_csv = sys.argv[2]
second_output_csv = sys.argv[3]

# Open, read *.csv files
inputcsv = open(first_input_csv, 'r')
inputreader = csv.reader(inputcsv)

# Creating the path to output file.
outfilepath = "./" + str(second_output_csv)
# Opening the file at the path.
outfile = open(outfilepath, 'w')
# Create writer to output *.csv.
writer = csv.writer(outfile, delimiter=',')

# New feature columns.
new_col_one = ["feat 1"]
new_col_two = ["feat 2"]
new_col_three = ["feat 3"]
new_col_four = ["feat 4"]
new_col_five = ["feat 5"]


# Feature 1 - Which player has a piece in the bottom left corner of the board?
# Implemented when writing to output

# Feature 2 - Which player has more pieces in the center columns?
def countCenterCols ( row ) :
    player_one_count = 0
    player_two_count = 0

    for k in range (12, 30):
        if row[k] == "1":
            player_one_count += 1
        elif row[k] == "2":
            player_two_count += 1
    if player_one_count > player_two_count:
        return 1
    elif player_two_count > player_one_count:
        return 2
    elif player_one_count == player_two_count:
        return 0



# Feature 3 - Which player has the most top pieces in the columns?
def countLastColPiece (row) :
    player_one_count = 0
    player_two_count = 0
    index_count = -1
    found_last = False
    # Iterate across rows
    for i in range (0, 7):
        # And up each column
        for j in range (0, 6):
            index_count += 1
            if (row[index_count] == "0") & (found_last == False):
                if row [index_count - 1] == "1":
                    player_one_count += 1
                elif row [index_count - 1] == "2":
                    player_two_count += 1
                found_last = True
        found_last = False
    if player_one_count > player_two_count:
        return 1
    elif player_two_count > player_one_count:
        return 2
    elif player_one_count == player_two_count:
        return 0



#Feature 4 - Which player the most chips in a horizontal connection?
def countHorizontalConnect (row):
    player_one_count = 0
    player_two_count = 0

    # Row 1
    for i in range (0, 31, 6):
        last_match = 0
        if row[i] == row[i+6]:
            if row[i] == "1":
                player_one_count += 1
            elif row[i] == "2":
                player_two_count += 1
            last_match = row[i]

    # Row 2
    for i in range (1, 32, 6):
        last_match = 0
        if row[i] == row[i+6]:
            if row[i] == "1":
                player_one_count += 1
            elif row[i] == "2":
                player_two_count += 1
            last_match = row[i]

    # Row 3
    for i in range (2, 33, 6):
        last_match = 0
        if row[i] == row[i+6]:
            if row[i] == "1":
                player_one_count += 1
            elif row[i] == "2":
                player_two_count += 1
            last_match = row[i]

    # Row 4
    for i in range (3, 34, 6):
        last_match = 0
        if row[i] == row[i+6]:
            if row[i] == "1":
                player_one_count += 1
            elif row[i] == "2":
                player_two_count += 1
            last_match = row[i]

    # Row 5
    for i in range (4, 35, 6):
        last_match = 0
        if row[i] == row[i+6]:
            if row[i] == "1":
                player_one_count += 1
            elif row[i] == "2":
                player_two_count += 1
            last_match = row[i]

    # Row 6
    for i in range (5, 36, 6):
        last_match = 0
        if row[i] == row[i+6]:
            if row[i] == "1":
                player_one_count += 1
            elif row[i] == "2":
                player_two_count += 1
            last_match = row[i]

    if player_one_count > player_two_count:
        return 1
    elif player_two_count > player_one_count:
        return 2
    elif player_one_count == player_two_count:
        return 0


# Feature 5 - Which player has a piece in the middle spot in the bottom column?
def countBottomMiddle (row):
    if row[18] == "1":
        return 1
    elif row[18] == "2":
        return 2
    else:
        return 0



# Write to output file.
j = 0
y = []
new = [1000]
for row in inputreader:
    y.append(row[42])       # Grab results column

    # Add feature values to each row in appropriate column.
    if j != 0:
        new_col_one.append(row[0])                          # Feature 1
        new_col_two.append(countCenterCols(row))            # Feature 2
        new_col_three.append(countLastColPiece(row))        # Feature 3
        new_col_four.append(countHorizontalConnect(row))    # Feature 4
        new_col_five.append(countBottomMiddle(row))         # Feature 5
    # Append to row.
    row.append(new_col_one[j])
    row.append(new_col_two[j])
    row.append(new_col_three[j])
    row.append(new_col_four[j])
    row.append(new_col_five[j])
    # Write row out to file.
    writer.writerow(row)
    j += 1


################################ DECISION TREE CODE ################################

# Separate X (2D array of features), Y (1D array of results)

new_col_one.pop(0)
new_col_two.pop(0)
new_col_three.pop(0)
new_col_four.pop(0)
new_col_five.pop(0)


# x = array of 1000, 5 elements each
x = []
for i in range(0, 1000):
    temp = [new_col_one[i], new_col_two[i], new_col_three[i], new_col_four[i], new_col_five[i]]
    x.append(temp)
y.pop(0)

# Split into training, test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

# Create decision tree classifier
tree = DecisionTreeClassifier (max_depth=5)

# Fit data
tree.fit(x_train, y_train)

# Cross validation
scores = cross_val_score(tree, X=x, y=y, cv=5)

features = ["Bottom Left", "More in Center Columns", "More Top Column Pieces", "Horizontal Connections", "Bottom Row Middle Column"]
classes = ["Player 1", "Player 2"]
dot_data = export_graphviz(tree, out_file="tree.dot", feature_names=features, class_names=classes, rounded=True, filled=True)
