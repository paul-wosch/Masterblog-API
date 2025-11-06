# Masterblog-API

This is the next iteration of the Masterblog project.  
It is structured as a modular web application with two main parts:

- **api-server**: A Flask REST API that exposes endpoints returning JSON data.  
  Handles business logic, data storage, and API provision.  
  Reuses core models from the [masterblog-core](https://pypi.org/project/masterblog-core/) package.

- **ui-server**: A Flask application that serves HTML templates and static assets.  
  The UI relies primarily on client-side rendering via JavaScript, consuming the API
  provided by the `api-server` to dynamically render and update content.  
  Handles user interface and interaction in the browser.

## Status
🚧 Work in progress — initial scaffolding only (.gitignore, LICENSE, README).  
Project structure and implementation will follow in upcoming commits.

## License
This project is licensed under the terms of the LICENSE file included in the repository.
