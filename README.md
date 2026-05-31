# GitHub Repository Analyzer

A web-based application that analyzes GitHub repositories and provides insights into repository health, contributor activity, language distribution, and project metadata using the GitHub REST API.

## Overview

GitHub Repository Analyzer helps developers quickly understand any public GitHub repository by entering either a repository name or a GitHub URL.

The application fetches real-time repository data from GitHub and presents it through an interactive dashboard with analytics and visualizations.

## Features

### Repository Analytics

* Repository Name
* Owner Information
* Stars Count
* Forks Count
* Primary Programming Language
* Repository Description

### Health Score Analysis

The application evaluates repository quality based on:

* Stars
* Forks
* Open Issues
* Documentation Availability

### Contributor Insights

* Displays Top Contributors
* Contribution Count Analysis

### Language Analytics

* Interactive Language Distribution Chart
* Percentage Breakdown of Languages Used

### Repository Activity

* Creation Date
* Last Updated Date
* Repository Topics

### URL Support

Supports multiple input formats:

```text
microsoft/vscode

https://github.com/microsoft/vscode

https://github.com/CoderOggy78/rag-qa-platform.git
```

### Error Handling

* Invalid Repository Detection
* User-Friendly Error Messages

## Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML5
* Bootstrap 5
* Jinja2 Templates

### Visualization

* Chart.js

### API

* GitHub REST API

## Installation

### Clone Repository

```bash
git clone https://github.com/alokxkh/github-repository-analyzer.git
cd github-repository-analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

## Example Repositories

```text
microsoft/vscode
facebook/react
pallets/flask
tensorflow/tensorflow
```

## Project Structure

```text
github-repository-analyzer/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── README.md
```

## Future Improvements

* Repository Comparison Tool
* Commit Activity Analytics
* Contributor Activity Visualization
* AI-Based Repository Summary
* Deployment Support

## Author

Alok Khanwar

GitHub: https://github.com/alokxkh
