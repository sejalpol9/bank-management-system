from db_config import connect

print("Connecting to DB...")
try:
    db = connect()
    print("Connected Successfully")
    db.close()
except Exception as e:
    print("ERROR:", type(e).__name__, "-", e)
