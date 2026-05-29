import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import io;

# Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('models/pneumonia_classifier.h5')

def preprocess_image(image):
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize image
    image = image.resize((224, 224))
    
    # Convert to array and preprocess
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    
    return img_array

def main():
    st.title("Pneumonia X-Ray Classification")
    st.write("Upload a chest X-ray image to check for pneumonia")
    
    # Load model
    try:
        model = load_model()
    except Exception as e:
        st.error("Error loading model. Please make sure the model file exists.")
        return
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded X-ray image', use_column_width=True)
        
        # Add a prediction button
        if st.button('Predict'):
            # Preprocess the image
            processed_image = preprocess_image(image)
            
            # Make prediction
            prediction = model.predict(processed_image)
            probability = prediction[0][0]
            
            # Display results
            st.write("## Results")
            if probability > 0.95:
                st.error(f"Pneumonia detected with {probability:.2%} probability")
            else:
                st.success(f"Normal X-ray with {1-probability:.2%} probability")
            
            # Display probability bar
            st.progress(float(probability))

if __name__ == "__main__":
    main() 