# ------------------------------


# Read the ReadMe File for getting started instructions/steps


# ------------------------------

# Importing required libraries
import cv2
import face_recognition
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import time

# Get your credentials from the firebase website
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    # Get your database URL from the firebase website
    "databaseURL": "YOUR_DATABASE_URL"
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference("Criminals")

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

# Setting up video footage and facial recognition

video = cv2.VideoCapture(0)

known_face_encodings = []
face_names = []

def load_and_encode(imageFile, name):
    image = face_recognition.load_image_file(imageFile)
    encoded_image = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoded_image)
    face_names.append(name)

load_and_encode(imageFile="photos/Loki.jpeg", name="Loki")
load_and_encode(imageFile="photos/GreenGoblin.jpeg", name="Green Goblin")

def main():
    counter = 0
    while True:
        isWorking, frame = video.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all the faces and face encodings in the video frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings_in_frame = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face in the video frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings_in_frame):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            # Use the face that has the closest match
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = face_names[best_match_index]
                if counter != 0:
                    time.sleep(2)
                ref.child(name).update(
                    {
                        "Date of Spotting": datetime.now().strftime("%m/%d/%Y"),
                        "Time of Spotting": datetime.now().strftime("%H:%M:%S")
                    }
                )
                counter += 1
            else:
                name = "Unknown"
                
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow("Video Footage", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
