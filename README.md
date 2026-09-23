STEELFLOW
AI-Powered Rebar Bundle Counting & Discrepancy Detection
==========================================================

ABOUT THE PROJECT
-----------------

Hi there!

I am Naresh Kumar Shaw, and along with Aman Kumar Sharma, we are
building this project to learn and understand how an AI-powered
computer vision system works.

The project name is STEELFLOW.

This project is being developed from scratch as a reverse-engineering
and learning project. The goal is not only to build the application,
but also to understand how each component works internally and how
the complete system is connected.


PROJECT OVERVIEW
----------------

SteelFlow is an AI-powered computer vision system designed to detect
and count rebar bundles during the movement of steel material from
trucks to a godown.

The system uses camera feeds placed at different stages of the
material movement process.

The main objectives are:

- Detect and count rebar bundles.
- Track the movement of bundles.
- Count bundles crossing virtual counting lines.
- Compare truck unloading and godown entry counts.
- Detect discrepancies between the two counts.
- Allow a human operator to verify or correct AI-generated results.


REAL-WORLD PROBLEM
------------------

Suppose a truck arrives at a steel godown.

During unloading:

    Truck Unloading Camera
            |
            v
       10 bundles detected

Later, when the material enters the godown:

    Godown Entry Camera
            |
            v
        8 bundles detected

SteelFlow compares both counts:

    Truck Count     = 10
    Godown Count    = 8
    Difference      = 2

The system flags the transaction for human verification.

The operator can then verify whether:

- The AI counted incorrectly.
- A bundle was missed.
- A bundle was moved somewhere else.
- The actual physical count is different.


SYSTEM WORKFLOW
---------------

                    CAMERA 1
               TRUCK UNLOADING
                       |
                       v
                 YOLO DETECTION
                       |
                       v
                 OBJECT TRACKING
                  (ByteTrack)
                       |
                       v
              VIRTUAL COUNTING LINE
                       |
                       v
                UNLOADING COUNT
                       |
                       |
                       v
                 COMPARE COUNTS
                       ^
                       |
                       |
               GODOWN ENTRY COUNT
                       ^
                       |
              VIRTUAL COUNTING LINE
                       ^
                       |
                 OBJECT TRACKING
                  (ByteTrack)
                       ^
                       |
                 YOLO DETECTION
                       ^
                       |
                    CAMERA 2
                 GODOWN ENTRY


TECHNOLOGIES USED
-----------------

Backend:
- Python
- FastAPI
- Uvicorn

Database:
- SQLite
- SQL

Computer Vision:
- YOLO
- ByteTrack
- Virtual Line Counting


YOLO
----

YOLO stands for "You Only Look Once".

YOLO is used for object detection in SteelFlow.

The purpose of YOLO is to analyze each camera frame and identify
objects that the model has been trained to detect.

Conceptually, YOLO provides:

    Object
      |
      +-- Class
      |
      +-- Confidence
      |
      +-- Bounding Box

Example:

    Camera Frame
         |
         v
        YOLO
         |
         v
    Rebar Bundle Detected
         |
         +-- Confidence: 0.91
         |
         +-- Bounding Box:
             (x1, y1, x2, y2)

The bounding box tells the system where the detected object is
located in the frame.

YOLO answers the question:

    "What objects are present in this frame and where are they?"


BYTETRACK
---------

ByteTrack is a multi-object tracking algorithm.

Object detection alone is not enough for SteelFlow.

YOLO processes individual frames. If the same rebar bundle appears
in multiple consecutive frames, the system needs to understand that
these detections belong to the same physical object.

The tracking system maintains an identity for detected objects
across frames.

Example:

    Frame 1:
        Bundle -> ID 1

    Frame 2:
        Bundle -> ID 1

    Frame 3:
        Bundle -> ID 1

    Frame 4:
        Bundle -> ID 1

The tracker answers the question:

    "Is this the same object that I saw in the previous frames?"


YOLO + BYTETRACK
----------------

YOLO and ByteTrack solve different problems.

    YOLO
    ----
    Detects objects.

    "I see a rebar bundle here."


    ByteTrack
    ---------
    Tracks objects.

    "That is the same rebar bundle I was already tracking."


    Counting Engine
    ---------------
    Counts movement.

    "That tracked bundle crossed the counting line,
     so increase the count."


The complete pipeline is:

    Camera
       |
       v
    Video Frame
       |
       v
    YOLO Detection
       |
       v
    Bounding Boxes
       |
       v
    Object Tracking
       |
       v
    Track IDs
       |
       v
    Track Movement
       |
       v
    Virtual Counting Line
       |
       v
    Count Event


WHY TRACKING IS IMPORTANT
-------------------------

Imagine one bundle appears in 20 consecutive video frames.

Without tracking, the system could potentially treat every detection
as a new object.

That could produce:

    Frame 1 -> Count 1
    Frame 2 -> Count 2
    Frame 3 -> Count 3
    ...
    Frame 20 -> Count 20

Even though there is actually only one physical bundle.

Tracking allows the system to maintain the same identity:

    Frame 1  -> ID 7
    Frame 2  -> ID 7
    Frame 3  -> ID 7
    ...
    Frame 20 -> ID 7

When ID 7 crosses the virtual counting line, the counting system
can register the crossing event once.


VIRTUAL COUNTING LINE
---------------------

A virtual counting line is a boundary defined inside the camera
view.

When a tracked object crosses this line, the system registers a
counting event.

Example:

                  Bundle
                    |
                    v
                  [ID 7]
                    |
                    v

    ---------------------------------
             VIRTUAL LINE
    ---------------------------------

                    |
                    v
              LINE CROSSED
                    |
                    v
                 COUNT +1


