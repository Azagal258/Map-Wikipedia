######## Libraries ########

import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os
import mysql.connector


######## Functions ########

### Nodes processing ###

def extract_infos(document_xml: str) -> list:
    """ 
    Extract all usefull infos (here : IDs, Namespaces, Titles and Revision IDs) and contatenates them in a list of tuples
    in view of inputting them into the database
    
    Parameters :
    - document_xml (str) : the path to the file

    Outputs :
    - list of tuples : list a list of tuple as (id, ns, title, revision id)
    """
    out_tuples = []
    tree = ET.parse(document_xml)
    root = tree.getroot()

    for page in root.findall('{http://www.mediawiki.org/xml/export-0.10/}page'): #'for variable in root.iter('{le truc xmlns}nom_de_la_balise')' 

        id = page.find('{http://www.mediawiki.org/xml/export-0.10/}id')
        ns = page.find('{http://www.mediawiki.org/xml/export-0.10/}ns')
        titles = page.find('{http://www.mediawiki.org/xml/export-0.10/}title')
        rev_id = page.find('{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}id')

        out_tuples.append((id.text, ns.text, titles.text, rev_id.text))

    return out_tuples

def init_db(infos: list):
    """ 
    Connects to a pre-established database with data from a .env file containing all connection informations.
    Then adds all data given in input

    Parameters :
    - infos (list) : a list of tuples containing values to input
    """
    load_dotenv()
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

    # Establish a connection to the MySQL database and create cursor
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = conn.cursor()

    #First querry
    insert_first_set = """
    INSERT INTO article_infos_final (ai_id_general, ai_namespace, ai_title, ai_id_revision)
    VALUES (%s, %s, %s, %s)
    """

    #Inputs
    cursor.executemany(insert_first_set, infos)

    #Closes connection
    conn.commit()
    cursor.close()
    conn.close()

######## Magic Land ########

### Inputs ###
# document_xml = "test_article.xml"
document_xml = "F:/Scrap Wikipedia/Dumps/XML_files/frwiki-20240301-pages-articles-multistream1.xml"


### Code ###
bulk = extract_infos(document_xml)
print("Extraction done")
init_db(bulk)
print("Database created")