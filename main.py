import gradio as gr
from PIL import Image, ImageOps
import numpy as np

def converter(img,final_w):
    w,h = img.size
    if(w>final_w):
        scale=w//final_w
        img=img.resize((w//scale, h//scale))
    img = ImageOps.grayscale(img) 
    img = np.array(img)
    print(img)
    img=img.tolist()
    characters=['#','X','%','&','*','+','/','(','-',"'",' ']
    s=""
    for row in range(len(img)):
        for col in range(len(img[row])):
            if (img[row][col]<=25):
                s=s+characters[0]*3
            elif (img[row][col]<=50):
                s=s+characters[1]*3
            elif (img[row][col]<=75):
                s=s+characters[2]*3
            elif (img[row][col]<=100):
                s=s+characters[3]*3
            elif (img[row][col]<=125):
                s=s+characters[4]*3
            elif (img[row][col]<=150):
                s=s+characters[5]*3
            elif (img[row][col]<=175):
                s=s+characters[6]*3
            elif (img[row][col]<=200):
                s=s+characters[7]*3
            elif (img[row][col]<=225):
                s=s+characters[8]*3
            elif (img[row][col]<=250):
                s=s+characters[9]*3
            else:
                s=s+characters[10]*3
        s=s+'\n'
    with open('temp.txt', 'w') as f:
        f.write(s)
    
    return('temp.txt')








with gr.Blocks() as demo:
    gr.Markdown("# Image to ascii")
    with gr.Row():
        with gr.Column():
            img=gr.Image(label="Image: ", type="pil")
        with gr.Column():
            result=gr.File(label="Result: ", file_types=['.txt'])
            size=gr.Slider(label="Result width", minimum=10, maximum=1000, value=400, step=1)
    convert=gr.Button("Convert")
    convert.click(fn=converter, inputs=[img,size], outputs=[result])

demo.launch(share=False)