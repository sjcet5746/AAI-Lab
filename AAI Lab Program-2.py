#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2

def detect_faces(image_path):
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the image with detected faces
    cv2.imshow('Faces Detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Input image path from the user
    image_path = input("Enter the path to the image: ")
    
    # Call the function to detect faces
    detect_faces(image_path)


# In[17]:


import face_recognition
import cv2

def identify_faces(image_path):
    # Load the image with faces
    image = face_recognition.load_image_file(image_path)
    
    # Find face locations and encodings in the image
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    # Load a sample image to compare against
    known_image = face_recognition.load_image_file("C:/Users/Public/Gskd/AAI/Program-2/Elonmusk.png")
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    
    # Compare each face found in the image with the known face
    for face_encoding in face_encodings:
        # Compare faces
        results = face_recognition.compare_faces([known_face_encoding], face_encoding)
        
        # Print the result
        if results[0]:
            print("This is a known face!")
        else:
            print("This is an unknown face.")

        # Display the face
        cv2.imshow("Face", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Input image path from the user
    image_path = input("Enter the path to the image: ")
    
    # Call the function to identify faces
    identify_faces(image_path)


# In[ ]:


pip install opencv-python


# In[7]:


import cv2


# In[8]:


get_ipython().run_cell_magic('cmd', '', 'where python\n')


# In[9]:


get_ipython().run_cell_magic('cmd', '', 'pip install cmake\n')


# In[10]:


get_ipython().run_cell_magic('cmd', '', 'pip install "C:/Users/Public/Gskd\\AAI/Program-2/dlib-19.24.1-cp311-cp311-win_amd64.whl"\n')


# In[16]:


get_ipython().run_cell_magic('cmd', '', 'pip install dlib\n')


# In[ ]:


get_ipython().run_cell_magic('cmd', '', 'pip install face_recognition\n')


# In[ ]:




