#insert function just like a controller function

#views.py
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import User 
from .models import UploadedImage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from django.core.files.storage import FileSystemStorage
def upload_image(request):
    """Handles image upload and classification."""
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']

        # Validate file type
        if not image_file.name.lower().endswith(('jpg', 'jpeg', 'png')):
            return render(request, 'isnjack_app.leaf.html', {
                'error': 'Unsupported file format. Please upload a JPG or PNG image.'
            })

        fs = FileSystemStorage()
        saved_path = fs.save(image_file.name, image_file)
        full_path = fs.path(saved_path)

        try:
            # Preprocess the image
            image = load_img(full_path, target_size=(150, 150))
            image_array = img_to_array(image) / 255.0  # Normalize the image
            image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

            # Model prediction
            predictions = model.predict(image_array)
            confidence = round(np.max(predictions) * 100, 2)  # Confidence as a percentage
            result = LABELS[np.argmax(predictions)]  # Predicted label

            # Save the result in the database
            uploaded_image = UploadedImage.objects.create(
                user=request.user,
                image=image_file,
                result=result,
                confidence=confidence
            )

            # Pass the image, result, and confidence to the template
            return render(request, 'isnjack_app.leaf.html', {
                'image': uploaded_image.image.url,
                'result': result,
                'confidence': confidence
            })

        except Exception as e:
            # Log the error for debugging
            
            return render(request, 'isnjack_app.leaf.html', {
                'error': 'There was an issue processing your image. Please try again.'
            })

    return render(request, 'isnjack_app.leaf.html')





# Create your views here.

def index(request):
    user = User.objects.all()
    return render(request, 'insjack_app.index.html', {
        'user' : user 
    })

def register(request):
    user = User.objects.all()
    return render(request, 'insjack_app.register.html', {
        'user' : user 
    }) 

def dashboard(request):
    return render(request, 'insjack_app.home.html')

def leaf(request):
    return render(request, 'insjack_app.leaf.html')

