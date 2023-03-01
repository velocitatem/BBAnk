![logo](./logo.png)

# Black Board Quiz to Anki

This is a simple script to convert a Black Board quiz to an Anki deck. It is not perfect, but it works for me. It is not intended to be a general purpose tool, but rather a tool for my own use. I am sharing it in case it is useful to others.

## Usage
1. Download the quiz JSON submission file from Black Board.
2. Run the script with the JSON file as the first argument and the name of the Anki deck as the second argument.
```bash
python process quiz.json "My Quiz"
```
3. Import the generated Anki deck into Anki.
