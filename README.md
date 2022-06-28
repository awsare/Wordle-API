# Wordle API
A simple API for wordle clones.

## Endpoint
https://wordle-api.awsare.repl.co/

## Paths
- `/get/` returns a random five letter word from the Wordle word list.
- `/ask/?word={word}` returns true or false if the inputted word is a valid five letter word.
- `/daily/?day={day}` returns a word based on the day given (1 through 2315).
