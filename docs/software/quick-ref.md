# Software Quick References

## Docker

## Kubernetes
### Overview
![Kubernetes Architecture](/img/components-of-kubernetes.png)

- Kubernetes master: three processes running on a single node:
    - `kube-api-server`
    - `kube-controller-manager`
    - `kube-scheduler`
- Kubernetes nodes: worker machines that can run containerized applications.
    - `kubelet`: communicates with the master
    - `kube-proxy`
- `etcd`: consistent and highly-available key value store used as Kubernetes' backing store for all cluster data

### Kubernetes object
Kubernetes object are persistent entities in the Kubernetes system to represent the state of your cluster.

#### Pod
- A basic execution unit of a Kubernetes application.
- The smallest the simplest unit in the Kubernetes object model that you can create or deploy.


#### Service

## Helm
Helm is a package manager for Kubernetes
### Concepts
- A **Chart** is a Helm package. It contains all of the resource definitions necessary to run an application inside a Kubernetes cluster.
- A **Repository** is the place where charts can be collected and shared.
- A **Release** is an instance of a chart running in a Kubernetes cluster.

## AWS
### AWS CloudFormation
- Templates: JSON or YAML files that will be used as the blueprints for building AWS resources.
- Stack: a single unit that you manage related resources in AWS CloudFormation
- Change set: a summary of changes to a stack.

#### AWS CloudFormation cheat sheet
##### Stack
- List names of activate stacks
```
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE ROLLBACK_COMPLETE UPDATE_ROLLBACK_COMPLETE | jq -r '.StackSummaries | .[] | .StackName'
```
- Get the template used to create a stack
```
aws cloudformation get-template --stack-name  <stack-name> | jq -r '.TemplateBody'
```



## Google Cloud Platform

## Postgres
- Role: a role is an entity that can own database objects and have database privileges; a role can be considered a "user", a "group", or both depending on how it is used

### Postgres cheat sheet
#### Connection
- Connect to database in terminal: `PGPASSWORD=*** psql "host=*** user=*** dbname=postgres sslmode=require"`
- `\conninfo`: Print out connection information

#### Databases
- `\l`: List all databases
- `\c <db_name>`: Connect to a given database

#### Tables
- `\dt`: List all tables.
- `\d+ <table_name>`: Get detailed information of a table.



## Jq
### Dealing with array
Suppose we have json data:
```json
[{
	"key": 1,
	"value": "one"
}, {
	"key": 2,
	"value": "two"
}]
```

Description | Filter | Result
:------------|:--------|:----------
Convert it to an object or dict | `map({(.key|tostring): .value}) | add` | `{"1": "one","2": "two"}`
Select a subset | `map(select(.key==1))` | `[{"key": 1, "value": "one"}]`
