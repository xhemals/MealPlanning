# [Meal Planning](MealPlanning/views.py)

This is a Django application that allows users to create a meal plan and view events on a calendar. The app has three main views:

- `index`: The main landing page, which displays a form for users to input a start date for their meal plan.
- `planning`: A form for users to input details about a specific meal, including the date and who will be eating. This view also includes a `MealView` class-based view that displays a detailed page for a specific meal, using the `meal_detail.html` template.
- `done`: A page that is displayed when the meal planning process is complete.

The `mealPersons` dictionary maps integers to names, and the `suffix` function is used to add the appropriate suffix to a day of the month (e.g. 1st, 2nd, 3rd). The `gCalendar` module is used for interacting with a calendar API, and has functions for creating and viewing events, finding the furthest event in the future, and adding events to the calendar.

The app also includes a `Meal` model that stores information about a specific meal, including the date, meal type, and who will be eating.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following software to run this project:

- Python 3
- Django
- The dependencies listed in the `requirements.txt` file

### Installing

Follow these steps to install the project:

1. Clone the repository: `git clone https://github.com/xhemals/MealPlanning.git`
2. Navigate to the project directory: `cd meal-planning`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the Django migrations: `python manage.py migrate`
5. Run the Django server: `python manage.py runserver`

# [Google Calendar API](MealPlanning/gCalendar.py)

This is a Python script that uses the Google Calendar API to create and view events on a calendar. The script has several functions:

- `creds`: Handles authentication and authorization for the Google Calendar API.
- `runCalendar`: Creates a new event on the calendar with the specified day, meal, and who is eating.
- `viewEvent`: Retrieves and displays a list of events from the calendar.
- `furthestEvent`: Finds the furthest event in the future.

## Prerequisites

You will need the following software to run this script:

- Python 2 or 3
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client

## Setting up the Google Calendar API

Follow these steps to set up the Google Calendar API:

1. Go to the [Google API Console](https://console.developers.google.com/apis/).
2. Click the project drop-down and select or create the project that you want to use for the API.
3. Click the hamburger menu and select APIs & Services > Library.
4. Search for "Calendar API" and click on the result.
5. Click the Enable button to enable the Calendar API.
6. Click the Create credentials button and follow the prompts to set up the necessary credentials.
7. Download the credentials.json file and save it in the `creds` directory.

## Contributing

I welcome contributions to this project. If you have an idea for a new feature or have found a bug, please open an issue on the [GitHub repository](https://github.com/user/meal-planning).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
