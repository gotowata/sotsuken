from PIL import Image
from telnetlib import RCP
import streamlit as st
import math

image1,image2 = st.columns(2)
with image1:
   image1 = Image.open('1124_s.jpg')
    
with image2:
   image2 = Image.open('1124_s.jpg')

sl = st.slider('θ値', min_value=1,max_value=45)

if sl:
    height = image1.height
    width = image1.width
    src = (0, 0, 
           0,height,
           width, height, 
           width, 0)
    k = sl
    k2 = math.radians(k)
    c = 3.25 
    b = c / k2
    a = math.sqrt(b**2 + c**2)

    d = 30 
    ppi = 300        
    ppc = ppi / 2.54 
    rs = math.atan(c/b)

    deg = math.degrees(rs)

    wid = width * b / a
    x = height / (1 + width * c / a / (d * ppc))
    h = (height - x) / 2 
    y1 = h
    y2 = height - h
    wx = width - wid

    tarl = (wx, y1, 
        wx, y2,
        width, height, 
        width, 0
    )
        
    tarr = (0, 0, 
        0, height, 
        wid, y2, 
        wid, y1
    )

    im1 = image1.transform(
        size=(width,height),
        method=Image.QUAD,
        data=tarl,
        resample=Image.BICUBIC
    )

    im2 = image2.transform(
        size=(width,height),
        method=Image.QUAD,
        data=tarr,
        resample=Image.BICUBIC
    )

    dst = Image.new(mode='RGB', size=(im1.width + im2.width, max(im1.height, im2.height)))
    dst.paste(im1, box=(0, 0))
    dst.paste(im2, box=(im1.width, 0))
    st.image(dst)
