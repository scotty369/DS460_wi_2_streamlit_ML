import streamlit as st

st.title("Welcome to *Streamlit* with *Docker*!" )
st.write("These are simple instructions to build Streamlit with Docker.")

st.header("🚀 Why Use Docker with Streamlit?")
st.write("Docker and Streamlit work together to create a streamlined and reproducible development environment for building and deploying data-driven web applications. Here’s why this combination is powerful:")
st.write("- **Reproducibility**: Docker ensures your app runs the same way on any system, avoiding issues with dependencies and configurations.")
st.write("- **Easy Deployment**: Package your app and all its dependencies into a single container, making it easy to share and deploy.")
st.write("- **Isolation**: Keeps your app's dependencies separate from other software, preventing conflicts.")
st.write("- **Scalability**: Docker makes it easier to scale applications by running multiple instances effortlessly.")
st.write("- **Cross-Platform Compatibility**: Docker containers run on any system with Docker installed, making your app accessible to a wider audience.")

st.header("⚙️ Installing Required Software")
st.write("Before getting started, ensure you have the necessary software installed:")
st.write("1. Install [Docker](https://docs.docker.com/get-docker/) for your operating system.")

st.header("📜 How to Get *Streamlit* Up and Running")
st.write("1. Create a Python file (e.g., `app.py`) and import Streamlit.")
st.write("2. Use `st.title()` to set the title of your app.")
st.write("3. Add interactive components using functions like `st.write()`, `st.header()`, etc.")
st.write("4. Add tabs to organize content using `st.tabs()` and `st.tab()`.")
st.write("5. Run the app using `streamlit run app.py` in your terminal.")

st.header("🐳 Steps to Run the App in *Docker* with Docker Compose")
st.write("1. **Create a Dockerfile** in the same directory as your `app.py` file. Make sure to choose a unique port other than what I have. 8000, 8001, etc.")
st.code("""
# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8501
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
""", language='dockerfile')
st.write("2. **Create a `requirements.txt` file** and list the dependencies:")
st.code("""
streamlit
pandas
numpy
""", language='plaintext')
st.write("3. **Create a `.dockerignore` file** to exclude unnecessary files:")
st.code("""
__pycache__/
.git/
.venv/
*.pyc
""", language='plaintext')
st.write("4. **Create a `docker-compose.yml` file** to simplify running the app:")
st.code("""
version: '3'
services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
""", language='yaml')
st.write("5. **Run the app using Docker Compose:**")
st.code("""
docker compose up --build
""", language='bash')
st.write("6. **Open your browser and visit `http://localhost:8501` to see the app in action.**")

st.header("☁️ Deploying a Streamlit App with GitHub")
st.write("Using GitHub for deployment provides several advantages:")
st.write("- **Version Control**: Track changes to your code and collaborate with others.")
st.write("- **Automatic Deployment**: Deploy changes automatically when pushing updates to the repository.")
st.write("- **Streamlit Cloud Integration**: Streamlit makes it easy to deploy apps from GitHub.")

st.subheader("1️⃣ Deploying with Streamlit Cloud")
st.write("1. Push your Streamlit app to a GitHub repository.")
st.write("2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with GitHub.")
st.write("3. Click 'New app' and connect your repository.")
st.write("4. Select the branch and filename (`app.py`).")
st.write("5. Click 'Deploy' to launch your app online.")

st.header("🎉 Enjoy Exploring Streamlit with Docker!")
st.write("Feel free to modify the code, add new features, and experiment with Streamlit components!")