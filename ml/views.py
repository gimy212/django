from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from rest_framework.decorators import api_view
from PIL import Image
import os
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response

# predict using the loaded model
@api_view(['POST'])
def predict2(request):
    # load the saved model from file
    model = load_model(r'C:\Users\IT\Desktop\src\ml\models\my_model.h5')

    image_file = request.FILES['image']
    image = Image.open(image_file).convert('L')
    image = image.resize((200, 200))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=-1)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)
    max_prediction = np.argmax(prediction)
    print(f"<{max_prediction}>")
    if max_prediction == 0:
        result = 'Cyst'
    elif max_prediction==1:
        result = 'Normal'
    elif max_prediction==2:
        result='Stone'
    else:
        result='Tumor'
    print(f"<{max_prediction}>")
    return Response({'result': result})
