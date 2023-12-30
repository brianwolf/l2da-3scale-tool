# 3scale-tool

> Herramienta para desplegar yamls en 3scale similar a como hace argocd

## Requerimientos

* python 3.11

## Carga de variables de ambiente

### Bash

```bash
export REPO_PATH=/home/brian/workspace/lasegunda/l2da-app/
export TOKEN=token
export URL_BASE=url
export APP_ENV=desa
```

### VScode

```json
"env": {
    "REPO_PATH": "/home/brian/workspace/lasegunda/l2da-app/",
    "TOKEN": "token",
    "URL_BASE": "url",
    "APP_ENV": "desa"
}
```

## Uso

```bash
python3 app.py
```
