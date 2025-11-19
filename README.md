# Ministerio de Relaciones Exteriores

## Requisitos

- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Azure Developer CLI](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd?tabs=winget-windows%2Cbrew-mac%2Cscript-linux&pivots=os-windows)
- Python 3.10 o 3.11 (Utilizar `python` en vez de `python3`. En Ubuntu,se debe ejecutar `sudo apt install python-is-python3` para vincular `python` a `python3`.)
- Node.js >=20 LTS
- [Powershell 7+ (pwsh)](https://github.com/powershell/powershell) (Sólo para windows)

## Recursos de Azure

- Grupo de recursos
- Recurso de Azure OpenAI, GPT4 y ADA
- Cuenta con rol `Microsoft.Authorization/roleAssignments/write`
- Suscripción con `Microsoft.Resources/deployments/write`
- Azure Blob Storage con ZRS???
- Azure AI Search, panel Settings/Keys, "API access control" "Both"
- Azure OpenAI {disableLocalAuth: false}

## Roles de Azure:

- Key Vault Secrets Officer
- Cognitive Services User 
- Search Index Data Contributor
- Search Service Contributor
- Cognitive Services OpenAI User

## Despliegue

1. Iniciar sesión: `azd auth login` y `az login`
2. Agregar cada variable de entorno: `azd env set {ENV_NAME} {env_value}` (Es recomendable crear grupos de recursos y el recurso de Azure OpenAI). Encaso solicite un nombre para el ambiente, escribir: `rree-chatbot-ia`.

```shell
azd env set AZURE_ENV_NAME rree-chatbot-ia
```

3. Seleccionar un intérprete de Python >= 3.10  y ejecutar: `azd up` y seleccionar zona `eastus`.

## Ejecución en local

1. Ir a la carpeta: `cd app`
2. Visualizar en local: `./start.ps1` (windows) o `./start.sh` (unix). En caso de error "permission denied" o "command not found", ejecutar `chmod +x start.sh`.
3. Ir a `http://127.0.0.1:50505`
4. `cd app/frontend` y `npm run dev` para ver cambios de frontend en `localhost:5173`
5. Ejecutar `azd deploy` desde la carpeta raíz para desplegar cambios de local a la nube.

### (Opcional) Eliminar los recursos

`azd down` para eliminar los recursos

## Indexar documentos
Se indexan los documentos de la carpeta `data`

- En el recurso "Document Intelligence", panel "Access control (IAM)", crear el rol "Cognitive Services User".
- Ejecutar `scripts/prepdocs.sh` (Mac/Linux) o `scripts/prepdocs.ps1` (Windows) desde la carpeta raiz.
  Proceso del script:

1. Si no existe todavía, crear un nuevo index en Azure AI Search.
2. Subir los PDFs a Azure Blob Storage.
3. Dividir los PDFs en chunks de texto.
4. Subir los chunks a Azure AI Search, y generar los embeddings correspondientes al texto.

### Formatos de documentos permitidos

- DOCX
- JPG
- PDF
- PNG
- PPTX
- XLSX

## Revisar configuración de recursos desplegados

1. Ir al recurso "Storage account".
2. Ir al panel "Settings"/"Configuration" y habilitar "Allow storage account key access".
3. Click en "Save".
4. Ir al panel "Data Storage"/"Containers" y crear Contenedor "uploads"
5. En el panel "Security + networking"/"Access keys" copiar "Connection string"

## Solución de problemas

- Azure CLI en proxy: https://learn.microsoft.com/es-mx/cli/azure/use-azure-cli-successfully?tabs=bash%2Cbash2#work-behind-a-proxy
- AIO: https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.aio?view=azure-python
- az login `az login use-device-code`
- Timeout: `DockerApiException: Docker API responded with status code=InternalServerError, response={"message":"Get \"https://mcr.microsoft.com/v2/\": net/http: TLS handshake timeout"}` Escalar App Service Plan y reiniciar Web App.

***

## Configuración de recursos de Azure

### Azure AI Search

Crear con JSON:

```JSON
{
  "@odata.context": "https://srch-rree-chat-ia.search.windows.net/$metadata#indexes/$entity",
  "@odata.etag": "\"0x8DD0260C1B113C9\"",
  "name": "rree-chat-ia-index-prod",
  "defaultScoringProfile": null,
  "fields": [
    {
      "name": "id",
      "type": "Edm.String",
      "searchable": false,
      "filterable": false,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": false,
      "key": true,
      "indexAnalyzer": null,
      "searchAnalyzer": null,
      "analyzer": null,
      "normalizer": null,
      "dimensions": null,
      "vectorSearchProfile": null,
      "vectorEncoding": null,
      "synonymMaps": []
    },
    {
      "name": "content",
      "type": "Edm.String",
      "searchable": true,
      "filterable": false,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": false,
      "key": false,
      "indexAnalyzer": null,
      "searchAnalyzer": null,
      "analyzer": null,
      "normalizer": null,
      "dimensions": null,
      "vectorSearchProfile": null,
      "vectorEncoding": null,
      "synonymMaps": []
    },
    {
      "name": "embedding",
      "type": "Collection(Edm.Single)",
      "searchable": true,
      "filterable": false,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": false,
      "key": false,
      "indexAnalyzer": null,
      "searchAnalyzer": null,
      "analyzer": null,
      "normalizer": null,
      "dimensions": 1536,
      "vectorSearchProfile": "embedding_config",
      "vectorEncoding": null,
      "synonymMaps": []
    },
    {
      "name": "category",
      "type": "Edm.String",
      "searchable": false,
      "filterable": true,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": true,
      "key": false,
      "indexAnalyzer": null,
      "searchAnalyzer": null,
      "analyzer": null,
      "normalizer": null,
      "dimensions": null,
      "vectorSearchProfile": null,
      "vectorEncoding": null,
      "synonymMaps": []
    },
    {
      "name": "sourcepage",
      "type": "Edm.String",
      "searchable": false,
      "filterable": true,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": true,
      "key": false,
      "indexAnalyzer": null,
      "searchAnalyzer": null,
      "analyzer": null,
      "normalizer": null,
      "dimensions": null,
      "vectorSearchProfile": null,
      "vectorEncoding": null,
      "synonymMaps": []
    },
    {
      "name": "sourcefile",
      "type": "Edm.String",
      "searchable": false,
      "filterable": true,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": true,
      "key": false,
      "indexAnalyzer": null,
      "searchAnalyzer": null,
      "analyzer": null,
      "normalizer": null,
      "dimensions": null,
      "vectorSearchProfile": null,
      "vectorEncoding": null,
      "synonymMaps": []
    },
    {
      "name": "storageUrl",
      "type": "Edm.String",
      "searchable": false,
      "filterable": true,
      "retrievable": true,
      "stored": true,
      "sortable": false,
      "facetable": false,
      "key": false,
      "indexAnalyzer": null,
      "searchAnalyzer": null,
      "analyzer": null,
      "normalizer": null,
      "dimensions": null,
      "vectorSearchProfile": null,
      "vectorEncoding": null,
      "synonymMaps": []
    }
  ],
  "scoringProfiles": [],
  "corsOptions": null,
  "suggesters": [],
  "analyzers": [],
  "normalizers": [],
  "tokenizers": [],
  "tokenFilters": [],
  "charFilters": [],
  "encryptionKey": null,
  "similarity": {
    "@odata.type": "#Microsoft.Azure.Search.BM25Similarity",
    "k1": null,
    "b": null
  },
  "semantic": {
    "defaultConfiguration": null,
    "configurations": [
      {
        "name": "default",
        "prioritizedFields": {
          "titleField": null,
          "prioritizedContentFields": [
            {
              "fieldName": "content"
            }
          ],
          "prioritizedKeywordsFields": []
        }
      }
    ]
  },
  "vectorSearch": {
    "algorithms": [
      {
        "name": "hnsw_config",
        "kind": "hnsw",
        "hnswParameters": {
          "metric": "cosine",
          "m": 4,
          "efConstruction": 400,
          "efSearch": 500
        },
        "exhaustiveKnnParameters": null
      }
    ],
    "profiles": [
      {
        "name": "embedding_config",
        "algorithm": "hnsw_config",
        "vectorizer": null,
        "compression": null
      }
    ],
    "vectorizers": [
      {
        "name": "rree-chat-ia-index-dev-vectorizer",
        "kind": "azureOpenAI",
        "azureOpenAIParameters": {
          "resourceUri": "https://oai-rree-chat-ia.openai.azure.com",
          "deploymentId": "ada-002",
          "apiKey": null,
          "modelName": "text-embedding-ada-002",
          "authIdentity": null
        },
        "customWebApiParameters": null,
        "aiServicesVisionParameters": null,
        "amlParameters": null
      }
    ],
    "compressions": []
  }
}
```
