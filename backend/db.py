from neo4j import GraphDatabase
import dotenv
import os

dotenv.load_dotenv()

def connect_db():
  driver = GraphDatabase.driver(uri="neo4j+s://9524d542.databases.neo4j.io", auth=("neo4j","P0WTzEncW6njSdQc6iGe3k5B1HrdaMhqiW5i90hgXGI"))
  print(driver.verify_connectivity())
  return driver