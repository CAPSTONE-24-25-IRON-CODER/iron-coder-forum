# Iron-Coder-Forum Work Done
- Built the core structure of the frontend including:
  - Homepage that displays categories/topics
  - Category pages, which list the posts in a particular category
  - Post detail page, which displays a post and its replies
- Implemented basic styling based on the Solarized Light theme in Iron Coder (will likely change the color theme later on)
- Displayed a search bar, copyright bar, navigation bar, reply to post button
- Display placeholder categories/posts in order to give a visualization of the forum layout
- Implemented some Javascript functionality to easily navigate between the different components 
# Iron Coder Forum Architecture
- Frontend:
  - The frontend is built using HTML, CSS, and Javascript
  - Each page currently displays the logo at the top, the navigation bar, and the copyright bar
  - home.html
    - Contains placeholder topics/categories
  - posts.html
    - Contains list of placeholder posts for a particular category
  - details.html
    - Contains post and reply and placeholder adding comment feature
- Backend:
  - Has not been implemented yet. Planning to use Django 
   
# Known bugs
  - All currently displayed categories/posts are placeholder (not functional)
    - This is simply to give a visualization of what the layout of the website will be
  - There are some styling inconsistencies that will need to be worked on as it relates to the color theme and arrangement of items on the page
  - There are some sizing issues when decreasing the size of the window. These would likely be visible on smaller devices like smartphones as well.  
    

