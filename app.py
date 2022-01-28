import streamlit as st
from fastai.vision import *
import PIL.Image

html_temp = """
    <div style="background-color:ghostwhite;padding:10px;margin-bottom: 25px">
    <h2 style="color:black;text-align:center;">OCT images Classifier</h2>
    <p style="color:black;text-align:center;" >This is a <b>Streamlit</b> app used to classify <b>Normal, CNV and Drusen</b>.</p>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

proj_path = ''
p_path = Path(proj_path)

learner = load_learner(proj_path, 'OCT_squeezenet.pkl')

option = st.radio('', ['Choose a test image', 'Choose your own image'])

if option == 'Choose your own image':
  uploaded_file = st.file_uploader("Choose an image...", type=None)
  if uploaded_file is not None:
    img = PIL.Image.open(uploaded_file)
    import torchvision.transforms as tfms
    def pil2fast(img):  
      return Image(tfms.ToTensor()(img))
    pred_class,pred_idx,outputs = learner.predict(pil2fast(img))
    st.image(img)
    st.write('Prediction:',pred_class)
    
if option == 'Choose a test image':
  test_images = os.listdir('Sample images')
  test_image = st.selectbox('Please select a test image:', test_images)
  file_path = 'Sample images/' + test_image
  img = PIL.Image.open(file_path)
  import torchvision.transforms as tfms
  def pil2fast(img):  
    return Image(tfms.ToTensor()(img))
  pred_class,pred_idx,outputs = learner.predict(pil2fast(img))
  st.image(img)
  st.write('Prediction:',pred_class)
