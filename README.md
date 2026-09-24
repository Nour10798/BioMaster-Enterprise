# BioMaster-Enterprise
# BioMaster Enterprise

BioMaster Enterprise is an end-to-end bioinformatics and cheminformatics pipeline. It transitions analytical scripts into a production-ready system. The platform handles epidemiological analysis, genomic clustering, machine learning predictions, and high-throughput virtual screening, all served through a secure API.

## System Architecture

The project is structured as a centralized backend service. Instead of standalone Jupyter notebooks, the core analytical engines are wrapped in a FastAPI application, backed by a SQLite database, and containerized for deployment.

## Project Structure

BioMaster-Enterprise/
|-- app.py
|-- bio_predictions.db
|-- protein_viewer.html
|-- requirements.txt
|-- Dockerfile
|-- docker-compose.yml
|-- README.md

## Installation and Execution

The recommended approach is using Docker to avoid environment conflicts.

git clone https://github.com/username/BioMaster-Enterprise.git
cd BioMaster-Enterprise
docker-compose up --build -d

The API server will be available at http://localhost:8000.

To run locally without Docker:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000

## API Reference

Authentication is enforced via headers. Include the following in all requests:
X-API-Key: sk-biomaster-prod-2026

GET /drug_screening_results
Returns the structured results of the Lipinski's Rule of Five evaluations directly from the database.

POST /docking_simulation
Accepts spatial coordinates and chemical structures to execute molecular docking simulations.

Payload format:
{
  "ligand_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
  "receptor_pdbqt_path": "/data/receptors/1hsg.pdbqt",
  "center_x": 15.2,
  "center_y": 20.5,
  "center_z": 10.1
}

## Structural Visualization

The spatial rendering of proteins and active binding pockets is handled client-side. Open protein_viewer.html in any standard web browser to view the 3D molecular structures generated via py3Dmol.

## License

This project is licensed under the MIT License.
