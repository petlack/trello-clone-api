# Trello clone API

API for simple Trello clone with in-memory database, supports AWS Lambda. Example:  [trello-clone](https://github.com/petlack/trello-clone)

## Features
- ⚙ Python, [Ariadne](https://ariadnegraphql.org/), [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- 📝 GraphQL
- 📚 In-Memory database
- 🔓 CORS enabled
- 🌎 AWS Lambda supported

[DEMO](https://c1p7mwemn6.execute-api.us-east-1.amazonaws.com/graphql)

## Install
```bash
git clone git@github.com:petlack/trello-clone-api.git
cd trello-clone-api
pip install -r requirements.txt
```

## Development
```bash
./bin/run.sh
```

## Deploy to AWS Lambda
Assuming the Lambda function & ECR repository is already created, following secrets and variables are needed for [Github Action](https://github.com/petlack/trello-clone-api/blob/main/.github/workflows/deploy.yml).

### Secrets
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

### Variables
- `AWS_FUNCTION_NAME`
- `AWS_REGION`
- `AWS_ECR_REPOSITORY_NAME`