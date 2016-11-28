# pdf2img
convert all pdf pages to imgs with python 

#Overview

pdf2img use ghostscript to convert pdf to img in each pdf pages. it can work on any type of 
pdf file regardless the pdf is native or scanned.

but the file `only-can-find-img-in-pdf-and-convert-to-img.py` can only work on scnned pdf or pdf that all pages are images.
because it just only extract images from pdf and will ingore the text. 

by the way, `only-can-find-img-in-pdf-and-convert-to-img.py` is comes from another author on github,but i am so sorry because
i forget where did i cite at that time

# Usages
by

      from pdf2img import pdf2img
      pdf2img(pdf_file_path,img_export_path)
  
and it will auto convert pdf to img files.
if img_export_path doesn't exists,it will create the directory of img_export_path

# Install

      pip install pdf2img
