# CrimeSnap
## Criminal Facial Recognition Software with realtime database 

## Developed using Python, OpenCV, and Firebase

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
