# Decision Trees for Connect Four
CS 4341 Project 3

## Dependencies
This project uses SkLearn to implement the structure of the decision tree model, and is written in Python.


## About

This project extracts five features from a raw Connect Four board state, and implements a decision tree model, using cross-validation to train the model. 
It contains a single .py file that takes in a .csv file of 1000 training examples, identifies specific features in each examples, and produces an output .csv file containing the new feature columns concatenated to the original input file, as specified by the assignment document. Additionally, this file also contains code for creating a Decision Tree Classifier, which will create a file called "tree.dot" in the same directory as the project. This .dot file con be copy-pasted into http://www.webgraphviz.com/ if you wish to visualize my created tree. 

## Running

To run this project, cd into my project and run from the command line: python3 main.py 1 <input.csv> <output.csv>, where input.csv is the name of the file (located within the same directory) that contains the 1000 training examples to be passed in. output.csv should be the name of a file you wish the output data to be written to. It will be created, and should not already exist. Should for whatever reason, the above command does not execute, the command python3 -m main 1 <input.csv> <output.csv> also returned the same results from the command line. 
