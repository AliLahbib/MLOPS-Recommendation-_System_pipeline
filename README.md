# 🎓 Student Recommendation System - MLOps Pipeline

A complete Machine Learning Operations (MLOps) pipeline for a student academic orientation recommendation system. This project demonstrates modern ML deployment practices using FastAPI, Docker, and CI/CD pipelines.

### 📋 Project Overview

This is a machine learning system that predicts and recommends suitable academic programs (Science, Commerce, Arts, etc.) for students based on their grades in various subjects.

**Key Features:**
- 🤖 Trained RandomForest classifier for multi-class prediction
- 📊 RESTful API built with FastAPI
- 🐳 Containerized deployment with Docker
- 🔄 Automated CI/CD pipeline with GitHub Actions
- ✅ Unit tests for model and API validation
- 📈 Model training pipeline with scikit-learn

### 🏗️ Project Architecture

```
.
├── main.py                          # FastAPI application
├── train_model.py                   # Model training script
├── test_app.py                      # Unit tests
├── recommendation_project.ipynb     # Jupyter notebook (exploratory)
├── student_grades.csv               # Sample input data
├── student_recommendations_final.csv # Training dataset
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker container configuration
├── .github/workflows/ci_pipeline.yml # CI/CD pipeline
└── recommender_model.pkl            # Trained model (generated)
```

### 🚀 Quick Start

#### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Docker (optional, for containerized deployment)
- Git

#### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AliLahbib/MLOPS-Recommendation-_System_pipeline.git
   cd MLOPS-Recommendation-_System_pipeline
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

#### Training the Model

Before using the API, train the machine learning model:

```bash
python train_model.py
```

**Output:**
- ✅ Model accuracy score
- 📊 Classification report
- 💾 `recommender_model.pkl` (saved model file)

#### Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

**Interactive API Documentation:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 📡 API Endpoints

#### 1. **Home Endpoint**
```bash
GET /
```
**Response:**
```json
{
  "message": "Bienvenue sur l'API de recommandation d'orientation !"
}
```

#### 2. **Prediction Endpoint**
```bash
POST /predict
```

**Request Body:**
```json
{
  "Maths": 85.5,
  "History": 78.0,
  "Science": 92.3,
  "English": 88.0,
  "Geograpgy": 76.5,
  "Hindi": 84.0
}
```

**Response:**
```json
{
  "predicted_program": "Science",
  "confidence": 0.95,
  "message": "Recommandation générée avec succès"
}
```

### 🐳 Docker Deployment

#### Build Docker Image
```bash
docker build -t student-recommender:latest .
```

#### Run Container
```bash
docker run -p 8000:8000 student-recommender:latest
```

The API will be accessible at `http://localhost:8000`

### ✅ Testing

Run unit tests to validate the model and API:

```bash
pytest test_app.py -v
```

**Test Coverage:**
- API endpoint validation
- Model prediction accuracy
- Input validation
- Error handling

### 📊 Data Format

#### Input Data (Grades)
The model expects student grades (0-100) in 6 subjects:
- **Maths**
- **History**
- **Science**
- **English**
- **Geograpgy** (note: intentional spelling variation)
- **Hindi**

#### Training Data
The `student_recommendations_final.csv` contains:
- 6 subject grades (features)
- Recommended academic program (target)

### 🔄 CI/CD Pipeline

The project includes automated GitHub Actions workflow (`.github/workflows/ci_pipeline.yml`) that:
- Runs tests on every push
- Validates code quality
- Builds Docker images
- Deploys to production

### 📦 Dependencies

Key libraries:
- **FastAPI** (0.128.0) - Web framework
- **scikit-learn** (1.8.0) - Machine learning
- **pandas** (2.3.3) - Data manipulation
- **numpy** (2.4.0) - Numerical computing
- **pydantic** (2.12.5) - Data validation
- **uvicorn** (included in FastAPI) - ASGI server

See `requirements.txt` for complete dependencies.

### 🛠️ Development

#### Project Structure Overview

**main.py** - FastAPI application with:
- Model loading and initialization
- Request validation with Pydantic
- Prediction endpoint

**train_model.py** - Model training pipeline:
- Data loading
- Feature/target preparation
- RandomForest training
- Model evaluation and saving

**test_app.py** - Comprehensive test suite:
- API endpoint tests
- Model performance tests
- Input validation tests

### 📈 Model Performance

The RandomForest classifier typically achieves:
- Accuracy: 85-95% (depends on data)
- Multi-class classification for 4-6 program categories
- Fast inference (<100ms per prediction)

### 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📝 License

This project is open source and available under the MIT License.

### 📧 Contact

**Author:** Ali Lahbib  
**Email:** [Your Email]  
**GitHub:** [AliLahbib](https://github.com/AliLahbib)

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Last Updated:** December 29, 2025
