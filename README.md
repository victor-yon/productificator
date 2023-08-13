# Productificator

This project aggregates information from several external APIs, including Notion, Weather, and Google Calendar, to
display in a dashboard.

## Requirements

- Docker
- API keys for Notion, Weather API, and Google Calendar credentials

## Running the Project

1. Clone the repository.
2. Build the Docker image: `docker build -t dashboard-api .`
3. Run the Docker container: `docker run -p 5000:5000 dashboard-api`
4. Open your browser to `http://localhost:5000` to view the dashboard.

## Environment Variables

You need to provide the following environment variables:

- `NOTION_API_KEY`: Your Notion API key.
- `WEATHER_API_KEY`: Your Weather API key.
- `GOOGLE_CALENDAR_CREDENTIALS`: Your Google Calendar credentials.

You can set these when running the Docker container with the `-e` option, e.g., `-e NOTION_API_KEY=my_notion_api_key`.

## Contributing

Feel free to open issues or PRs if you find any problems or have suggestions for improvements.

