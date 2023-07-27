# Python Challenge

Front-end link: [https://github.com/rafaellevissa/company-reactjs](https://github.com/rafaellevissa/company-reactjs)

## 👨🏻‍🔧 Installation

First things first, make sure you have `python3`, `pip3`, and `venv` installed.

Activate the virtual environment by running the following command in the root folder of the project:

```
source env/bin/activate
```

Next, install the required dependencies:

```
pip3 install -r requirements.txt
```

Set a few environment variables:

```
export FLASK_ENV=development
export FLASK_APP=server.py
```

We're almost done! Now, run the migrations:

```
flask db upgrade
```

After that, run the following code. If everything went right, you are ready to go:

```
flask run
```

### Install with Docker

Alternatively, you can run the project with Docker. Make sure the `.env` file is correctly set up, and then build a Docker image using the following command:

```
docker compose build
```

Once the image is built, start the container:

```
docker compose up -d
```

After the container is up, create the migrations with the following command:

```
docker compose exec api flask db upgrade
```

That's all you need 🎉! Now you are ready to use the Python Challenge!