import sqlite3
import weasyprint
import pandas as pd

def connect_database(db):
    connection = sqlite3.connect(db)
    return connection

def clean_data(df, flag):
    pass

def read_template_html(file_path="pdf_template.html"):
    template_file = open(file_path)
    content = template_file.read()
    template_file.close()
    return content

def df_to_html(df, html_file, title=""):
    ht = ""
    if title != "":
        ht += f"<h2>{title}</h2>\n"
    ht += df.to_html(classes='wide', escape=False, index=False)

    with open(html_file, "w") as f:
        f.write(read_template_html() + ht + "</body></html>")

def create_pdf(df, callback):
    title = "Kalender Akademik PTA 2020/2021" if callback == "kalenderpdf" else "Jadwal Perkuliahan PTA 2020/2021 - 3KA17"
    html_file = f"temp/{callback}.html"
    pdf_file = f"temp/{callback}.pdf"
    df_to_html(df, html_file, title)
    weasyprint.HTML(html_file).write_pdf(pdf_file)

if __name__ == "__main__":
    callback = "jadwal_kuliah" # test
    connection = sqlite3.connect("database.db")
    df = pd.read_sql_query(F"select * from {callback}", connection)

    create_pdf(df, callback)