My implementation of a images to pdf app using Flask(python).

### Steps to reproduce environment

Due to memory caps of free hosting it might be a good idea to reproduce the
environment locally. To do that, follow the steps.

Make sure python3, pip3, and pipenv are installed !!

- Git clone repo.
- Navigate to project directory
- Run `$ pipenv shell` to activate virtaul environment.
- Then to install all dependencies execute `$ pipenv install`
- Finally to run the app enter ` $ gunicorn run:app --timeout 300 ` 
