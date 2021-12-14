# Full Stack Evaluation

### **Welcome to Pumpkin's Full Stack Evaluation.**

This task combines both frontend and backend components.

The frontend is built in React and JS and the backend is Python with Flask.  

### **How it Works**

- Clone this repo: [git@github.com](mailto:git@github.com):pumpkincare/fullstack.git
- Complete the exercise.
- Return a link to or a zip file of your git repo.

You are being asked to alter an existing feature and create a new view for the resulting calculation.  This task should not take more than an hour or two.

It is important to us that this exercise not become a burden. Feel free to be as elaborate or expressive as you see fit, but we also recognize that you are a person with a life, friends, and family. We are using it as a filter and not the end-all-be-all of your capabilities.

### **Context**

- When a customer makes a wellness claim, Pumpkin's claims adjusters seek to approve claimed line items.
- A line item represents a specific product or service from an invoice.
- A customer is allotted a specific amount of products or services they can use within a given policy year.  We call this *utilization*.
- When a line item is approved, we reflect that on their utilization (the business logic is describe in the requirements).

The frontend is intended to be simple and unbranded.  If you find the time to do more, please do make it as beautiful as you wish to.  You can add in some branding if you choose, make it responsive.  All of the libraries you need should be included in the repository.

The backend will provide you with the components you need to get started, but will require some changes in order to accommodate the product requirements.  If you find that you have the time, please do make any improvements to the code you see fit.

### **Setup**

- To run the database and backend application, run `docker-compose up -d` from the `./` directory.
- To run the front end application, run `yarn start`  from the `./front-end` directory.
- To generate database schema updates and apply those updates on the database, run both
    - `./backend/devops/local/alembic-generate-revision.sh`
    - `./backend/devops/local/alembic-upgrade.sh`

This exercise will form the basis of your interview.  Please let us know if you have questions.

### Basic Requirements

- Add a field to the line item display that will allow a user to select whether a line item is approved or not approved according to the wireframes.
- The backend must receive the update and store in the db whether a line item is approved or not.
- Create an endpoint to retrieve the utilization for particular claim.
    - For example, if a line item of type "vaccine" is marked as approved, then vaccine utilization is incremented by 1 and remaining is decremented by 1
- On the utilization page:
    - Create a table that displays:
        - The utilized category: medicine, vaccine, wellness, etc.
        - Amount utilized
        - Amount remaining
