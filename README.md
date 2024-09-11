
# SOCA Analysis

This repo is an implementation of the SOCA (Strengths, Opportunities, Challenges, Action Plan) analysis for JEE students.



# Usage
The analysis can be run locally as well as on kaggle
## Running Locally

clone the repo
```bash
git clone https://github.com/SumitTahiliani/soca-analysis.git
```
Set up and activate virtual environment
```bash
pip install venv

cd soca-analysis

python3 -m venv .venv
source .venv/bin/activate
```

Installing the required dependencies:
```bash
pip install -r requirements.txt
```

Running the analysis:
```bash
python3 main.py
```

## Known Issues
- After answering all the questions, the script might appear stuck while the script ```ai_model.py``` downloads the Qwen model in the background.
- To avoid this, run the command ```python3 ai_model.py``` first to download the model, then follow the usage instructions for running locally.
## Running on Kaggle

Access the notebook 
[here](https://www.kaggle.com/code/sumittahiliani/studiez-2)

Select ```Copy and Edit``` option on the top right

Follow instructions given in the first markdown cell of the notebook to run the script on kaggle.

