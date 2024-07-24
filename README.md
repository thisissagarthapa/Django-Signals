# Django-signals

This project demonstrates the use of Django signals to handle various events within a Django application. Signals are used to perform certain actions when specific events occur, such as user login, logout, database operations, and request handling.

## Features

- **User Authentication Signals**:
  - `user_logged_in`: Triggered when a user successfully logs in.
  - `user_logged_out`: Triggered when a user logs out.
  - `user_login_failed`: Triggered when a user login attempt fails.

- **Model Signals**:
  - `pre_save`: Triggered before a model instance is saved.
  - `post_save`: Triggered after a model instance is saved.
  - `pre_delete`: Triggered before a model instance is deleted.
  - `post_delete`: Triggered after a model instance is deleted.
  - `pre_init`: Triggered before a model instance is initialized.
  - `post_init`: Triggered after a model instance is initialized.

- **Request Handling Signals**:
  - `request_started`: Triggered when a request is started.
  - `request_finished`: Triggered when a request is finished.
  - `got_request_exception`: Triggered when a request raises an exception.

- **Migration Signals**:
  - `pre_migrate`: Triggered before the migration process starts.
  - `post_migrate`: Triggered after the migration process completes.

- **Database Connection Signal**:
  - `connection_created`: Triggered when a new database connection is created.
