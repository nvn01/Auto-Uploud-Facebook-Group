# Facebook Group Post Automation

This is a personal Python program designed to automate posting in Facebook groups. The script uses `PyAutoGUI` to interact with the browser and `tkinter` for the graphical user interface (GUI). 

## Features

- Automatically post in multiple Facebook groups based on a scheduled time and day.
- Customize the content for each post, including captions and images.
- GUI interface for selecting the day and time of posting.
- Ability to stop the program mid-execution if needed.

## How to Use

1. **Run the Program**: Double-click the executable file or run the Python script from the terminal.
2. **Select Day and Time**: Choose the appropriate day and time from the dropdown menus in the GUI.
3. **Click "Run"**: The bot will start posting to the selected Facebook groups according to the specified schedule.
4. **Click "Stop"**: If you need to halt the bot for any reason, you can click the "Stop" button.

## Important Notes

- **Manual Intervention**: Due to the nature of Facebook's dynamic UI, the program requires manual clicking on the "Photo/Video" button before it can proceed with posting. The bot will wait 30 seconds after loading the group page, allowing you to make this manual intervention.
- **Randomization**: The program includes randomized delays to mimic human interaction, reducing the risk of being flagged by Facebook's algorithms.

![Screenshot](./images/screenshot.png)

## Disclaimer

This program is a personal project and is **not intended for public use**. The workflow is tailored specifically to my needs and may be difficult for others to understand or modify without significant effort. Use at your own discretion, and please be aware that automating actions on platforms like Facebook could potentially violate their terms of service.
