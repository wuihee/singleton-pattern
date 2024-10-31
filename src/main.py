from singleton import AppContext

config = {"db_url": "sqlite://mydb"}
app_context = AppContext.get_instance(config)
app_context.connect_db()

print(f"Configuration: {app_context.config}")
print(f"Database Status: {app_context.config}")

app_context.close_db()
