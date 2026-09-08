# STEELFLOW REVERSE ENGINEERING PROCESS

## Task 1 — Project Setup
- Created the project structure in VS Code.
- Created a Python virtual environment.
- Started working with the backend.

Command:
python -m venv .venv


## Task 2 — Activate Virtual Environment
- Activated the Python virtual environment.

Windows:
.venv\Scripts\activate


## Task 3 — Install Dependencies
- Installed the required backend packages.
- Learned that requirements.txt contains project dependencies.

Command:
pip install -r backend/requirements.txt


## Task 4 — FastAPI Introduction
- Learned what FastAPI is.
- FastAPI is used to build APIs using Python.
- Created the FastAPI application.


## Task 5 — Run FastAPI
- Learned that Uvicorn runs the FastAPI application.

Command:
uvicorn backend.app.main:app --reload

Important:
module:object
backend.app.main = Python module
app = FastAPI object


## Task 6 — Health Endpoint
- Created a health-check endpoint.
- Learned how GET endpoints work.

Endpoint:
GET /health

Response:
{
    "status": "healthy"
}


## Task 7 — Hello Endpoint
- Created a simple GET endpoint.
- Learned how FastAPI returns JSON.

Endpoint:
GET /hello

Response:
{
    "message": "hello steelflow"
}


## Task 8 — Pydantic Introduction
- Learned what Pydantic is.
- Pydantic validates and structures data.
- Learned about BaseModel.


## Task 9 — Truck Model
- Created a Truck Pydantic model.
- Added:
  licence_plate
  bundle_count

Example:
class Truck(BaseModel):
    licence_plate: str
    bundle_count: int


## Task 10 — Pydantic Object
- Created a Truck object from the Truck model.
- Learned the difference between a class and an object.

Truck = class/model
truck = object/instance


## Task 11 — Type Validation
- Tested invalid data with Pydantic.
- Learned that Pydantic validates field types.
- Invalid values can produce ValidationError.


## Task 12 — API Endpoint
- Learned what an API endpoint is.
- An endpoint is a specific path accessed using an HTTP method.


## Task 13 — GET vs POST
- Learned the difference between GET and POST.

GET:
Used to retrieve data.

POST:
Used to send data to the backend.


## Task 14 — Test POST API
- Created POST /trucks.
- Tested the endpoint using Swagger UI.
- Sent Truck JSON data.
- Received HTTP 200 response.

Endpoint:
POST /trucks

Example request:
{
    "licence_plate": "UP16563",
    "bundle_count": 450
}


## Task 15 — Custom POST Response
- Modified POST /trucks.
- Used values from the Truck object.
- Returned a custom JSON response.

Used:
truck.licence_plate
truck.bundle_count

Response:
{
    "plate": "UP16563",
    "count": 450,
    "message": "truck received"
}


## Task 16 — Pydantic Validation
- Imported Field from Pydantic.
- Added a minimum value to bundle_count.

Used:
Field(ge=0)

Meaning:
bundle_count must be >= 0.

Negative bundle counts are rejected.

Invalid request produced:
422 Unprocessable Entity


## Task 17 — GET Truck
- Created GET /trucks.
- Returned truck information as JSON.
- Learned how a GET endpoint can read data from an object.

Endpoint:
GET /trucks

Response:
{
    "plate": "UP16562",
    "count": 415
}


## Task 18 — Multiple Trucks
STATUS: NOT COMPLETED

Goal:
- Create 3 Truck objects.
- Store them in a Python list.
- Create GET /all-trucks.
- Return all trucks.

Next task to complete.


--------------------------------------------------
IMPORTANT COMMANDS LEARNED
--------------------------------------------------

python -m venv .venv
→ Create virtual environment.

.venv\Scripts\activate
→ Activate virtual environment.

pip install -r backend/requirements.txt
→ Install project dependencies.

uvicorn backend.app.main:app --reload
→ Start FastAPI development server.

Ctrl + C
→ Stop the running server.


--------------------------------------------------
GIT COMMANDS
--------------------------------------------------

git init
→ Start Git repository.

git status
→ Check changes.

git add .
→ Add all changes to staging.

git commit -m "message"
→ Save changes as a commit.

git push
→ Upload commits to GitHub.

git pull
→ Get latest changes from GitHub.

git clone URL
→ Download a GitHub repository.

git branch
→ See branches.

git switch branch-name
→ Switch branch.

git merge branch-name
→ Merge a branch.

git log --oneline
→ See commit history.

git diff
→ See code changes.

git remote -v
→ Check GitHub connection.


--------------------------------------------------
DAILY GIT WORKFLOW
--------------------------------------------------

git status
↓
git add .
↓
git commit -m "message"
↓
git push