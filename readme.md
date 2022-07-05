## GroundX AWS Lambda
---
### Lambda return form protocol
```json
{
  "code": "200",
  "message": "success message"
}
//
{
  "code": "500",
  "message": "fail message"
}
```

### Create Lambda on local Mac
> Install Mac SAM CLI
```bash
brew tap aws/tap
brew install aws-sam-cli
```
> Create team directory
* DevOps already have `devops` subdirectory.
> Add your function into team directory as a module.
* Add a python file into under team directory. For example, new file name would be `devops/test.py`.
* Edit `__init__.py` to make sure your new file read as module for local testing.
* Call your module from `main.py`

> Local invoking with SAM
* Add your module defined in `template.yaml`
* If your module(lambda) needs specific input values, define `events.json` file. Take a look `events/events.json`
* Run SAM CLI
```
sam local invoke CFInvalidationFunction -e events/events.json
```
* Don't forget login OKTA

> Deploy lambda application
* Update or create your `samconfig.toml`
  + Please check `samconfig.toml.sample`
* Run SAM CLI
```bash
sam deploy # If you have samconfig.toml
sma deploy --guided # If you don't have samconfig.toml -> This will generate samconfig.toml

```
