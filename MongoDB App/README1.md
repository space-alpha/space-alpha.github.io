# Girl Hacks 2023

Welcome to the "Girl Hacks 2023" project! This is a Streamlit web application that allows you to track and manage space events. You can enter event details, view them by date, and even delete events you no longer need.

## Getting Started

### Prerequisites

Before you can run this application, you need to have Python and the following Python packages installed:

- pymongo
- streamlit
- PIL (Python Imaging Library)
- base64

You can install these packages using pip:

```bash
pip install pymongo streamlit pillow
```

### Installation and Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your/repo.git
cd repo
```

2. Replace `'mongodb+srv://ps332:ps332@cluster0.z5ipz8j.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp'` with your MongoDB connection string in the code.

3. Run the Streamlit application:

```bash
streamlit run your_app.py
```

4. Access the application in your web browser at [http://localhost:8501](http://localhost:8501).

## Usage

### Event Entry

On the left side of the application, you can enter event details. Fill in the event title and select a date for the event. Then, click the right arrow button (→) to add the event to the list.

### Date View

In the Date section, you can view the events sorted by date. The date is displayed in a stylish header.

### Event Title View

In the Event Title section, you can see the titles of the events in a stylish header.

### Event Deletion

In the Delete section, you can remove events that you no longer need by clicking the trash can (🗑) icon next to the event. This will delete the event from the list.

## Customization

You can customize the appearance and behavior of this application by modifying the code as needed. Feel free to change the colors, styles, or add more features to suit your requirements.

## Credits

This project was created by [Your Name] and is inspired by [Source of Inspiration]. It is made possible by the awesome Streamlit and MongoDB community.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.