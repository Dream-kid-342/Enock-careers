# Flask Documentation Builder

This project is a Flask-based application for building and serving PyTorch documentation sites.

## Features

- Build PyTorch documentation from source
- Serve documentation via a Flask web server
- Download and manage documentation archives

## Requirements

- Python 3.9+
- Flask
- git
- ffmpeg (if using video features)
- pip

## Setup

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd ml-docs
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Build the documentation site:
   ```bash
   python build_pytorch_docs_site.py
   ```

2. Run the Flask server:
   ```bash
   flask run
   ```
   or, if you have an `app.py`:
   ```bash
   python app.py
   ```

3. Access the documentation in your browser at [http://localhost:5000](http://localhost:5000).

## Notes

- Ensure `ffmpeg` and `git` are installed and available in your system PATH if required.
- For development, use a virtual environment to avoid dependency conflicts.

## License

MIT License
