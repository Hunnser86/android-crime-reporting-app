# Android Crime Reporting App

THE ANDROIDS ARE TAKING OVER!!!!

As we all know by now, the Androids are trying to take the place of Humans on planet earth.

This must not be allowed to happen.

That is why, The Police and Crime Commission have requested this software for their officers.

An app that allows officers to CREATE, READ, UPDATE AND DELETE reports of Android crimes and details of Androids that are known to the system.

It will connect with our database on MongoDB, where we have previous crimes and android data stored.

I expect all of you Scrappers(Officers), will find it easy to navigate and intuitive to use.

---

## Index - Table of contents
* [User Experience (UX)](#user-experience) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Acknowledgements](#credits)

## User Experience (UX)

---


* ### **User Stories**
     
     * **Site Owner Goals**
        
       **To help report and catalogue Android crime.**

        *  To make it simple to understand. 
        *  To make it easy for officers to create, read, update and delete reports.
        *  Allow officers to read information about known androids.
            
     * **Visitor Goals**

       *  Visitors should be able to easily navigate the site
       *  Perform C.R.U.D functions on any reports
       *  Have confirmation about the actions they have taken
---
 ## Structure

 ***
  All pages will have the same navigation bar at the top, with links to add reports, view reports and view known androids.

  The home page has a welcome message and an explaination of what the site is for.  There are two buttons at the bottom that navigate to the add report and view report pages.

  On the Add Report page, there is a form for the officer to fill in.  The form uses front end validation techniques, to ensure that the information given is what is needed to keep the database consistant.

  Once the form is filled out, the user clicks the submit button at the bottom of the page.  This takes them to a page that says "Report successfully submitted", where the user can then navigate to any of the other pages.

  On the view reports page, the user can read, update and delete reports, using the buttons within the detailed report dropdown.  When a user attempt to delete a report, a modal appears, asking if the user is sure they want to delete the report, just in case the button is pressed accidentally.

  The final page is a known androids page, which details some of the known androids on the database.  Each android is displayed on a card with an image at the top.  The cards also display name, location, occupation, detention status and previous crimes committed by the android. 

## Database Design

I decided to use MongoDB for my database.  Therefore all the data is stored in key/value pairs (The most simple kind of data storage system).  I found this was the correct way to store my data, as it was very simple in it's nature e.g. android name, location etc.

It was an easy way to later fetch the data to display it to the user via jinja and dot notation in the HTML templates by providing the key to MongoDB.

The advantage of using a key/value database, is that it can be used as a cache to speed up the retrieval of commonly used data.  However, the disadvantage of this type of database is that the data being sent to it is uncontrolled, and needs a form of control to avoid bad data being stored.  I took care of this by using front end validation on the form elements of the app. 


---
 ## Design
---
   * **Colours**
       
       * The site is designed in the retrofuturism style, depicting the old black and green phosperescent monitors from the 80s.  Simple, yet effective, giving great contrast on the screen. This is said to be one of the best contrast colour schemes to use for the visually impaired.
       
   * **Typography**

       *  I used the 'Share Tech Mono' and 'Monospace' fonts from google fonts.
        
          I used these fonts as I felt it fit the art style of the site.

   * **Imagery**

     *  The imagery used was a simple black background with green text.
        
     *  The images used for the androids were stock photos from Pexels.
     I used the image URLs on the database.

* **Wireframes**

    * I made some simple wireframes in the design process to show how it will look.  As you can see, the original idea was a workshop database, for androids that had broken down.
---

   ![screenshot of the wireframe process](/assets/wireframes/wireframe-1.png)

    
# Features 
  ### Welcome Page
     
* The first page the user will land on, is the welcome page.  On this page, there is a welcome message, followed by a description of what the site is for.  There is a navbar that is consistant accross all pages, that has links to home, add report, view reports and known androids pages.  Under the message, there are two buttons.  One to add a report and one to view previous reports.


### Add Report Page

* On this page, there is a form for the user to fill out.  There are several categories to choose from in regards to crime type.  The user simply follows the form down to the bottom of the page and submits the report.  There are several front end validation techniques, to ensure that the user fills out the form correctly.  For example, min and max length, type="text", pattern(a-zA-Z) and the required attribute.  These are used to ensure consistancy of data on the database.


# Technologies Used

## **Launguages**

    
 * [HTML5](https://en.wikipedia.org/wiki/HTML5) - Mark-up language using semantic structure.
 
 * [CSS3](https://en.wikipedia.org/wiki/CSS) - Cascading style sheet used to style.

 * [JavaScript](https://en.m.wikipedia.org/wiki/JavaScript) - Programming language, used to activate the collapsible side nav and form elements, through the use of jQuery.

 * [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))- Programming language used to create the main app and render the html templates.
 
 

 ## **Frameworks, Libraries and Programs Used**

 1. [Materialize CSS](https://materializecss.com/)

   * I used Materialize to create the form elements, collapsable elements.

 2. [jsdelivr:](https://getbootstrap.com/)   

   * jsdelivr was used to enable GitHub to serve my web files without any configuration.

 3. [Git:](https://github.com/)  

   * Git was used for version control of the game by using the git commit and git push functions in the terminal, to to ensure any changes I made were not lost and were also meaningful to the development process. It would also help any other developers to assess or make changes in a real world setting.

 4. [GitHub:](https://github.com/)

   *  GitHub was used to store the code from the project after being pushed from the terminal.

 5. [Figma:](https://www.figma.com/)  

  * I used Figma for the Wireframe, to full site visual design process.

 6. [Google Fonts](https://fonts.google.com/) 

  * I used the font Tourney from Google fonts, as it looked the fitting
    for the style of the game.  

 7. [jQuery](https://en.wikipedia.org/wiki/JQuery)

  * I used jQuery to activate the Materialize drop down menu, mobile side nav and the sweet alert function upon attempting deletion of reports.

 8. [MongoDB](https://www.mongodb.com/)

  * I used MongoDB to store all the data given by the user and the data on the known androids.     


# Testing

For my testing I used manual testing.

For testing the code for errors, I used the following;

- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

- [pep8online.com](http://pep8online.com/)

- [W3C Markup Validation](https://validator.w3.org/)

These were used in particular, to check for errors in the code to enable me
to rectify these and have a fully functioning website.

# Testing the app functionality

For the functionality tests, I ran through what I considered to be the core 
functions of the app and attempted to use them as a standard user would.  I also checked that the correct data only was being sent to and from the database.
The results are as below.

| Test Label     | Test Action   | Expected Outcome  | Test Outcome | 
| -------------  |-------------- |----------------- | ------------ |
| Home Page<br>Display    | All aspects of the <br> page are displaying <br> correctly. | The page displays<br> correctly. | PASS
| The Nav hover <br> works correctly      | Hover the cursor<br> over the nav links. |  The link switches <br> colours  | PASS
| The button hover<br>works correctly.  | Hover the cursor <br>over the buttons. | The buttons switches<br>colours.   | PASS |
| All links work<br>correctly.  | Attempt to use<br> the links  | The links go to the<br>correct page.   | PASS | 
| All buttons work<br> correctly | Attempt to use the <br> buttons. | Buttons go to the <br> correct page. | PASS 
| Form inputs accept<br> user input. | Attempt to input <br> data. | Input is accepted. | PASS
| Form validation<br>works correctly.| Attempt to input<br>invalid data. | Form validation<br>gives a warning<br>stating to the user<br> that the data is invalid. | PASS |
 only correct<br>data goes to<br>the database.| Attempt to input<br>invalid data. | Form validation<br>does not allow<br>incorrect data to <br>be sent to and <br>from the database | PASS  

# Testing the app during the build

To test the app while I was coding, I checked that the CRUD functions were working correctly, by physically checking the database to ensure that the actions and data were being executed properly.  For the @app.routes, I simply used the live preview to check that the pages were being displayed properly and that the redirects were going to the correct page.

| Test Label     | Test Action   | Expected Outcome  | Test Outcome | 
| -------------  |-------------- |----------------- | ------------ |
| user can create <br> a report. | Attempt to <br>create a <br>report. | The report is<br>successfully<br>sent to the <br>database. | PASS
| User can <br>read reports.| Go to the view<br>reports page to<br>check the reports are<br>being displayed.| The reports are<br>displayed<br>correctly. | PASS
| Does the dropdown<br>menu work for viewing<br>reports | Click on the carret <br>to check the functionality. | Dropdown functions<br>correctly. | PASS
|The edit report<br>button works. | The edit report button <br>goes to the edit report <br>page. | The button goes to<br>the correct page.   | PASS |
| Users can edit<br>a report. | attempt to edit a<br>report. | The submit button <br>takes the user <br>to the edit success <br>screen.   | PASS |
| Edited reports<br>are changed on the<br>database. | Check the database<br>to see if the report<br>has been updated. | The report has been <br>updated.   | PASS |
| Users can remove<br>reports. | Attempt to delete<br>the report. | The report has been <br>deleted. | PASS 
| Delete confirmation <br>warning is displayed. | Attempt to delete<br>the report. | The warning <br>is displayed. | PASS
| Reports have been<br>reomved from the <br>database. | Check the database<br>to see if the report<br>has been removed. | The report has been <br>removed from the<br>database. | PASS
| Known android<br>data is loaded from<br>the database correctly. | View the known<br>androids page. | All data is correctly <br>displayed on the page. | PASS


# Code errors from the validator tools

While there is a lot of code in this project, I am happy to confirm, there are no errors after running the code into the different validators.

---

## Known Bugs
---

The only bug that I came accross during development was that the category dropdown on the add report page was unable to be styled correctly, leaving it more narrow than the other inputs.  However, it still functions correctly and does not look out of place.

---

## Site owner Goals testing

  **To help report and catalogue Android crime.**

   *  **To make it simple to understand**
          
        This was achieved by giving the user a brief explaination of what the app was for on the home page. There is a nav bar that populates the top of each page and all the form elements and buttons are clearly labeled and positioned seperately, allowing the user to easily undertand the intended flow of the app.       
    
 *  **To make it easy for officers to create, read, update and delete reports.**
      This was achieved, by having a simple form for report creation, which is fully labeled and has front end validation to avoid any bad data being sent to the database.

      There is a view reports page, where the user can read all the previous reports.  Within the reports there are buttons that are clearly marked, allowing the user to edit or remove reports.  When users attempt to remove a report, an alert pops up to ask them to confirm that they are sure, to make sure that reports don't get removed by accident. 
 
    
 
 *  **Allow officers to read information about known androids.**

     To achieve this, I have created a known androids page.  This page contains an image and the details of all the known androids.
            
    
---


## Visitor Goals



 *  **Visitors should be able to easily navigate the site**
      
      Users can easily navigate the site either by using the nav bar at the top of each page, or using the buttons that are clearly marked with their functions.

      
 *  **Perform C.R.U.D functions on any reports**

     As stated above, the users can perform all the C.R.U.D functions by following the flow of the app, or by visiting the previously reported crime page and using the buttons to edit or remove reports. 


 *  **Have confirmation about the actions they have taken**

      Each time the user performs one of the C.R.U.D functions, they are taken to a seperate page confirming that the actions they have taken have been successful.  When the user attempts to remove a report, an alert pops up asking them to confirm the action.      

---
# Client based testing

  * For the client based tests, I sent the link to the app to various people and asked them, to 
  use it.  I asked the first person to test it on mobile devices such as , mobile phones and tablets.
  
    They were asked to check both orientations, to see if the responsiveness worked.
    They were also asked to check the site accross Chrome, Firefox and Opera browsers to check compatability.

  * For the next test I asked three people to check the desktop version of the app. Each of them had a different browser.  One had Chrome, one had Firefox and one had Opera.  

    I asked them to check the app for glitches such as items not displaying correctly and gramatical errors.

  * After the tests were completed, they reported back that the gapp worked fine accross all browsers
  and the responsiveness worked on all the mobile devices that were used.  There were no gramatical errors either (which was nice).    

# Deployment

  * To deploy the app, I linked my Github to heroku.

  
---

# Running the game locally

  *  To run the game locally, you will need to clone the GitHub [repository](https://github.com/Hunnser86/Spaceball-shooter-game)

  *  To do this, simply go to the GitHub [repository](https://github.com/Hunnser86/Spaceball-shooter-game).

     * Next, click the dropdown menu named "code".  This will bring up the clone menu.
     
     * Select HTTPS and copy the link.

     * Create a location on your local computer, where you would like to clone the repository.

     * Then on your local terminal use the "git clone" command and paste the link after it and hit return.

     * This will create a folder in the location you have created.  This will contain all the files from the
     repository, allowing you to run the site.

# Credits

  **Content**

  * All code was written by myself (Rob Hunns).

  **Tutorials**

  * [For ideas on creating enemy ships](http://blog.sklambert.com/html5-canvas-game-the-enemy-ships/)  

  * [For tips on canvas](https://www.w3schools.com/tags/ref_canvas.asp)

  * [For information on canvas arc to draw the characters](https://www.w3schools.com/tags/canvas_arc.asp)

  * [For information on collision detection](https://happycoding.io/tutorials/processing/collision-detection)

  * [For how to move objects](https://stackoverflow.com/questions/6199018/moving-objects-on-html5-canvas)

  * [for creating particles](https://modernweb.com/creating-particles-html5-canvas/)



  


#  Acknowledgements
  
 

  * I would first like to acknowledge my mentor Brian, for the suppoprt he has
    given me during the project.  Particularly for giding me towards good documentation, for the parts of the project where I needed to do a bit more research.

  * Codeinstitute: For providing such good training and tutorials, giving me the confidence to 
    keep going and to hone my problenm solving skills.
    
      






