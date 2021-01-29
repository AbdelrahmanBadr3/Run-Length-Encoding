# Run-Length-Encoding
## Functions:
### imOpen
    * input: string representing the name of an image file (.bmp)
    * output: Image1 object representing the opened image file after turning it tograyscale - 
### toStrH
    * input: Image object representing a grayscale image
    * output: a string representing row-wise run-length code (horizontal runs) 
### toStrV
    * input: Image object representing a grayscale image
    * output: a string representing column-wise run-length code (vertical runs) 
### toFile
    * inputs: a string representing the name of a .txt file
        * note that the string will also include the extension (e.g. ‘f1.txt’)
        * a string representing the run-length code of an image, to be written to a text file
    *   output: a .txt file with the given name containing the given run-length code • note that this file is written to the workspace, not returned by the function
### toImg
    *   input:astringrepresentingthenameofa.txtfile(withextension)containing run-length code of an image
    *   output: Image object representing the grayscale image generated from the given run-length code