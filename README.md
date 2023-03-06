# Youtube Video QR Code Generator
## This Python code generates a QR code for a YouTube video and saves it with the specified video name, by allowing the user to input the video link.

# How to Use?
- Download this code to your computer.
- Install required libraries (qrcode, requests, pytube, re, io).
- Run the code and enter a YouTube video link.
- The program will clean the video name from invalid characters, generate a QR code and save it.
# Requirements
- Python 3.x
- qrcode library
- requests library
- pytube library
- re library
- io library
# Installation
To install required libraries, use the following commands:
```python
pip install qrcode
pip install requests
pip install pytube
```
# Notes
- This program does not perform any validation before entering a YouTube video link to ensure that a valid link is entered.
- The QR code will be saved to the directory where the program is located.
- The video name will be created after removing invalid characters.
