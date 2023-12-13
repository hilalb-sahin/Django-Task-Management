# Team *Magpie* Small Group project

## Team members
The members of the team are:
- *DEIVIDAS JUSKA*
- *YOHANN PIRBAY*
- *HILAL SAHIN*
- *HUMAYRA TAPALI*
- *HENG ZHANG*

## Project structure
The project is called `task_manager`.  It currently consists of a single app `tasks`.

## Deployed version of the application
The deployed version of the application can be found at [*enter url here*](*enter_url_here*).

## Installation instructions
To install the software and use it in your local development environment, you must first set up and activate a local development environment.  From the root of the project:

```
$ virtualenv venv
$ source venv/bin/activate
```

Install all required packages:

```
$ pip3 install -r requirements.txt
```

Migrate the database:

```
$ python3 manage.py migrate
```

Seed the development database with:

```
$ python3 manage.py seed
```

Run all tests with:
```
$ python3 manage.py test
```

*The above instructions should work in your version of the application.  If there are deviations, declare those here in bold.  Otherwise, remove this line.*

## Sources
The packages used by this application are specified in `requirements.txt`

Uses of chatGPT:

Deividas:

- Magpie/tasks/models.py Task class: When I originally coded the task class I didn't know models.DateField existed when attempting to implement a due date (less than 25% of the unit). User class: I didn't know how to seed a superuser so chatGPT explained it could be done by adding is_superuser and is_staff fields to the user model (less than 25% of the unit).

- Magpie/tasks/management/commands/seed.py: generate_task function: I didn't know how to get Faker to seed future dates so I had chatGPT show me how to (less than 25% of the unit).


Yohann:

- Magpie/tasks/templates/create_task.html I used chatGPT to help me add an eventlistener to trigger the javascript (less than 25% of the unit).

- Magpie/tasks/admin.py I couldn't find a way to show a many to many field on the admin panel, so I used chatGPT to help me for the TaskAdmin (less than 25% of the unit).

- Magpie/tasks/models.py I just double checked with chatGPT how to correctly use the 'related name' parameter in the Task Model (less than 10% of the unit).

- Magpie/tasks/forms.py Used chatGPT to find how to correctly have a multiple checkbox for Team form (less than 10% of the unit).

