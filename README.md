# Productificator

This project aggregates information from several external APIs, including Notion, Weather, and Google Calendar,
to display in a minimalist dashboard.

# Running the project in production

## Requirements

- Docker
- API keys for Notion, Weather API, and Google Calendar.

## Instructions

1. Clone the repository.
2. Build the Docker image: `docker build -t dashboard-api`.
3. Run the Docker container: `docker run -p 5000:5000 dashboard-api`.
4. Open your browser to `http://localhost:5000` to view the dashboard.

## Environment Variables

You need to provide the following environment variables:

- `NOTION_API_TOKEN`: Your Notion API key.
- `WEATHER_API_KEY`: Your Weather API key.
- `GOOGLE_CALENDAR_CREDENTIALS`: Your Google Calendar credentials.

You can set these when running the Docker container with the `-e` option,
e.g., `-e NOTION_API_TOKEN=my_NOTION_API_TOKEN`.

# Running the project in development

## Requirements

- Python `> 3.11`
- API keys for Notion, Weather API, and Google Calendar.

## Instructions

1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv`.
3. Activate the virtual environment: `source venv/bin/activate`.
4. Install the dependencies: `pip install -r requirements.txt` and `pip install -r requirements-dev.txt`.
5. Set the environment variables in a `.env` file in the root directory of the project.


## Contributing

Feel free to open issues or PRs if you find any problems or have suggestions for improvements.

