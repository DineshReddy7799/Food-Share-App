Food Share App
A web-based platform for sharing, listing, and discovering food items. Users can register, log in, and add food items with location details that are displayed on an interactive map.

Features
User Authentication: Secure registration, login, and logout functionalities.
Add Food Items: Users can add food items with details like name, description, and location.
Interactive Map: Food items are displayed on a map using Leaflet.js.
Search Functionality: Search for food items based on specific criteria.
Responsive Design: Works seamlessly on desktop and mobile devices.
Technologies Used
Backend:
Django (Python framework)
SQLite (default database)
Frontend:
HTML, CSS, JavaScript
Leaflet.js (for interactive map)
Tools:
Git (version control)
Django’s built-in authentication
Getting Started
Prerequisites
Python 3.8+ installed
Git installed
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/DineshReddy7799/Food-Share-App.git
Navigate to the project directory:

bash
Copy code
cd Food-Share-App
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/.

Usage
Register: Create a user account.
Login: Access your account.
Add Food Items: Share food items with descriptions and locations.
Explore: View available food items on the interactive map.
Contributing
Contributions are welcome! Follow these steps:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Description of changes"
Push the branch:
bash
Copy code
git push origin feature-name
Submit a Pull Request for review.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or issues, feel free to reach out:

Name: Dinesh Reddy
GitHub: DineshReddy7799
Email: dineshreddy3450@gmail.com
