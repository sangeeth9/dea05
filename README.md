#MVP Library Apprenticeship
PM Task
Load the two datasets
Clean the them (thoroughly)
Measure at least 1 data engineering metric in the data cleaning process (ie dropped rows)
MVP: Output the cleaned files as a local csv.
Stretch:

Output the cleaned files into the local SSMS (use SQLAlchemy); create a new DB for this.
Refactor your code into modular functions.
Day 2
AM Task:
Focus on having at least one function like:
dataEnrich():
Calculate the days between the two date columns and add it as a new col.
fileLoader
duplicateCheck
naCheck
dataCleaner
addToSQL

....