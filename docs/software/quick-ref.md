# Software Quick References

## Docker

## AWS
### AWS CloudFormation
- Templates: JSON or YAML files that will be used as the blueprints for building AWS resources.
- Stack: a single unit that you manage related resources in AWS CloudFormation
- Change set: a summary of changes to a stack.

## Google Cloud Platform

## Postgres
- Role: a role is an entity that can own database objects and have database privileges; a role can be considered a "user", a "group", or both depending on how it is used

### Postgres cheat sheet
#### Connection
- Connect to database in terminal:
```
PGPASSWORD=*** psql "host=*** user=*** dbname=postgres sslmode=require"
```
- `\conninfo`: Print out connection information

#### Databases
- `\l`: List all databases
- `\c <db_name>`: Connect to a given database

#### Tables
- `\dt`: List all tables.
- `\d+ <table_name>`: Get detailed information of a table.