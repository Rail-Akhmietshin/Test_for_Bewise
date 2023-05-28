# Test task for the company Bewise

## Deployment with Docker

After cloning the repository, grant write permissions for the root and its incoming files and folders:

* chmod -R 755 (your path to the root folder)

Starting the project build:

* docker-compose up -d --build

After successfully running the project in Docker, application will be available at:

* http://0.0.0.0:8000

## Web routes:

### Get questions for quizzes:

* Route: http://0.0.0.0:8000/task/get_tasks
* Method: POST
* Data: 
```json
{
  "questions_num": "quantity(int)"
}
```
* Response: 
```json
{
  "last_task": {
    "task_id": "number_task(int)",
    "question": "somebody",
    "answer": "somebody",
    "created_at": "date"
  }
}
```


### Create user:

* Route: http://0.0.0.0:8000/auth/create_user
* Method: POST
* Data: 
```json
{
  "username": "my_name"
}
```
* Response: 
```json
{
    "my_name": {
        "id": "my_unique_id",
        "token": "my_unique_token"
    }
}
```

### Formatting an audio file from wav to mp3:

* Route: http://0.0.0.0:8000/audio/upload
* Method: POST
* Content-Type: multipart/form-data
* Data: 
  <ul>
    <li> user_id: "my_unique_id" </li>
    <li> token: "my_unique_token"</li>
    <li> file: "attached file"</li>
  </ul>
* Response: 
```json
{
    "Download URL": "http://0.0.0.0:8000/audio/record?audiofile_id=YOUR AUDIOFILE UUID&user=YOUR UNIQUE ID"
}
```

### Getting an audio file to download:


* Route: http://0.0.0.0:8000/audio/record?audiofile_id=YOUR AUDIOFILE UUID&user=YOUR UNIQUE ID
* Method: GET
* Response: 
  <ul> 
    <li> Formatted file </li>
  </ul>


### Also:

* All routes are available on http://0.0.0.0:8000/docs or http://0.0.0.0:8000/redoc paths with Swagger or ReDoc.
