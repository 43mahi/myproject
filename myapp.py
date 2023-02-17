import streamlit as st
from PIL import Image
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Tool Wear Prediction System",page_icon="memo",layout="wide")

img1 = Image.open('logoimg.png')

st.header("Tool Wear prediction")


st.sidebar.image(img1)
st.sidebar.header("Predict Tool wear")
img = st.sidebar.file_uploader("Choose Input Image",type=["jpg"])

def r2_score(y_true,y_pred):
    u = sum(square(y_true-y_pred))
    v = sum(square(y_true-mean(y_true)))
    return (1-u/(v+epsilon()))

model = load_model('mysurface_model.h5',custom_objects={"r2_score": r2_score})

if img:
	img = Image.open(img)
	st.image(img,caption="Surface Image")
	img_grey = img.convert("L")
	img_grey = img_grey.resize((64,64))
	imgs = np.array(img_grey)
	data = np.reshape(imgs,(1,64,64,1))

	wear = model.predict(data)

	if st.sidebar.button("Predict Wear "):
    		st.subheader("Predicted Tool Wear : {}".format(wear[0][0]))


