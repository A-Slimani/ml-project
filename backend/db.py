from neo4j import GraphDatabase
import dotenv
import os

dotenv.load_dotenv()

def open_connection():
  URI = os.getenv('NEO4J_URI')
  AUTH = (os.getenv('NEO4J_USERNAME'), os.getenv('NEO4J_PASSWORD'))

  with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

