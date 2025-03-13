<div align="center">
  
  <h1>GoPhish</h1>
  
  <p>
    AI and Cybersecurity in Education Simulation for the SANS AI and Cybersecurity Hackathon 2025
  </p>
  
  <p>
    A phishing simulation that sends randomized phishing emails to employees and tracks their interactions. If an employee clicks on a phishing link, they are redirected to an interactive chatbot that educates them about phishing and social engineering tactics.
  </p>
  
  
<!-- Badges (Add links once available) -->
<p>
  <img src="https://img.shields.io/badge/status-in%20development-orange" alt="status" />
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="python" />
  <img src="https://img.shields.io/badge/made%20with-streamlit-red" alt="streamlit" />
</p>
   
<h4>
    <a href="#">View Demo</a>
  <span> · </span>
</h4>
</div>

<br />

## :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  - [Screenshots](#camera-screenshots)
  - [Tech Stack](#space_invader-tech-stack)
  - [Features](#dart-features)
  - [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  - [Prerequisites](#bangbang-prerequisites)
  - [Installation](#gear-installation)
  - [Run Locally](#running-run-locally)
  - [Deployment](#triangular_flag_on_post-deployment)
- [Usage](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [License](#warning-license)
- [Contact](#handshake-contact)

---

## :star2: About the Project

GoPhish is a cybersecurity education tool that helps organizations train employees to recognize phishing attacks. The system automates the process of sending phishing emails at random intervals and tracks user interactions. If a user clicks a link, they are redirected to an AI chatbot that educates them about phishing tactics.

### :camera: Screenshots
![Image](https://github.com/user-attachments/assets/57674436-1ee2-4466-a603-345e0c1e3262)


### :space_invader: Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** MongoDB

### :dart: Features

- Automated phishing email simulations
- AI-powered chatbot for interactive learning
- Tracks user clicks and responses
- Analytics dashboard for monitoring engagement

### :key: Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

```
API_KEY=your_openai_api_key
MONGO_URI=your_mongodb_connection_string
EMAIL_SERVER=your_smtp_server
EMAIL_USERNAME=your_email
EMAIL_PASSWORD=your_password
```

## :toolbox: Getting Started

### :bangbang: Prerequisites

Ensure you have **Python 3.8+** installed.

```bash
python --version
```

### :gear: Installation

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/yourusername/gophish.git
cd gophish
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### :running: Run Locally

Run the application using:

```bash
streamlit run app.py
```

### :triangular_flag_on_post: Deployment

- Sytem was deployed via Streamlit Share

## :eyes: Usage

- The system automatically sends phishing emails at random intervals.
- Employees receive the email and, if they click the link, are directed to the chatbot.
- The chatbot educates them about phishing and records analytics.

## :compass: Roadmap

- [ ] Add support for customizable phishing templates
- [ ] Implement user authentication and role-based access
- [ ] Improve chatbot interaction with more real-life phishing examples
- [ ] Enhance analytics dashboard

## :warning: License

_(License information to be determined)_

## :handshake: Contact

Project Team:

- [Tatenda Moyo](https://www.linkedin.com/in/tatenda-moyo-576235220/)
- [Khawulela Mpono](https://www.linkedin.com/in/khawulela-mpono-9a7744163/)
- [Sbonelo Dube](https://www.linkedin.com/in/sbonelodube/)
- [Manqoba Nkosi](https://www.linkedin.com/in/manqoba-nkosi-iot/)
- [Charlie Mashinini](https://www.linkedin.com/in/charlie-s-mashinini-490444272/)

Project Link: [https://github.com/yourusername/gophish](https://github.com/yourusername/gophish)
