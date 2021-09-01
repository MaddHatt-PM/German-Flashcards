# German-Flashcards
Using this to learn German and Python since I don't like writing tons of flashcards and I'm new to Python.


## TODO List
- [ ] Figure out how to handle multiple py files
- [ ] Change around names since I'm shoehorning in C# naming conventions...
- [ ] GuessTheTranslation game
    - [x] Move away from the main file 
    - [x] Display the correct version of words when incorrect
    - [x] When comparing an answer to the player input, compare as lower case
    - [x] Flip from German to English
    - [x] Compute {#,#,#} as a reference ID tuple to cells. When attempting to display, substitute out the {#} with a linked cell, or as nothing
    - [x] Options menu
        - [x] Toggle for language swapping
        - [x] Kategorie selection (defaults to all words)
        - [ ] Toggle to show category (in German)
    - [ ] Better string displaying by removing ', ...'
- [ ] Move vocabData to a class
    - [ ] On creation, create category list
        - [ ] Keep category list ordered
- [ ] Move helper files and "global" variables to a utility file
- [ ] Keep track of last ~50 incorrect words and store into file as JSON
    - [ ] Loadable from different sessions
- [ ] Implement categories as a vocabWords processor
    - [ ] Implement last ~50 incorrect words as a special category

- [ ] Output session data so I can use them for R and data analysis
    - [ ] Amount of vocab words on startup
    - [ ] What was played?
        - [ ] Correct / Total
        - [ ] Start time - End time
        - [ ] Difficult kategories
## Bug Tracker
- [ ] Current vocabSetup is too complicated and prone to bugs(who could've guessed)
- [ ] Does not play normally in the terminal... VSCode might be doing additional debugging stuff that helps?