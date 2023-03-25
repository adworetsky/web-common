# Gratton Lab Website

This site is currently hosted at [https://psy.fsu.edu/grattonlab/](https://psy.fsu.edu/grattonlab/).

The docker image can be found on [Docker Hub](https://hub.docker.com/repository/docker/caterinagratton/gratton-lab-website).

## Dependencies

See requirements.txt. If you are using the docker image, the only dependency
needed is `Docker`.

## Folder Structure and Files

The code in this repository uses the [django](https://www.djangoproject.com/) framework.
Please read the django documentation for a better overview.

`/labsite`: Contains the main django project  
`/common`: Application for the lab website

Within the `common` application, the following files are of interest:

* `admin.py`: contains the definitions for each model in the admin panel
* `models.py`: definitions for each data model
* `urls.py`: urls for each viewport
* `views.py`: defines views for each webpage

The `templates` folder in the `common` application contains the html files for each page.

## Admin Panel

Everyday changes to the site can be made through the admin panel,
which can be accessed from [https://psy.fsu.edu/grattonlab/@dmin](https://psy.fsu.edu/grattonlab/@dmin). This will allow you to add news posts, edit the lab members, or add new publications.

For access, you will need another site administrator to make an account
for you. Once you have an account, you can login at the link above.

## Running the Site

The Gratton Lab Website is currently hosted on the FSU server, where an
Apache webserver redirects to a dockerized django application running on
port 8000:

```mermaid
flowchart LR
    A[User Web Request] <--> B[Apache WebServer]
    B<-->C[Docker]
    C[Docker] <--> D[Gunicorn/Django]
    C[Docker] <--> E[Postgres Database]
```

The Apache webserver has been setup by Jason Ketterer and should not need to be 
modified. Please contact him for assistance if you think there issues with it 
(modifying the Apache configuration requires root privileges).

The dockerized django application is deployed via `docker-compose`. For
example:

```bash
# note you must be in the root of the repo when executing these commands
# the repo can be found at /home/www/sites/grattonlab/web-common

# the up command will start the website, adding -d with run it in the
# background
docker-compose up -d
```

The `docker-compose` configuration can be found at `compose.yaml` in the root
of this repo.

After starting the image, the dockerized application is designed to
auto-restart automatically on any crashes or a system reboot.

To stop the dockerized application, use the `docker-compose down` command:

```bash
# this also must be executed in the root of the repo
docker-compose down
```

> **__NOTE:__** At the moment, the current server the gratton lab website 
> is hosted on has some issues when trying to tear down docker containers. 
> You should use `kill_script.sh` located in the root of this repo as an
> alternative to `docker-compose down`. This script can take up to two 
> minutes to complete, but will ensure that the docker containers are
> properly stopped.
>
> This note should be removed if the issue is fixed.

## Updating the Site

To update the site, you must rebuild the docker image, push the image
to the dockerhub repo @ caterinagratton/gratton-lab-website:latest, and
then restart the `docker-compose` application on the server after removing
the existing image. Below is an example of how to do this (note that this
assumes you have docker installed on your local machine):

```bash
# let's say you've made some changes to the code
# now we want to rebuild the docker image

# first, on our local machine (not the server), clear out any existing
# gratton-lab-website images
docker rmi caterinagratton/gratton-lab-website

# next execute the build command
# old way
docker build -t caterinagratton/gratton-lab-website .
# or
# new preferred way (but requires newer docker versions installed)
docker buildx build -t caterinagratton/gratton-lab-website .

# once the image has been built, we can push it to the dockerhub repo
docker push caterinagratton/gratton-lab-website

# now we want to ssh into the https://psy.fsu.edu (Jason Ketterer for
# the IP address and login credentials)
ssh <username>@<ip address for https://psy.fsu.edu>

# once we've ssh'd into the server, go to the root of the repo on the server
cd /home/www/sites/grattonlab/web-common

# if you made any git commits to the repo, you should pull them down
# at this step
# this only really matters if you've somehow modified compose.yaml
git pull

# now we want to stop the existing docker-compose application
docker-compose down
# or if the above bug is still present, use kill_script.sh
./kill_script.sh

# once the application has been stopped, we can remove the existing
# docker image
docker rmi caterinagratton/gratton-lab-website

# now we can start the docker-compose application again
# this will auto re-pull the image from dockerhub since we removed the
# local image above
docker-compose up -d
```

> **__NOTE:__** Please note that changing files on the server will NOT update
> the site. Since the site is deployed via docker, the only way to update it
> is to rebuild the docker image and push/pull it to/from the dockerhub repo.
>
> The only exception to this is if you are modifying the `compose.yaml` file.
> In this case, you can simply pull the changes from git and restart the
> docker-compose application. In fact, the only file read on the server is
> `compose.yaml`, all other files are ignored.

## Local Testing

Sometimes it is useful to test the site locally before pushing any changes.
There are two ways to test the site locally:

1. Using django's built-in development server. This can be started through
the `manage.py` script. For example:

```bash
# from the root of the repo
python manage.py migrate  # you only ever need to run this once (initializes the database)
python manage.py runserver
```
This method is useful for testing the site locally, but does not run gunicorn or
the postgres database, so is not a perfect replication of the production environment the site is hosted on.

2. Using docker-compose. This is the preferred method for testing the site locally.
Before running the site using this method, you want to modify the `compose.yaml` 
file, so that `USE_SUBPATH` is set to `FALSE`. This will turn off the configuration
that allows the site to be hosted on a subpath (e.g. https://psy.fsu.edu/grattonlab/):

```yaml
services:
  gunicorn:
    image: caterinagratton/gratton-lab-website
    depends_on:
      - postgres
    ports:
      - "8000:8000"
    networks:
      - main
    environment:
      - DATABASE_URL=postgres://ajxfstclzxhdss:postgres@postgres:5432/d7i8e5thopmkvh
      - PRODUCTION=TRUE  # leave this TRUE, this sets the database to use postgres
      - DEBUG=TRUE  # you probably want this set to TRUE during testing
      - USE_SUBPATH=FALSE  # this line should be set from TRUE --> FALSE
    secrets:
      - dropbox
    restart: always
```

> **__NOTE:__** After modifying the `compose.yaml` file, take care NOT to commit
> the changes to git. You can break the site if you leave the testing configuration
> options on in the file.

Then, after the compose file is modified, you can run the site locally using:

```bash
# from the root of the repo
docker-compose up

# and to pause the site, use ctrl+c to stop the containers
# to actually remove the containers, use
docker-compose down
```
