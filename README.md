# gearboxDataModel
SQL data model for gearbox

### Shared utils functions that are unrelated to the model
- gearboxdatamodel/util/bucket_utils.py

### To access migrations from gearbox matching modify gearbox-matching/alembic.ini as follows:
- for building image
script_location = %(here)s/.venv/src/gearboxDataModel/migrations
version_locations = %(here)s/.venv/src/gearboxDataModel/migrations/versions

- for local testing
script_location = %(here)s/env/src/gearboxDataModel/migrations
version_locations = %(here)s/env/src/gearboxDataModel/migrations/versions 

- for local testing you should modify pyproject.toml by adding "develop=true" in gearbox-matching as follows which will copy the migrations into the env/src directory
gearboxdatamodel = { git = "https://github.com/chicagopcdc/gearboxDataModel", branch = "<branch>", develop=true }
