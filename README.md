# ankistatsonmenu

# Description

![Screenshot 2022-02-26 at 00 37 06](https://user-images.githubusercontent.com/8883914/155821021-10dd2437-4cb4-4c31-aa91-6b889129ff32.png)

This app allows the display of user-specified anki decks' remaining daily reviews to the macOS menu bar. It updates the remaining count every 30 seconds and saves your previous configuration when closing and re-opening the app.

Note this is a mac only app and will not work on windows or other operating systems.

# Download/Installation instructions

Go to the "Releases" page by clicking on the "Releases" link on the right hand side of this page. Scroll down to and click on the "assets" toggle near the bottom of the releases page. Download the dist.zip file, extract it, open the resulting folder and inside will be the .app file which you can double click to start the app.

Feel free to copy this .app file to your applications folder or drag it onto your mac's dock for easier access.

To make sure it is connected properly to your anki, ensure you have installed the anki connect plugin/addon within the anki app.

# Usage instructions

Note that when adding decks, the name of the deck must be an exact match. If you wish to add subdecks, you can press the gear icon next to the name deck on anki and it will show you the name you must use. It will include two colons "::" at each level of subdeck.

If you want to add multiple decks/subdecks in one go, you can do this by writing a semicolon ";" between each deck/subdeck name but make sure not to add spaces either side of the semicolon. The permisiveness of the deck/subdeck input/removal will be improved in a future version.

# Acknowledgements

This small tool was bashed together using: rumps, anki-connect API and pickle.

Thank you to the developers of these for their hard work, which has let even a total beginner like me to make this personal project.
