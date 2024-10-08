# AI Course Planner Web App



### Team Members
- David Wang
- Arunjay Agrawal
- Ish Patel
- Harshwardhan



### Project Description
A web application that generates personalized course recommendations for future semesters using course data, Reddit posts and AI.



### Built With
* [![Next][Next.js]][Next-url]
* [![Flask][Flask]][Flask-url]
* [![Tailwind][Tailwind CSS]][Tailwind-url]



## Getting Started

### Prerequisites

- npm ([Download Node.js])
  ```sh
  npm install npm@latest -g
  ```
- Python ([Download Python])



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SDC-Fall-2024/Team-30-AICoursePlanner
   ```
2. Set up a Python virtual environment
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment
    - Windows
        ```sh
        venv\Scripts\activate
        ```
    - macOS/Linux
        ```sh
        source venv/bin/activate
        ```
4. Install Python dependencies
   ```sh
   pip install Flask flask_cors
   ```
5. Install NPM packages
   ```sh
   cd frontend
   npm install
   ```
6. Get a free API Key at [https://example.com](https://example.com)
7. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```



### Running the web app
- To start the Flask backend in a new terminal
    ```sh
    cd backend
    python server.py
    ```
- To start the Node.js frontend in a new terminal
    ```sh
    cd frontend
    npm run dev
    ```



## Demo
If your app is hosted on a published website, include the link here



<!-- MARKDOWN LINKS & IMAGES -->

[Download Node.js]: https://nodejs.org/en/download/prebuilt-installer

[Download Python]: https://www.python.org/downloads/

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/

[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/

[Tailwind CSS]: https://img.shields.io/badge/Tailwind_CSS-black?style=for-the-badge&logo=tailwind-css&logoColor=38B2AC
[Tailwind-url]: https://tailwindcss.com