from PyPDF2 import PdfWriter


merger = PdfWriter()


for pdf in ["Agile Project Management.pdf","Databases and SQL for Data Science.pdf"
            ,"Git and Github.pdf","Introduction to Data Engineering.pdf","Introduction to Relational Databases.pdf","Linux and Shell Scripting.pdf","Python.pdf",
            "Cloud Computing.pdf","High Performance Collaboration.pdf","Web Development.pdf"]:
    merger.append(pdf)

merger.write('Merged Certificates.pdf')
merger.close()