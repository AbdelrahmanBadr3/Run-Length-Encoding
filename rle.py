from PIL import Image
import matplotlib.pyplot as plt

def imOpen(path):
    im = Image.open(path).convert('LA')
    return im

def toStrH(image): 
    row_RLE= "H"+" " + str(image.size[0])+ " "+ str(image.size[1]) + "\n"
    for i in range(0,image.size[1]):
        start=0   
        current_row_color=image.getpixel((start,i))
        for j in range(0, image.size[0]):
            if(image.getpixel((j,i))[0] != current_row_color[0]):
                row_RLE+= str(current_row_color[0]) + " " + str(start) + " "+ str(j-1)+" "
                start=j
                current_row_color=image.getpixel((j,i))
        row_RLE += str(current_row_color[0]) + " " + str(start) + " "+ str(image.size[0]-1)
        row_RLE +="\n"      
    return row_RLE

def toStrV(image): 
    row_RLE= "V"+" " + str(image.size[0])+ " "+ str(image.size[1]) + "\n"
    for i in range(0,image.size[0]):
        start=0   
        current_row_color=image.getpixel((i,start))
        for j in range(0, image.size[1]):
            if(image.getpixel((i,j))[0] != current_row_color[0]):
                row_RLE+= str(current_row_color[0]) + " " + str(start) + " "+ str(j-1)+" "
                start=j
                current_row_color=image.getpixel((i,j))
        row_RLE += str(current_row_color[0]) + " " + str(start) + " "+ str(image.size[1]-1)
        row_RLE +="\n"
    return row_RLE

def toFile(fileName,RLE):
    text_file = open(fileName+".txt", "w")
    text_file.write(RLE)
    text_file.close()

def toImg(fileName):
    count = 0
    im = None
    direction = ""
    num_cols = -1
    num_rows = -1
    with open(fileName) as fp: 
        for line in fp:
            line_info = line.split()
            if (count == 0):             
                direction = line_info[0]
                num_cols = int(line_info[2])
                num_rows = int(line_info[1])
                im =Image.new(mode = "RGB", size = (num_rows, num_cols))    
                print(num_rows,":",num_cols)   
            else:
                if (direction == "H"):
                    for k in range(0,((int)(len(line_info)/3))):
                        for i in range(int(line_info[k * 3 + 1]),int(line_info[k * 3 + 2])+1):
                            im.putpixel((i,count-1),(int(line_info[k * 3]),int(line_info[k * 3]),int(line_info[k * 3])))
                elif (direction == "V"):         
                    for k in range(0,((int)(len(line_info)/3))):
                        for i in range(int(line_info[k * 3 + 1]),int(line_info[k * 3 + 2])+1):
                            im.putpixel((count-1,i),(int(line_info[k * 3]),int(line_info[k * 3]),int(line_info[k * 3])))
            count += 1
    im.save('RLE'+"2"+'.png')
    return im
    







