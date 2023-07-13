# File_sorter
Small app for sorting trash folders by their extensions using Python

Many people have a folder on their desktop that is called something like "Disassemble." As a rule, hands never reach this folder.

The script takes one argument at startup - this is the name of the folder in which it will sort. Suppose the file with the program is called sort.py, then to sort the folder/user/Desktop/Junk, you need to run the script with the python command sort.py/user/Desktop/Junk

The script must pass through the folder specified during the call and sort all files into groups:
- images ('JPEG', 'PNG', 'JPG', 'SVG');
- video files ('AVI', 'MP4', 'MOV', 'MKV');
- documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
- music ('MP3', 'OGG', 'WAV', 'AMR');
- archives ('ZIP', 'GZ', 'TAR');
- unknown extensions.

Functions:
- all files and folders are renamed using the normalize function.
- file extensions do not change after renaming.
- empty folders are deleted
- the script ignores the archives, video, audio, documents, images folders;
- the unpacked content of the archive is transferred to the archives folder in a subfolder named the same as the archive, but without an extension at the end;
- files whose extensions are unknown remain unchanged.

Use console to start an app.
Type "python main.py test"

/b'TEST' IS A NAME OF TRASH FOLDER
