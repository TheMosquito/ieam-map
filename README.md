# ieam-map

Extremely simple HTTP server (written in Python) that responds on port 80 with a map showing the IP geolocation of the server where it is being run. E.g.:

![example-image](https://raw.githubusercontent.com/TheMosquito/ieam-map/master/example.png)

You need a *free* API key from [https://ipgeolocation.io/](https://ipgeolocation.io/) to use this.

Usage:

First get the API key and edit it into ieam-map.py.

```
make build
make run
```

The connect your browser to the machine where this is running, and see the map.

```
make test
make stop
```

