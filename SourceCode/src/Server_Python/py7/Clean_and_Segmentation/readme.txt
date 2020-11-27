this function concludes preprocessing stage, using Mostafa Cheikh's work with some modification that fits our work
see link : https://www.moustaphacheikh.com/2017/11/17/preprocessing
and  the sentence segmentation of   ArabicProcessingCog projct 
see  https://github.com/disooqi/ArabicProcessingCog/tree/0583e64cb5118cf279e86020944a1d348637d434


input : Input.txt (the encoding must be UTF 8 )
output: filename.txt with "SEG_" prefix on the name (ex: filename.txt ---> SEG_filename.txt)

Note:  the output file location will be at the script's same path 
       The is intended for Python 3
	   the script.py must be in the same folder with Seg_clean.py
