# Fusion Script Tutorial README

## Introduction
This script is designed to scrape design history and model specifications for your Fusion Project, aiding in efficient CAD design for robotics. This README provides step-by-step instructions to set up and use the script effectively.

## Important Notes
- **Capture Design History:** Ensure that 'Capture Design History' is enabled in Fusion 360. To confirm, check for a timeline at the bottom of your screen. You can also click the gear icon on the bottom right of the screen for verification.
- **CSV File Path Configuration:** Before the script can function on your machine, edit **line 95** to specify the complete path where the CSV file created by the script will be stored.

## Video Tutorial
For a detailed walkthrough, watch the video tutorial here: [Video Tutorial](https://www.youtube.com/watch?v=NA3KkmzRYl4)

## Setup and Usage Steps
1. **Verify Design History:** Ensure 'Capture Design History' is enabled before starting your CAD work.
2. **Access Utilities Menu:** In Fusion 360, go to the Utilities Menu and select 'Add-Ins.'
3. **Create New Script:** Click 'Create' to make a new script. Choose Python as the programming language and name your script.
4. **Save Script:** Press Enter to save your new script.
5. **Edit Script in VS Code:** Select 'Edit' to open the script in Visual Studio Code (VS Code). Install VS Code if prompted.
6. **Paste Script Content:** Copy and paste the contents of `FusionHistoryScript.py` into your newly created script.
7. **Configure CSV File Path:** Modify line 95 in the script to indicate the complete path for storing the generated CSV file.
8. **Save Changes:** Use Ctrl-S to save the file in VS Code, then close the editor.
9. **Run Script:** Back in Fusion 360, click 'Add-ins,' select your new script, and click 'RUN.'
10. **Check CSV Output:** The CSV file should now be available at the specified path.

## Support
For any questions or issues, feel free to reach out via email: [zachary.charlick@duke.edu](mailto:zachary.charlick@duke.edu)

---
Best,
Zach Charlick

---

*This README is intended for educational purposes within the context of the Robot Studio project at Duke University.*
