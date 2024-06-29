import gradio as gr
from PIL import Image, ImageOps
import numpy as np

def converter(img):
    w,h = img.size
    final_w=400
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
                s=s+characters[0]
            elif (img[row][col]<=50):
                s=s+characters[1]
            elif (img[row][col]<=75):
                s=s+characters[2]
            elif (img[row][col]<=100):
                s=s+characters[3]
            elif (img[row][col]<=125):
                s=s+characters[4]
            elif (img[row][col]<=150):
                s=s+characters[5]
            elif (img[row][col]<=175):
                s=s+characters[6]
            elif (img[row][col]<=200):
                s=s+characters[7]
            elif (img[row][col]<=225):
                s=s+characters[8]
            elif (img[row][col]<=250):
                s=s+characters[9]
            else:
                s=s+characters[10]




            # value=0
            # c=0
            # while(img[row][col]>=value):
            #     s=s+characters[c]
            #     c+=1
            #     value+=25
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
    convert=gr.Button("Convert")
    convert.click(fn=converter, inputs=[img], outputs=[result])

demo.launch(share=False)