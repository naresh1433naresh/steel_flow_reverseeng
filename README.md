# Hii there I am  Naresh Kumar Shaw Im building this project to learn for myself the project name is STEELFLOW im doing reverse engineering and building this project from scratch 

# the project is actually
-Detects and counts rebar bundles using YOLO + ByteTrack.
-Tracks movement through virtual counting lines.
-Compares Truck Unloading vs Godown Entry counts using two cameras.
-Flags discrepancies when, for example, 10 bundles leave the truck but only 8 reach the godown.
-Allows a human operator to verify or correct AI results.

# Structure of project
steelflow_reverse/
│
├── backend/
│   └── app/
│       ├── main.py
│       │
│       ├── api/
│       │   └── routes/
│       │
│       ├── services/
│       │
│       ├── models/
│       │
│       ├── schemas/
│       │
│       └── core/
│
├── tests/
│
├── .gitignore
├── README.md
├── GITHUB_HELP.md
└── requirements.txt

# technologies used 

- Python
- FastAPI
- Uvicorn
- Pydantic
- OpenCV
- YOLO
- PostgreSQL
- pgvector
- Git & GitHub

.........................................