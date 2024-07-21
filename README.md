# Mediaflex DB PLSQL Jupyter Notebook

- Mediaflex DB Data Dictionary
- Sample records
- Sample queries

## Develolpment Configuration Setup

### Required Software

- VSC
- Python 3.12+
- 'Basic Package' Oracle Client
    > Install `Basic Package` Oracle Client [Oracle Instant Client Downloads page](https://www.oracle.com/database/technologies/instant-client/downloads.html)
    > Unzip and place it under C:\oracleclient\instantclient_19_23

### Dedicated Python Enviroment

```shell
conda create --name nfsa-env python=3.12.3
conda init
conda activate nfsa-env

# conda env list 
# conda remove --name nfsa-env --all
# conda update conda
# conda config --set solver classic
```

To delete and recreate a new enviroment

```shell
conda deactivate
conda env list 
conda remove --name nfsa-env --all
conda create --name nfsa-env python=3.12.3
conda init
conda activate nfsa-env

conda install --name nfsa-env --update-deps --force-reinstall

```

### Install `pip-tools` tool

```pip install pip-tools```

### Python Library Dependency Management

1. Compile requirements.in to requirements-full.txt

    ```pip-compile --output-file=requirements-full.txt requirements.in```

    ![](https://i.imgur.com/AGv3MWT.png)

2. Lock working library version (always)

    ```pip-compile --output-file requirements.lock```

3. Run python script to clean up genereated `requirements.txt`

    ```python src/util/generate_requirements.py```

4. Compare, update `requirements-ddev.txt` with `requirements-full.txt` to reflect the libary version change and update `requirements.txt`

    ![Compare library version change](https://i.imgur.com/FU7v2z7.png)

5. Install Dependencies

    ```pip install -r requirements.txt```

    ```pip install -r requirements.in```

6. Update `requirements-full.txt` from `requirements.lock`
