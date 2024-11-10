<h1>CLI - Dictionary (Discouninued)</h1>

This is a command line interface (CLI) program for searching the definition, example sentence and translation of an English word using the free dictionaryapi.dev API and the googletrans Python package.
<h3>Requirements</h3>

To use this program, you need to have Python 3.x installed on your system. You can download Python from the official website at https://www.python.org/downloads/.

You also need to install the following packages:

    requests
    json
    googletrans

You can install them by running the following command in your terminal:

    pip3 install requests json googletrans
     
<h3>or</h3>
   
   
    pip3 install -r requirements.txt
    
<h3>How to use</h3>

To use this program, simply run the dictionary.py file in your terminal with the command:
      cd CLI---Dictionary 
<h4>and</h4>
      python3 dictionary.py

You will be presented with the following options:

    |-------------------------------------------------------|
    |   Press 1 for show this screen                        |
    |   Press 2 for enter the word and find the definition  |
    |   Press 3 for translate the given word                |
    |   Press 4 for both definition and translate           |
    |   Press 5 for translation of the definition           |
    |   Press 6 for give example sentence if available      |
    |   press 7 for translate the sentence                  |
    |   Press 8 for write everything for future reference   |
    |   Press 9 for exit                                    |
    |-------------------------------------------------------|

<h4>Press 1: to show the options again.</h4>
    <h4>Press 2: to enter a word and find its definition.
    <h4>Press 3: to enter a word and translate it to Tamil.
    <h4>Press 4: to enter a word and display both its definition and Tamil translation.
    <h4>Press 5: to enter a word, find its definition, translate the definition to Tamil and display both.
    <h4>Press 6: to enter a word and display an example sentence (if available) with its Tamil translation.
    <h4>Press 7: to enter a sentence and translate it to Tamil.
    <h4>Press 8: to enter a word, save its definition, example sentence and Tamil translations to a file for future reference.
    <h4>Press 9: to exit the program.
<h3>Special option - Option 8</h3>


I am create a free defined file <h5>ref.txt</h5> for save word,definitation,translated sentence and example 
    
<h3>Translate to other languages</h3>
To change the language you are translating to or from, you can modify the dest parameter for the destination language and src parameter for the source language in the Translator().translate() function from the googletrans library.

For example, to translate from English to French, you can change the dest parameter to "fr", which is the language code for French

Here are some of the most commonly used language codes for the Google Translate API:

    Afrikaans: af
    Arabic: ar
    Bengali: bn
    Chinese (Simplified): zh-CN
    Chinese (Traditional): zh-TW
    Dutch: nl
    English: en
    French: fr
    German: de
    Greek: el
    Hindi: hi
    Italian: it
    Japanese: ja
    Kannada: kn
    Korean: ko
    Malayalam: ml
    Marathi: mr
    Portuguese: pt
    Russian: ru
    Spanish: es
    Tamil: ta
    Telugu: te
    Turkish: tr

You can find a complete list of language codes supported by Google Translate on their website.


<h3>License</h3>


This program is licensed under the MIT License. See the LICENSE file for more information.
