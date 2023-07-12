# Social App Python

This project, named "Social App Python," focuses on building a social application using Python and Jupyter Notebook as the development platform. The application connects to a MySQL database using an SQL connector and provides functionality for various CRUD (Create, Read, Update, Delete) operations such as adding posts, deleting posts, updating posts, and viewing all posts. Additionally, SQL Workbench is used for query practice and testing.

## Project Structure

The project directory is structured as follows:

```
social-app-python/
    ├── notebooks/
    │   └── Social_App_Python.ipynb
    ├── README.md
    └── requirements.txt
```

- `notebooks/`: This directory contains the Jupyter Notebook (`Social_App_Python.ipynb`) where the application is developed and the CRUD operations are performed.
- `README.md`: The file you are currently reading, which provides an overview of the project.
- `requirements.txt`: This file lists the required Python packages and their versions.

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python 3.x
- Jupyter Notebook
- MySQL database
- SQL Connector for Python (e.g., `mysql-connector-python`)

To install the necessary packages, use the following command:

```bash
pip install -r requirements.txt
```

## Running the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/social-app-python.git
```

2. Navigate to the project directory:

```bash
cd social-app-python
```

3. Start Jupyter Notebook:

```bash
jupyter notebook
```

4. Open the `Social_App_Python.ipynb` notebook from the `notebooks/` directory in the Jupyter Notebook interface.

5. Execute the code cells in the notebook to run the social application and perform CRUD operations.

## Database Configuration

The project assumes that you have a MySQL database set up. Make sure to configure the database connection details in the notebook (`Social_App_Python.ipynb`) before running the code.

The necessary database connection parameters include:

- Host
- Port
- Username
- Password
- Database name

Update the connection details in the notebook's code cells that interact with the database.

## CRUD Operations

The Jupyter Notebook (`Social_App_Python.ipynb`) contains code and explanations for performing the following CRUD operations:

1. **Add Post**: This operation allows users to create and add new posts to the social application. The notebook demonstrates how to collect user input, execute SQL queries to insert the post into the database, and handle exceptions.

2. **Delete Post**: Users can delete existing posts using this operation. The notebook guides you through the process of selecting the post to delete, executing the corresponding SQL query, and handling any errors that may occur.

3. **Update Post**: This operation enables users to update the content of an existing post. The notebook demonstrates how to select the post to update, collect new content from the user, execute the SQL query to update the post in the database, and handle exceptions.

4. **View All Posts**: This operation allows users to view all posts in the social application. The notebook showcases how to execute a SQL query to retrieve all posts from the database and display them in a formatted manner.

## SQL Workbench

SQL Workbench is mentioned as a tool for query practice and testing. While it is not directly used within the project, you can use SQL Workbench or any other SQL client of your choice to connect to the MySQL database and execute queries.

## Conclusion

The "Social App Python" project developed in Jupyter Notebook demonstrates the implementation of a social application with CRUD functionality. The notebook provides step-by-step explanations and code for adding, deleting, updating, and viewing posts. Additionally, SQL Workbench or a similar SQL client can be used for query practice and testing.

If you have any questions or encounter any issues, please feel free to contact S Antony vinothan at antonyvino777@gmail.com.
