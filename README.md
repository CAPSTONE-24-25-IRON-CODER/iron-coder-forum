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
# Iron-Coder-Forum Work Done
- Built the core structure of the frontend including:
  - Homepage that displays categories/topics
  - Category pages, which list the posts in a particular category
  - Post detail page, which displays a post and its replies
- Implemented basic styling based on the Solarized Light theme in Iron Coder (will likely change the color theme later on)
- Displayed a search bar, copyright bar, navigation bar, reply to post button
# Iron Coder Forum Architecture
- Frontend:
  - The frontend is built using HTML and styled using CSS 
  - Each page currently displays the logo at the top, the navigation bar, and the copyright bar
  - home.html
    - Contains placeholder topics/categories
  - posts.html
    - Contains list of placeholder posts for a particular category
  - details.html
    - Contains post, reply, and placeholder adding comment feature
- Backend:
  - Has not been implemented yet. Planning to use Django 
   
# Known bugs
  - All currently displayed categories/posts are placeholder (not functional)
    - This is simply to give a visualization of what the layout of the website will be
  - There are some styling inconsistencies that will need to be worked on as it relates to the color theme and arrangement of items on the page
  - There are some sizing issues when decreasing the size of the window. These would likely be visible on smaller devices like smartphones as well.  
    
## Homepage
![Homepage](./assets/Screenshots/homepage.png)

## Categories
![Categories](./assets/Screenshots/categories.png)

## Post
![Post](./assets/Screenshots/post.png)