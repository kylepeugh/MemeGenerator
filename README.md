# Meme Generator
Generate Memes using Command Line Interface(CLI) and a web application.

## Overview 
The purpose of this project is to make a Meme Generator utilizing Python program language, Command Line tools, and Flask web application. The meme will use either random photos and quotes from the data folder or can be selected by the user from the CLI or with a web URl. The randomly selected quote data will be extracted from the file using the appropriate Ingestor functions based on file type. We will use several different libraries to pass agruments CLI, use other softwarprgramse, size the images and place the quote on the image, make requests to he internet, and make random choices. Once the Meme is created via the CLI it will be saved in the ./tmp folder and the meme created via the web app will be saved in the ./static foler. Continue reading to understand how to set up your computer environment, details on how to run the program using the two different options, and a further explanation of the modules and dependencies.

## Setting Up 

First download the code from my GitHub Repo: https://github.com/kylepeugh/MemeGenerator.git

Create a virtual environment and install all of the dependencies by executing these commands from the terminal

1) python -m venv venv2
2) source venv2/bin/acitvate
3) pip install -r requirements.txt

Download Command-Line tools XpdfReader from this site: 
https://www.xpdfreader.com/pdftotext-man.html

After downloading XpdfReader, add a folder to the Path Environment Variable in your computer system settings by this following these step-by-step instructions from this Stack Overflow post.

https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho

Once, these steps are complete you are ready to Generator memes!

## How to Run Programs
To run the web app interface enter the following in your terminal and run:

##### python app.py

The app.py conatains the Flask app for generating memes on the web. After you execute the above script an http hyperlink will be returned that you can copy and paste to your web browser. On the web page you can either choose a random meme which will use the options in the ._data folder or you click creator. Creater allows you to enter a image URL from the web and to type in a user selected quote and author. The script utilizes the requests library to fetch an image when a URL is given. Once you have selected the random option or entered the required arguments in Creator the meme will appear on the webpage.

To generate a meme using your CLI enter the following in you terminal and run:

##### python meme.py 

By running just meme.py it will create a random meme using the options from the _data folder and save it in the ./tmp folder. The other option is to run meme.py and enter three agruments to make a customized meme. You can pass these agruments by including the options when you run meme.py --path --body --author

--path allows you to enter in a filepath for the user selected image location

--body allows you to manually enter the user selected quote.

--author allows you to put the author name on the quote 

Here is an example of running meme.py from your terminal while passing all three arguements.

##### python meme.py --path ./_data/phots/dog/xander_1.jpg --body 'Python is tough but rewarding' --author 'Kyle Peugh'

**NOTE: The body and author arguments both need inputs or neither will appear on the meme. 

## Modules and Dependencies
#### _data folder

This folder contains quotes an images used to create the memes. The photos folder contains .jpg formatted images and the the quote files contain a collections of quotes 

#### font folder

This folder contains the selected font in a .tff file

#### template folder

This folder contains 3 HTML files and they are used for formatting when making the web app memes.

### MemeEnigine Module 

This mdoule contains a __init__.py file that initializes the the MemeEngine and the MemeEngine.py script.

The MemeEngine.py script is respoonsbile for loading the image using the Pillow library, resizing the image, adding the quote and author to the image, saving the meme, implementing an instance method which returns the new meme file location.

### QuoteEngine Module

Here is a list of the modules contained within the QuoteEngine and a brief explanantion of its purpose. 

 __init__.py: file that initializes the QuoteEngine

 CSVIngestor.py: Responsible for ingesting a CSV file using the Pandas Library to read the CSV file and the interrows method to make the data iterable.

 DOCXIngestor.py: Responsible for ingesting the DOCX file and reading the file using the docx Library.

 PDFIngestor.py: Responsible for ingesting the PDF files. This file uses the several different to modules to prase the quote from the pdf file.

    OS module is responsbile for interacting with the filing system. 

    Subprocess module is responsible for allowing the ingest to run an external program. In this case subprocess is called to allow 'pdftotext' to interpret the data.

    Random module is used to create a random number for the tmp meme file name. 

 TXTIngestor.py: Responsible for ingesting a TXT file by using the readlines method to prase the quotes.

 **Note: All of the file ingestors return a redy-to-use quote.

 Ingestor.py: Realizes the IngestorInterface.py and encapsulates the file ingestor classes listed above.
 
 IngestorInterface.py: Reponsible for creating a abstract base class and defines two methods. Can_ingest method validates whether the file can be ingested. if it can be ingested, it will be used in file ingestors to parse the quote.

 QuoteModel: Responsible for creating a blank template for the quotes to be extracted. 


## Acknowledgemment
Meme Generator Stater Code provided by Udacity 

