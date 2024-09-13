# Step To Run Lunch Voter Service

### Prerequisite
- Make sure **docker** is already running in you machine

### Prepare and running services

1. Build service image using this command in parent directory
    ```
    make docker-build
    ```
   
2. There should be docker image with `lunch-voter:latest` if build is successful.

3. Go to `docker` directory and run this command to run all required service
    ```
    docker compose up -d
    ```
### Migrate database

1. After services are up. Connect to the database and execute script in `migrations/table_schema.up.sql`

2. If script are succesfully executed. Now backend service should be ready


### Backend service

1. API documentation should be available at `{service_url}:{port}/docs`

2. Some of the API request examples are available at `examples` directory.

3. To create employee and restaurant please use **SERVER_KEY** available in service.env and encoded in base64 as **API KEY** in the request header.

4. To upload menu please use `menu_template.csv` as a reference on how the data structure required for uploading menu. **Code** and **API Key** for this endpoint can be found in the database.

5. To vote for menu please use `access_token` for each user which available at `/access_token` endpoint.