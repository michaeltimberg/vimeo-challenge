# Vimeo

### Assessment

## Contents

 - [**Statement**](#statement)
 - [**Assumptions**](#assumptions)
 - [**Prerequisites**](#prerequisites)
 - [**Setup**](#setup)
 - [**Usage**](#usage)
 - [**Testing**](#testing)

## Statement

### Background

You have 10GB of text logs. Each log line corresponds to a single HTTP response
from web frontend. You goal is to write a simple, reusable tool that returns the
percentage of responses that were HTTP 5xx errors, broken down by domain, for a
given timeframe.

Output should look something like this:

```shell script
Between time XXXXXXXXXX and time YYYYYYYYYY:
vimeo.com returned 2.15% 5xx errors
player.vimeo.com returned 3.01% 5xx errors
api.vimeo.com returned 0.01% errors
```

The input to your tool will be a start time, an end time, and a list of files.
You should consider lines at or after the start time, and strictly before the
end time. You may choose to take input in whatever format you like.

Each log line looks like this (this is a single line, which may be wrapped on
your screen):

```shell script
1493969101.644 | https | vimeo.com | GET | 404 | 1493969101583195,1493969101635320, | IAD |  | 10.10.3.59 | 0.009
```

The fields are:

 1. Time of response (seconds since epoch, as a float)
 2. Response scheme ("http" or "https")
 3. HTTP Host (domain)
 4. HTTP request method
 5. HTTP status
 6. CDN information
 7. CDN ingress point
 8. Remote address metadata
 9. Remote address
10. Time taken by request in seconds

Each field is separated by " | " (a pipe enclosed by spaces). The fields you
care about are (1), (3), and (5).

`log_sample.txt` contains a small sample of log entries.

We wrote a sample solution in about 1 hour, and we're expecting something of a
similar level of complexity -- we don't need something complex, and it doesn't
need to solve use cases other than the one we're describing.

### Our Questions

 1. Please write a program to solve the problem above, in Python, Ruby, or Go.
    (If you don't know any of these languages, talk to us and we'll figure
    something out.)
 2. Please write a README file including the following information:
    1. A sample invocation of your program and its output.
    2. A list of any external dependencies of your program, and any applicable
       installation instructions.
    3. A list of any assumptions you made in your solution.

Thanks for taking the time to complete this exercise!

<3, Vimeo

## Assumptions

The script (`./error_percentage/error_percentage.py`) was written under the
following assumptions:

 - Any log file fed into it would have the same format as `./test/log_sample.txt`
 - The script could be utilized on the smallest virtual machines AWS or GCP has
   to offer: single threaded, with low memory requirements
 - The script is able to be run in a VM or Docker image that is Python 3.8
   capable
 - 

 ## Prerequisites

  - Python 3.8.x (found [here][1])

## Setup

1. Install `virtualenv` via `pip`:

    ```shell script
    python \
     -m pip install \
     --user \
     virtualenv
    ```

 2. Create a new virtual environment:

    ```shell script
    virtualenv \
     --python=$(which python3.8) \
     venv
    ```

 3. Activate the virtual environment:

    ```shell script
    source ./venv/bin/activate
    ```

 4. Install required packages:

    ```shell script
    pip install
     --no-cache-dir \
     --requirement=requirements.txt
    ```

 5. Install current dir. as package:

    ```shell script
    pip install . --log LOG_FILE
    ```

 6. Check to make sure everything worked properly:

    ```shell script
    python ./error_percentage/error_percentage.py --help

    #=>

    Usage: error_percentage.py [OPTIONS]
    . . .
    ```

## Usage

This script can be ran directly:

```shell script
python ./etl/extract_transform_load.py
```

## Testing

Run `pytest` from the base dir.:

```shell script
pytest

#=>

=== test session starts ===
. . .
```

You can exit after the first failed test by using the `--exitfirst` flag:

```shell script
pytest \
 --exitfirst

#=>

=== test session starts ===
. . .
```

You can also run without executing the pre-script functions found within
`./test/conftest.py` with the `--noconftest` flag:

```shell script
pytest \
 --noconftest

#=>

=== test session starts ===
. . .
```

[1]: https://www.python.org/downloads