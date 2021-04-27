Flasky
======

A simple Flask app to play around with docker and kubernetes.

## Supported Endpoints
```
GET /
Returns "Hello, World!" and a 200 HTTP Code

GET /healthz
Returns "OK" and a 200 HTTP Code

GET /unhealthz
Returns "NOK!" and a 500 HTTP Code
```

## Usage

```
docker build . -t flasky
docker run -p 5000:5000 flasky
```
