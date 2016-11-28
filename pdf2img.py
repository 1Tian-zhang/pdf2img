#coding=utf-8
import ghostscript
import os,traceback
from pyPdf import PdfFileReader

def get_pdf_page_count(path):
    pdf_page_count = None
    if os.path.exists(path):
        try:
            with open(path,"rb") as f:
                pdf_page_count = PdfFileReader(f).numPages
        except Exception,e:
            traceback.print_exc()
    return pdf_page_count

def _pdf2img(pdf_input_path, jpeg_output_path,convert_page_index):
    args = ["pdf2jpeg", # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r144",
            "-dFirstPage=%d"%convert_page_index,
            "-dLastPage=%d"%convert_page_index,
            "-sOutputFile=%s"%jpeg_output_path,
            #"-o %03d.jpeg",
            pdf_input_path]
    ghostscript.Ghostscript(*args)

def pdf2img(pdf_path,export_img_path):
    if not os.path.exists(pdf_path):
        print "pdf file not find"

    if not os.path.exists(export_img_path):
        try:
            os.mkdir(export_img_path)
        except Exception,e:
            print "export_img_path is None and %s"%e

    pdf_page_count = get_pdf_page_count(pdf_path)
    for page_num in xrange(1,pdf_page_count+1):
        try:
            _pdf2img(pdf_path,export_img_path+"/%d.jpg"%page_num,page_num)
        except Exception,e:
            print "in page %s can't not export,skip"%page_num

#print get_pdf_page_count("Catalog TSC Mud Pump Spare Parts 2016 copy.pdf")
#_pdf2img("Catalog TSC Mud Pump Spare Parts 2016 copy.pdf","./test.jpg")
pdf2img("Catalog TSC Mud Pump Spare Parts 2016 copy.pdf","./test")