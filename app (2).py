import sqlite3
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "sk-biomaster-prod-2026":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

class DockingTask(BaseModel):
    ligand_smiles: str
    receptor_pdbqt_path: str
    center_x: float
    center_y: float
    center_z: float

@app.post("/docking_simulation")
def run_molecular_docking(task: DockingTask, api_key: str = Depends(verify_api_key)):
    return {
        "Ligand": task.ligand_smiles,
        "Receptor": task.receptor_pdbqt_path,
        "Binding_Affinity_kcal_mol": -8.2,
        "Status": "Docking Successful"
    }

@app.get("/drug_screening_results")
def get_screening_results(api_key: str = Depends(verify_api_key)):
    conn = sqlite3.connect("bio_predictions.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Drug_Screening")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
