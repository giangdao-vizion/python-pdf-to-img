## How to run

1. Install python3
2. Start a virtual env in python to make sure no conflict with other tools
> cd /path/to/your/project
> python3 -m venv .venv
> source .venv/bin/activate

3. Install PyMuPDF
> pip install PyMuPDF

4. Put the input.pdf file in the root folder

5. execute the pdf_ti_img.py
> python ./pdf_to_img.py 


## Config
Inside pdf_to_img.py there is config: 
> pdf_to_jpeg("input.pdf", "output_images", dpi=300)

`dpi` can be adjust to change output quality. Higher dpi => higher quality