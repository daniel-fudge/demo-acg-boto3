# demo-acg-boto3
Demo repo for experimenting with boto3

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty.py uses the configuration file created by the AWS cli. e.g..

`aws configure --profile shotty`

## Running

`pipenv shell`
`python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command* is `instances`, `volumes` or `snapshots`   
*subcommand* depends on command
*project* is optional
