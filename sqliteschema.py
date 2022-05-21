import json
import sqliteschema

extractor = sqliteschema.SQLiteSchemaExtractor('C:/Users/Innovative Pasantía/Documents/Proyectos/SqliteToPostgres/app.db')

print("--- dump all of the table schemas with a dictionary ---\n{}\n".format(
    json.dumps(extractor.fetch_database_schema_as_dict(), indent=4)))

print("--- dump a specific table schema with a dictionary ---\n{}\n".format(
    json.dumps(extractor.fetch_table_schema("sampletable1").as_dict(), indent=4)))