# GameAPI :video_game:

A hobby project RestAPI created to create an retrieve game data from a SQLite database.

## Purpose
This project was created to act as the back-end to a custom game launcher.

## Prerequisites

- Bottle
- SqlAlchemy

Full prerequisites are contained within the `requirements.txt` file.

Install them using `pip install -r requirements.txt`

## Contributing
If you find any problems, you should open a new issue.

If you can fix an issue (either one you have found or an existing one) you should open a pull request.

## Notes
Within the test files, the test to call to the `TestDelete` class is commented out. This is intentional as it other tests rely on data being present. In my tests, it seems the order was not always consistent and other tests could fail due to the `TestDelete` class being called before other tests.
