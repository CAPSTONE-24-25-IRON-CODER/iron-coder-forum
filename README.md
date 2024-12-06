# How to Setup the Forum
* Ensure that you have python and pip installed on your machine!
    * Note that these instructions are for Windows! 
* Clone the repository:
```
git clone https://github.com/CAPSTONE-24-25-IRON-CODER/iron-coder-forum.git
```
* Enter the cloned repository:
```
cd iron-coder-forum
```
* Run `setup_project.bat' in the terminal. 
    * Alternatively, you double click on it in the file explorer
* The above steps should as long as you have python and pip installed.
* Now, navigate to `http://127.0.0.1:8000/` in the browser
* To access the admin page, navigate to `http://127.0.0.1:8000/admin`
    * Credentials that can be used for the admin page:
        *  Username: admin
        *  Password: testpassword
# Iron-Coder-Forum Work Done
* Frontend
    * Homepage, list of posts, and post pages are viewable and integrated with backend 
    * Login feature has been implemented
        * Only users that are logged in can post
    * Signup feature has been implemented
        * Users select username, password, display name, bio, and profile pic
    * Separate pages for login and signup
    * Implemented a Create Post page
        * Users can select a category
        * Gets reflected in the backend 
    * Displayed a search bar, copyright bar, navigation bar, reply to post button
* Backend
    * Admin can create posts, categories, replies, and comments for admin page
        * User registration implemented
        * All actions in the backend are visible in the app and vice versa
        * Posts need to be approved before being displayed
* Implemented basic styling based on the Solarized Light theme in Iron 
# Iron Coder Forum Architecture
- Frontend:
  - The frontend is built using HTML and styled using CSS 
  - Each page currently displays the logo at the top, the navigation bar, and the copyright bar
  - home.html
    - Displays topics/categories
  - posts.html
    - Contains list of posts for a particular category
  - details.html
    - Contains post, reply, and placeholder adding comment feature (will be implemented later)
- Backend:
  - The forum’s architecture is built with Django and utilizes its Model-View template framework to manage the frontend-backend interactions. The backend consists of models that represent authors, categories, posts, comments, and replies. The author model defines user functionality while models like categories/posts define the hierarchy of the discussion forums. Django’s admin page is used to manage all of the backend elements. For authentication, Django’s auth system was used. Posts, categories, comments, and replies are connected. A post belongs to a category and can have multiple comments. Comments can have multiple replies.

   
# Known bugs
 - When creating an account without setting a profile picture, application may crash when trying to view the post in the frontend
 - Creating a post sometimes causes the application to crash
    - Not sure exactly why. Only observed this happening once after randomly typing into the input fields. Might be related to signing into the 
- If you are signed into a user account on the forum and then log into an admin account on the admin page, the user will be logged out and replaced by the admin on the forum
    - To prevent this, sign into the forum with a user account in an incognito tab
 - There are some styling inconsistencies that will need to be worked on as it relates to the color theme and arrangement of items on the page
 - There are some sizing issues when decreasing the size of the window. These would likely be visible on smaller devices like smartphones as well.  
    
## Homepage
![Homepage](./assets/Screenshots/homepage.png)

## Categories
![Categories](./assets/Screenshots/categories.png)

## Post
![Post](./assets/Screenshots/post.png)