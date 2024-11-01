# CrimeSnap
## Criminal Facial Recognition Software with realtime database 
## Developed using Python, OpenCV, and Firebase
---
#### If you have suggestions to improvements or issues, include those in the 'Issues' tab of this repo. Your feedback is appreciated :)
---
### Install Dependencies (Assuming you have python3 already installed)
```
pip install firebase
pip install opencv-python
pip install face-recognition
```
### Setting up realtime database
- #### Visit https://console.firebase.google.com/ 
  - Click on 'Create a Project,' and follow the steps
  - Once your project is created, under the 'Build' section, click on 'Realtime Database' and create a database
  - Copy the reference url, and set databaseURL to the reference url in main.py
  - Go to 'Project settings,' and click on 'Service accounts'
  - Select 'Python' and click on 'Generate new private key'
  - Rename the .json file that downloaded to 'serviceAccountKey.json'
  - Move the 'serviceAccountKey.json' to the same directory as your project

## Accessing CrimeSnap
- Create a folder called CrimeSnap:
```
mkdir CrimeSnap
```
- Navigate to the directory where you created the project folder:
```
cd CrimeSnap
```
- Clone the repository:
```
git clone https://github.com/SD-Coder24/CrimeSnap.git
```

### How to add new data
- I am uploading data this way because I am not using large amounts of data, and also this way keeps it simple
- If you are using a large amount of data, you can upload the data in a .json file and save it to your project directory
- You can load the data from the .json file to the database with the following modification to the code
  - Instead of
```
data = {
    "Loki":
        {
            "Crime": "Loki's Crime",
            "Date of Spotting": "00-00-00",
            "Time of Spotting": "00:00:00"
        },

    "Green Goblin":
        {
            "Crime": "Green Goblin's Crime",
            "Date of Spotting": "00-00-00",
            "Time of Spotting": "00:00:00"
        }
}

for key,val in data.items():
    ref.child(key).set(val)
```
  - Do this:

```
import json

# Load data from JSON file
with open("data.json") as json_file:
    data = json.load(json_file)

# Writing data to Firebase
for key, val in data.items():
    ref.child(key).set(val)
```
