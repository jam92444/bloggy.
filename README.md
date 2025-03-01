# Bloggy - A Django Blog App

**Bloggy** is a blogging platform built using Django where users can share their thoughts, research, ideas, and more through blog posts. Users can create, update, and delete posts, manage their profiles, follow other users, like/dislike posts, save posts for later, and interact with other content in various ways.

---

## Features

### User Authentication
- **Sign Up/Sign In**: Users can register by creating an account and log in with their credentials (email and password).
- **Profile Management**: Users can update their profiles, including their name, bio, profile picture, and more.
- **Account Deletion**: Users can delete their account at any time.

### Blogging
- **Create Posts**: Users can create new blog posts, including text, images, and links to share their thoughts.
- **Edit Posts**: Users can update their posts after publishing them.
- **Delete Posts**: Users can delete their posts when they no longer want them to appear on the platform.
- **Save Posts**: Users can save posts they find interesting for easy access later.

### Social Interaction
- **Follow Users**: Users can follow other users to stay updated on their posts.
- **Like/Dislike Posts**: Users can express their opinions by liking or disliking posts.
- **Comment on Posts**: Users can engage with posts through comments, fostering discussions.
- **Notifications**: Users will receive notifications when they get new followers, likes, comments, or when someone they follow publishes new content.

### Admin Features
- **User Management**: Admins can manage user accounts, block abusive content, and ensure that the community remains safe.
- **Content Moderation**: Admins can remove inappropriate posts or comments.

---

## Tech Stack

- **Backend**: Django (Python framework)
- **Database**: PostgreSQL (for storing user data, posts, comments, likes, etc.)
- **Authentication**: Django’s built-in authentication system (using sessions and tokens)
- **Deployment**: Can be deployed on any server such as Heroku, AWS, or DigitalOcean.

---

## Setup & Installation

Follow these steps to get **Bloggy** up and running on your local machine:

### Prerequisites

- Python 3.x
- PostgreSQL (or another database of your choice)

### Backend Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/bloggy.git
   cd bloggy
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:
   - Make sure you have PostgreSQL installed or use any database that you are familiar with.
   - Update the `DATABASES` settings in the `settings.py` file.

5. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (Admin account to access Django Admin):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

### Database Configuration (PostgreSQL example)

If you're using PostgreSQL, make sure you set up the database correctly in `settings.py`. Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bloggy_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Usage

### User Features

- **Sign Up**: Users can create an account by visiting the registration page and providing a username, email, and password.
- **Log In/Log Out**: Users can log in to the platform using their credentials and log out when done.
- **Create/Manage Posts**: Users can create, update, and delete their posts.
- **Follow Users**: Users can follow others by visiting their profile page and clicking the "Follow" button.
- **Like/Dislike Posts**: Users can express their opinion on posts through likes and dislikes.
- **Comment on Posts**: Users can leave comments on posts, participating in discussions.

### Admin Features

- **Access Django Admin**: The admin can log into the Django Admin interface to manage users, posts, comments, and other content.
  - To access Django Admin, go to `http://127.0.0.1:8000/admin/` and log in with the admin credentials you created during the `createsuperuser` process.

---

## Model Overview

Here’s a simple overview of the core models used in Bloggy:

### **User Model**
- `username`: A unique identifier for the user.
- `email`: User's email address (unique).
- `profile_picture`: An image field for the user’s profile picture.
- `bio`: A short biography that the user can edit.

### **Post Model**
- `author`: A ForeignKey to the `User` model, representing the author of the post.
- `title`: The title of the blog post.
- `content`: The body/content of the post (text).
- `created_at`: Timestamp when the post was created.
- `updated_at`: Timestamp when the post was last updated.

### **Comment Model**
- `post`: A ForeignKey to the `Post` model, linking the comment to a specific post.
- `author`: A ForeignKey to the `User` model, linking the comment to the user who made it.
- `content`: The text content of the comment.
- `created_at`: Timestamp when the comment was created.

### **Follow Model**
- `follower`: A ForeignKey to the `User` model (the user who is following).
- `followed`: A ForeignKey to the `User` model (the user being followed).

### **Like/Dislike Model**
- `post`: A ForeignKey to the `Post` model.
- `user`: A ForeignKey to the `User` model.
- `like`: Boolean indicating whether the user liked or disliked the post.

---

## Contributing

We welcome contributions to Bloggy! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request to the main repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

If you have any questions or need assistance, feel free to open an issue on the GitHub repository or contact us at [email@example.com].

---

Thanks for using Bloggy! We hope you enjoy blogging and connecting with others!

---

This README provides a clear explanation of how to set up and use the Bloggy app built with Django, focusing entirely on the backend without the use of frontend frameworks like React. Let me know if you need further customizations or details!
