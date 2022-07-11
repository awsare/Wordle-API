# Wordle API
A simple API for wordle clones.

## Endpoint
https://thatwordleapi.azurewebsites.net/

## Paths
- `/get/` returns a random five letter word from the Wordle word list.
- `/ask/?word={word}` returns true or false if the inputted word is a valid five letter word.
- `/daily/?day={day}` returns a word based on the day given (1 through 2315).

## Examples
- https://thatwordleapi.azurewebsites.net/get/ =>\
`{"Call":"Get","Response":"mouse","Status":200,"Timestamp":1657565106.6235178}`
- https://thatwordleapi.azurewebsites.net/ask/?word=plant =>\
`{"Call":"Ask","Response":true,"Status":200,"Timestamp":1657565138.3285017}`
- https://thatwordleapi.azurewebsites.net/ask/?word=aaaaa =>\
`{"Call":"Ask","Response":false,"Status":200,"Timestamp":1657565185.0503025}`
- https://thatwordleapi.azurewebsites.net/daily/?day=15 =>\
`{"Call":"Daily","Response":"stink","Status":200,"Timestamp":1657565201.699736}`
- https://thatwordleapi.azurewebsites.net/ask/ =>\
`{"Call":"Ask","Details":"No word provided","Status":400,"Timestamp":1657565380.9049528}`
- https://thatwordleapi.azurewebsites.net/daily/?day=-6.2 =>\
`{"Call":"Daily","Details":"Day must be an integer between 1 and 2315","Status":400,"Timestamp":1657565441.5970824}`