DISCREPANCY DETECTION
---------------------

SteelFlow compares the counts from the two cameras.

Example:

    Truck Unloading Count = 10
    Godown Entry Count    = 8

    Difference = 10 - 8
               = 2

The system flags this transaction for verification.

Example status:

    Expected Count : 10
    Actual Count   : 8
    Difference     : 2
    Status         : Verification Required


HUMAN VERIFICATION
------------------

AI detection and tracking may not always be perfect.

SteelFlow therefore includes a human verification concept.

A human operator can:

- Review AI-generated counts.
- Verify whether a discrepancy is real.
- Correct an incorrect count.
- Confirm the final result.

The goal is to combine:

    AI Automation
          +
    Human Verification
          =
    Reliable Operational Result


DATABASE
--------

SteelFlow currently uses SQLite.

The database stores information related to trucks and counting
events.

TRUCKS TABLE
------------

    trucks
    |
    +-- id
    |
    +-- licence_plate
    |
    +-- bundle_count


COUNTING EVENTS TABLE
---------------------

    counting_events
    |
    +-- id
    |
    +-- truck_id
    |
    +-- camera_id
    |
    +-- count

The truck_id connects a counting event with a truck.


BACKEND
-------

SteelFlow currently uses FastAPI as the backend framework.

Uvicorn is used to run the FastAPI application.

Current API concepts implemented include:

    GET
    POST
    Path Parameters
    Query Parameters
    Pydantic Validation
    HTTP Exceptions
    SQLite Integration


CURRENT API ENDPOINTS
---------------------

    GET     /health

    GET     /hello

    GET     /trucks

    POST    /trucks

    GET     /all-trucks

    GET     /truck_count

    GET     /truck-search

    GET     /trucks/{truck_id}


CURRENT PROJECT STRUCTURE
--------------------------

    steelflow_reverse/
    |
    +-- .venv/
    |
    +-- backend/
    |   |
    |   +-- app/
    |       |
    |       +-- main.py
    |
    +-- database.db
    |
    +-- .gitignore
    +-- GITHUB_HELP.md
    +-- progress.md
    +-- README.md


LEARNING AND REVERSE-ENGINEERING APPROACH
------------------------------------------

This project is not being developed by simply copying an existing
implementation.

The objective is to understand the complete system and rebuild it
step by step.

The learning path is:

    Python
       |
       v
    FastAPI
       |
       v
    REST APIs
       |
       v
    SQLite
       |
       v
    Database Integration
       |
       v
    SQLAlchemy
       |
       v
    Computer Vision
       |
       v
    YOLO
       |
       v
    Object Tracking
       |
       v
    Virtual Line Counting
       |
       v
    Counting Engine
       |
       v
    Two-Camera Verification
       |
       v
    WebSockets
       |
       v
    Frontend
       |
       v
    Complete SteelFlow System


CURRENT PROGRESS
----------------

Currently implemented and studied:

- FastAPI backend
- Uvicorn server
- REST API endpoints
- Pydantic request validation
- SQLite database
- Trucks table
- Counting events table
- SQL queries
- Python and SQLite integration
- Reusable database functions
- FastAPI and SQLite integration
- Creating trucks through API
- Reading trucks from SQLite
- Database-backed truck data


FUTURE DEVELOPMENT
-------------------

Planned development includes:

[ ] Complete database integration

[ ] SQLAlchemy integration

[ ] Async SQLAlchemy

[ ] Computer vision pipeline

[ ] YOLO object detection

[ ] ByteTrack / object tracking

[ ] Virtual counting lines

[ ] Rebar bundle counting engine

[ ] Camera stream processing

[ ] Two-camera comparison

[ ] Discrepancy detection

[ ] Human verification system

[ ] WebSocket real-time updates

[ ] React frontend dashboard

[ ] Complete system integration

[ ] Deployment


IMPORTANT IMPLEMENTATION NOTE
----------------------------

The project architecture uses YOLO for object detection and
ByteTrack for object tracking.

During the reverse-engineering process, the actual implementation
will be studied carefully to understand whether each component is
implemented directly using an existing library, adapted from an
algorithm, or implemented as a custom solution.

The goal is to understand the difference between:

    What the system is designed to do

and

    What the actual code is doing.


RUNNING THE PROJECT
-------------------

1. Create a virtual environment:

    python -m venv .venv


2. Activate the virtual environment.

Windows:

    .venv\Scripts\activate


Linux / macOS:

    source .venv/bin/activate


3. Install dependencies:

    pip install fastapi uvicorn pydantic


4. Start the server:

    uvicorn backend.app.main:app --reload


5. Open the API:

    http://127.0.0.1:8000


6. Open Swagger documentation:

    http://127.0.0.1:8000/docs


EXAMPLE API REQUEST
-------------------

POST /trucks

Request:

    {
        "licence_plate": "UP16AB1234",
        "bundle_count": 50
    }


Response:

    {
        "plate": "UP16AB1234",
        "count": 50,
        "message": "truck received"
    }


PROJECT PHILOSOPHY
------------------

"Don't just use the system. Understand how the system works."

SteelFlow is being developed as a practical reverse-engineering
and learning project.

Every major component should be:

    UNDERSTOOD
        |
        v
    IMPLEMENTED
        |
        v
    TESTED
        |
        v
    INTEGRATED


AUTHORS
-------

Naresh Kumar Shaw
Aman Kumar Sharma


PROJECT NAME
------------

STEELFLOW

AI-Powered Rebar Bundle Counting & Discrepancy Detection