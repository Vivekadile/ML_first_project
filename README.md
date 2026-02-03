# end to end ml project hai bhaiya pehla wala
### finally aaj hua yr MLFLoW ho gaya aaj

import dagshub
dagshub.init(repo_owner='Vivekadile', repo_name='ML_first_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)