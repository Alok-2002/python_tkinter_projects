# Student Management System with MySQL Database

The Student Management System (SMS) is a GUI application created with Python and tkinter. It is designed to manage student data for a school or university. This version of the system utilizes a MySQL database to store and retrieve student information, such as names, addresses, contact information, and academic records.

## Features

- Add new students to the system
- Edit existing student information
- Delete students from the system
- View a list of all students in the system
- Search for a specific student by name or ID
- Export student data to a CSV file

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`
3. Create a MySQL database and import the `sms.sql` file to create the necessary tables.
4. Modify the `config.ini` file to include your MySQL database credentials.
5. Run the `student.py` file to launch the application.

## Usage

Upon launching the application, you will be presented with a GUI window that displays a list of all students in the system. From there, you can perform various actions on the student data using the buttons and fields provided.

### Adding a new student

To add a new student, click the "Add Student" button and fill out the required fields in the form that appears. Once you have entered all the necessary information, click "Save" to add the new student to the system.

### Editing a student

To edit an existing student's information, select the student from the list and click the "Edit Student" button. This will bring up the same form used for adding a new student, but with the fields pre-filled with the student's current information. Make any necessary changes and click "Save" to update the student's data.

### Deleting a student

To delete a student from the system, select the student from the list and click the "Delete Student" button. You will be prompted to confirm the deletion before the student is removed from the system.

### Searching for a student

To search for a specific student, enter the student's name or ID in the search field at the top of the window and click "Search". The list of students will be filtered to show only those that match your search criteria.

### Exporting student data

To export the student data to a CSV file, click the "Export to CSV" button. The file will be saved in the same directory as the application.

## Contributing

If you find a bug or would like to suggest a new feature, please open an issue or submit a pull request on GitHub. Contributions are always welcome!
