# Ophelia Resturant

💻 [Visit live website](https://ophelia-resturant-856f44a031c1.herokuapp.com/)  
(Ctrl + click to open in new tab) 

![Mockup image](docs/features/mockup.jpg)

**Developer: Daniel Elde-Johansson**

## Table of Contents
1. [About](#about)
2. [Project Goals](#project-goals) 
     1. [User Goals](#user-goals) 
     2. [Site Owner Goals](#site-owner-goals)
3. [User Experience](#user-experience)
     1. [Target Audience](#target-audience)
     2. [User Requirements and Expectations](#user-requirements-and-expectations)
4. [User Stories](#user-stories)
     1. [Users](#users)
     2. [Admin](#admin)
     3. [Site Owner](#site-Owner)
5. [Design](#design)
     1. [Colors](#colors)
     2. [Fonts](#fonts)
6. [Structure](#structure)
     1. [Website pages](#website-pages)
     2. [Database](#database)
     3. [User Model](#user-model)
7. [Wireframes](#wireframes)
8. [Technologies Used](#technologies-used)
9. [Features](#features)  
    1. [Home page](#home-page)  
    2. [Logo & Navigation](#logo--navigation)  
    3. [Footer](#footer)  
    4. [Sign up / Register](#sign-up--register)  
    5. [Login](#login)  
    6. [Logout](#logout)  
    7. [Booking](#booking)  
    8. [My Bookings](#my-bookings)  
    9. [Edit Booking](#edit-booking)  
    10. [Cancel Booking](#cancel-booking)  
    11. [Food Menu](#food-menu)  
    12. [Drinks Menu](#drinks-menu)  
    13. [Contact Us](#contact-us)  
    14. [Social Media Links](#social-media-links)
10. [Validation](#validation)  
    1. [HTML Validation](#HTML-validation)  
    2. [CSS Validation](#CSS-validation)  
    3. [PEP8 Validation](#PEP8-Validation)  
    4. [Lighthouse](#Lighthouse)  
    5. [Wave](#Wave)  
    6. [Desktop](#Desktop)  
    7. [Mobile](#Mobile)
11. [Testing](#testing)  
    1. [Manual testing](#manual-testing)  
    2. [Automated testing](#automated-testing)  
12. [Bugs](#bugs)
13. [Heroku Deployment](#heroku-deployment)
14. [Credits](#credits)
15. [Acknowledgements](#acknowledgements)

### About  

Ophelia is a made-up, world-leading Michelin restaurant with a tasting menu where users can create an account, book a table, read about us, and view the drink menu.

## Project Goals

### User Goals

* To create a timed table booking.
* To be able to view edit and cancel bookings.
* To view menus, a blog and contact info.

### Site Owner Goals

* To provide a solution to allow users to book a table online. 
* To attract more business with a well crafted site.
* Provide a modern application with an easy navigation.
* Fully responsive and accessible.
* To make a Classy website that shows what a resturant we are.

<hr>

## User Experience

### Target Audience
* Users that wish to book a table for a meal or a party with family and friends
* Past and new customers for the business
* Tourists visiting the area that are looking for a meal or a drink or both
* People employed in the area to drink after work
* people who would like to try new worldleading food

### User Requirements and Expectations

* Fully responsive
* Accessible
* A welcoming design
* Social media
* Contact information
* Accessibility


##### Back to [top](#table-of-contents)<hr>

## User Stories

### Users

1.  As a User I can navigate across the site so that I can move to each feature of the site easily.
2.  As a User I can use a navbar, footer, and social icons so that I can navigate the site, access menus, and access socials.
3.  As a User I can view the opening hours and contact details so that I know when the business is open and how to contact them via email, phone and socials.
4.  As a User I can create a booking by selecting a date and time so that I can reserve my table.
5.  As a User I can update my booking so that I can choose another available time and date.
6.  As a User I can delete my booking so that I can cancel my table reservation.
7.  As a user I can view my booking so that I can remind myself of the date and time I have booked.
8.  As a User I can register to create an account so that my details are stored for faster booking in future.
9.  As a user I can login so that I can book a table.
10. As a user I can see my login status so that I know if I am logged in or not.
11. As a User I can view the site's about us page to get to know the resturant.
12. As a User I can view the drink menu so that I can decide wether to drink at the business.
13. As a User I can view the food menu so that I can decide wether to eat at the business.
14. As a User I can not book a date in the past so that my booking is valid.
15. As a User I can not book a table already booked so that my booking is valid and not double booked.

### Admin

16. As an Admin I can login to add or remove items from the drinks menu so that we can add more drinks or remove them 
17.	As an Admin / Authorised User I can log in so that I can access the back end of the site.
18.	As an Admin / Authorised User I can manually add a booking so that I can book a table if someone phones, or emails the business.
19. As an Admin / Authorised User I can filter bookings by date so that I can see what bookings we have for a particular day.

### Site Owner

20. As a Site Owner I can provide a fully responsive site for my customers so that they have a good user experience.
21. As a Site Owner I can validate data entered into my site so that all submitted data is correct to avoid errors.

## Design

### Colors

I used only black, because dark themes are popular so I wanted to keep the site on a dark theme and not overly bright.

### Fonts

The fonts selected were from Google Fonts.

## Structure

### Website pages

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.

* The site consists of the following pages:
  * Homepage with cards for the user to choose to book a table, view the food or drinks menu.
  * Food menu has the current list of all available foods from the database sorted by starters, mains and desserts
  * Drinks menu has the current list of all available drinks from the databse sorted by type
  * About page that gives a small presentation about the resturant.
  * Book page allows registered users to book a table , guest count, date requested, time requested and table location
  * My bookings displays all bookings for the user that they have made, bookings in the past are automatically expired
  * Edit booking allows the user to change their date, time, table and guest count
  * Cancel booking allows the user to cancel the booking which will then delete it from the database
  * Contact us allows the user to send us a DM if the are registered, or they can contact us from the displayed email and phone number or visit the address listed.
  * Login / Logout allows users to login to make bookings, view, edit, and delete bookings
  * Register allows the user to regiser so they can use the booking system
  * 404 error page to display if a 404 error is raised

### Database

* Built with Python and the Django framework for the deployed Heroku version

<details><summary>Database</summary>
<img src="docs/features/databasedesign.jpg">
</details>


### User Model

The User Model contains the following:
* user_id
* password
* username
* first_name
* last_name
* email
* date_joined
* max_seats
* available
* booking_id (PrimaryKey)
* created_date
* requested_date
* requested_time
* guest (ForeignKey)
* guest_count

## Wireframes

The wireframes were created using Balsamiq

<details><summary>Home</summary>
<img src="docs/wireframes/homewireframes.jpg">
</details>

<details><summary>menu</summary>
<img src="docs/wireframes/menuwireframes.jpg">
</details>

<details><summary>Book a Table</summary>
<img src="docs/wireframes/bookwireframes.jpg">
</details>

<details><summary>Bookings</summary>
<img src="docs\wireframes\bookingswireframes.jpg">
</details>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

* [Am I Responsive](http://ami.responsivedesign.is/)
* [Balsamiq](https://balsamiq.com/)
* [Bootstrap v5.2](https://getbootstrap.com/)
* [Cloudinary](https://cloudinary.com/)
* [Favicon.io](https://favicon.io)
* [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
* [Font Awesome](https://fontawesome.com/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Google Fonts](https://fonts.google.com/)
* [Heroku Platform](https://id.heroku.com/login)
* [jQuery](https://jquery.com)
* [Postgres](https://www.postgresql.org/)
* [Summernote](https://summernote.org/)
* Validation:
  * [WC3 Validator](https://validator.w3.org/)
  * [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  * [JShint](https://jshint.com/)
  * [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  * [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  * [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)

## Features

### Home page

* Home page includes nav bar, main body and a footer

<details><summary>Screenshot</summary>
<img src="docs/features/homepage.jpg">
</details>

### Logo & Navigation

* Custom logo for the business
* Fully Responsive
* On small screens switches to hamburger menu
* Indicates login/logout in status
* displayed on all pages

<details><summary>Screenshot</summary>
<img src="docs/features/login.jpg">
<img src="docs/features/logout.jpg">
<img src="docs/features/logintelephone.jpg">
</details>

### Footer

* Contains social media links and copyright
* Contains Addres, opening hours and contact information
* displayed across all pages

<details><summary>Screenshot</summary>
<img src="docs/features/footer.jpg">
</details>

### Sign up / Register

* Allow users to register an acoount
* Username and password is required, email is optional 

<details><summary>Screenshot</summary>
<img src="docs/features/register.jpg">
</details>

### Login

* User can login to create a booking, view bookings, edit and delete bookings
* user can click to remember the username and password

<details><summary>Screenshot</summary>
<img src="docs/features/signin.jpg">
<img src="docs/features/signinerror.jpg">
</details>

### Logout

* Allows the user to securely log out
* Ask user if they are sure they want to log out

<details><summary>Screenshot</summary>
<img src="docs/features/signout.jpg">
</details>

### Booking

* Allows the user to book a table using the booking form
* Allows the user to choose how many are comming
* Allows the user to choose what date
* Allows the user to choose what time

<details><summary>Screenshot</summary>
<img src="docs/features/booking.jpg">
</details>

### My Bookings

* Allows the user to see all their bookings in a paginated layout, 4 per page
* If the booking is older than today it is automatically expired for the user
* Status of the booking is displayed, awaiting confirmation and when approved will then change to confirmed status for the user

<details><summary>Screenshot</summary>
<img src="docs/features/bookings.jpg">
</details>

### Edit Booking

* Allows the user to edit their booking to another date, time, guest count and table

<details><summary>Screenshot</summary>
<img src="docs/features/editbookings.jpg">
</details>

### Cancel Booking

* Allows the user to cancel their booking, asks user are they sure

<details><summary>Screenshot</summary>
<img src="docs/features/cancel.jpg">
</details>

### Contact Us

* Contact info such as, phone, email, and address is displayed
* A Google Map is embedded with the address for users to use
* All links are interactive and takes you where u need to get
* Displayed on all pages

<details><summary>Screenshot</summary>
<img src="docs/features/contact.jpg">
</details>

### Social Media Links 

* A logo and link is used for each social media displayed
* All links open in a new tab to ensure user is not directed away from the business
* Displayed on all pages

<details><summary>Screenshot</summary>
<img src="docs/features/social.jpg">
</details>


##### Back to [top](#table-of-contents)<hr>


## Validation

### Html validation

The W3C Markup Validation Service

<details><summary>Home</summary>
<img src="docs/validation/homevalidation.jpg">
</details>

<details><summary>Food menu</summary>
<img src="docs/validation/foodmenuvalidation.jpg">
</details>

<details><summary>Drink menu</summary>
<img src="docs/validation/drinksmenuvalidation.jpg">
</details>

<details><summary>About</summary>
<img src="docs/validation/aboutvalidation.jpg">
</details>

<details><summary>Register (Could not find the source code to fix error)</summary>
<img src="docs/validation/registervalidation.jpg">
</details>

<details><summary>Log in</summary>
<img src="docs/validation/loginvalidation.jpg">
</details>

<details><summary>Log out</summary>
<img src="docs/validation/logoutvalidation.jpg">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/bookingvalidation.jpg">
</details>

<details><summary>My bookings</summary>
<img src="docs/validation/bookingsvalidation.jpg">
</details>

<details><summary>Edit bookings</summary>
<img src="docs/validation/editvalidation.jpg">
</details>

<details><summary>Cancel bookings</summary>
<img src="docs/validation/cancelvalidation.jpg">
</details>


### CSS Validation

The W3C Jigsaw CSS Validation Service
<details><summary>Script.js</summary>
<img src="docs/validation/cssvalidation.jpg">
</details>

### PEP8 Validation

PEP8 Validation Service was used to check the code for PEP8 requirements

<hr><summary>Home</summary><hr>

<details><summary>views.py</summary>
<img src="docs/validation/homeviewspep2.jpg">
</details>

<details><summary>ulrs.py</summary>
<img src="docs/validation/homeurlspep2.jpg">
</details>



<hr><summary>Menu</summary><hr>

<details><summary>admin.py</summary>
<img src="docs/validation/menuadminpep.jpg">
</details>

<details><summary>apps.py</summary>
<img src="docs/validation/menuappspep.jpg">
</details>

<details><summary>forms.py</summary>
<img src="docs/validation/menuformspep.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/menumodelspep.jpg">
</details>

<details><summary>ulrs.py</summary>
<img src="docs/validation/menuurlspep.jpg">
</details>

<details><summary>views.py</summary>
<img src="docs/validation/menuviewspep.jpg">
</details>

<hr><summary>About</summary><hr>

<details><summary>admin.py</summary>
<img src="docs/validation/aboutadminpep.jpg">
</details>

<details><summary>apps.py</summary>
<img src="docs/validation/aboutappspep.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/aboutmodelspep.jpg">
</details>

<details><summary>tests.py</summary>
<img src="docs/validation/abouttestpep.jpg">
</details>

<details><summary>ulrs.py</summary>
<img src="docs/validation/abouturlspep.jpg">
</details>

<details><summary>views.py</summary>
<img src="docs/validation/aboutviewspep.jpg">
</details>


<hr><summary>Bookings</summary><hr>

<details><summary>admin.py</summary>
<img src="docs/validation/bookadminpep.jpg">
</details>

<details><summary>apps.py</summary>
<img src="docs/validation/bookappspep.jpg">
</details>

<details><summary>models.py</summary>
<img src="docs/validation/bookmodelspep.jpg">
</details>

<details><summary>test_models.py</summary>
<img src="docs/validation/booktestmodelspep.jpg">
</details>

<details><summary>test_ulrs.py</summary>
<img src="docs/validation/booktesturlspep.jpg">
</details>

<details><summary>test_views.py</summary>
<img src="docs/validation/booktestviewspep.jpg">
</details>

<details><summary>ulrs.py</summary>
<img src="docs/validation/bookurlspep.jpg">
</details>

<details><summary>views.py</summary>
<img src="docs/validation/bookviewspep.jpg">
</details>


### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

<details><summary>Home</summary>
<img src="docs/validation/lighthousehome.jpg">
</details>

<details><summary>Menu</summary>
<img src="docs/validation/lighthousemenu.jpg">
</details>

<details><summary>Drink menu</summary>
<img src="docs/validation/lighthousedrinkmenu.jpg">
</details>

<details><summary>Food menu</summary>
<img src="docs/validation/lighthousefoodmenu.jpg">
</details>

<details><summary>About</summary>
<img src="docs/validation/lighthouseabout.jpg">
</details>

<details><summary>Register</summary>
<img src="docs/validation/lighthouseregister.jpg">
</details>

<details><summary>Log in</summary>
<img src="docs/validation/lighthouselogin.jpg">
</details>

<details><summary>Log out</summary>
<img src="docs/validation/lighthouselogout.jpg">
</details>

<details><summary>Book a table</summary>
<img src="docs/validation/lighthousebook.jpg">
</details>

<details><summary>Bookings</summary>
<img src="docs/validation/lighthousebookings.jpg">
</details>

<details><summary>Edit booking</summary>
<img src="docs/validation/lighthouseeditbookings.jpg">
</details>

<details><summary>Cancel booking</summary>
<img src="docs/validation/lighthousecancelbookings.jpg">
</details>


### Wave

WAVE was used to test the websites accessibility.

<details><summary>Home</summary>
<img src="docs/validation/wavehome.jpg">
</details>

<details><summary>Menu</summary>
<img src="docs/validation/wavemenu.jpg">
</details>

<details><summary>Drink menu</summary>
<img src="docs/validation/wavedrinkmenu.jpg">
</details>

<details><summary>Food menu</summary>
<img src="docs/validation/wavefoodmenu.jpg">
</details>

<details><summary>About</summary>
<img src="docs/validation/waveabout.jpg">
</details>

<details><summary>Register(Could not find the source code to fix error)</summary>
<img src="docs/validation/waveregister.jpg">
</details>

<details><summary>Login</summary>
<img src="docs/validation/wavelogin.jpg">
</details>

<details><summary>Log out</summary>
<img src="docs/validation/wavelogout.jpg">
</details>

<details><summary>Book a table</summary>
<img src="docs/validation/wavebook.jpg">
</details>

<details><summary>Bookings</summary>
<img src="docs/validation/wavebookings.jpg">
</details>

<details><summary>Edit booking</summary>
<img src="docs/validation/waveeditbookings.jpg">
</details>

<details><summary>Cancel booking</summary>
<img src="docs/validation/wavecancelbookings.jpg">
</details>

## Testing

1. Manual testing
2. Automated testing

### Manual testing

1. As a User I can navigate across the site so that I can move to each feature of the site easily

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Home' link in the navigation bar | Homepage will load| Works as expected |
| Click on the 'Menus' link in the navigation bar |menu page will load| Works as expected |
| Click on the 'Menus' link in the navigation bar, select 'Food Menu' | Food menu page will load| Works as expected |
| Click on the 'Menus' link in the navigation bar, select 'Drinks Menu' | Drinks menu page will load| Works as expected |
| Click on the 'About us' link in the navigation bar | About us page will load| Works as expected |
| Click on the 'Register' link in the navigation bar | Sign up page will load| Works as expected |
| Click on the 'Login' link in the navigation bar | Login page will load| Works as expected |
| Click on the 'Logout' link in the navigation bar | Logout page will load| Works as expected |
| Click on the 'Book' link in the navigation bar | Reservations page will load| Works as expected |
| Click on the 'My Bookings' link in the navigation bar | Booking list page will load| Works as expected |
| Click on the 'My Bookings' link then the 'Edit Bookings' link  | Cancel Booking list page will load| Works as expected |
| Click on the 'My Bookings' link then the'Cancel Bookings' link  | Cancel Booking list page will load| Works as expected |


<details><summary>Home link</summary>
<img src="docs/testing/testing1home.jpg">
</details>

<details><summary>Menu link</summary>
<img src="docs/testing/testing1menu.jpg">
</details>

<details><summary>Food menu link</summary>
<img src="docs/testing/testing1menu.jpg">
<img src="docs/testing/testing1foodmenu.jpg">
</details>

<details><summary>Drink menu link</summary>
<img src="docs/testing/testing1menu.jpg">
<img src="docs/testing/testing1drinkmenu.jpg">
</details>

<details><summary>About link</summary>
<img src="docs/testing/testing1about.jpg">
</details>

<details><summary>Register link</summary>
<img src="docs/testing/testing1register.jpg">
</details>

<details><summary>Log in link</summary>
<img src="docs/testing/testing1login.jpg">
</details>

<details><summary>Log out link</summary>
<img src="docs/testing/testing1logout.jpg">
</details>

<details><summary>Book a table link</summary>
<img src="docs/testing/testing1book.jpg">
</details>

<details><summary>Bookings link</summary>
<img src="docs/testing/testing1bookings.jpg">
</details>

<details><summary>Edit booking link</summary>
<img src="docs/testing/testing1editbookings.jpg">
</details>

<details><summary>Cancel booking link</summary>
<img src="docs/testing/testing1cancelbookings.jpg">
</details>


2. As a User I can use a navbar, footer, and social icons so that I can navigate the site, access menus, and access socials

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
 | See test 1 | See test 1 | Works as expected |
 | Scroll to footer at bottom of page | find footer | Works as expected |
 | Scroll to footer at bottom of page | find social links | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing2.jpg">
</details>

3. As a User I can view the opening hours and contact details so that I know when the business is open and how to contact them via email, phone and socials

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on Any link in the navigation bar, scroll to bottom of page | Find contact details and opening hours | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing3.jpg">
</details>

4. As a User I can create a booking by selecting a date and time so that I can reserve my table

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Book' link in the navigation bar | Find the booking form on the reservations page | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing4.jpg">
</details>

5. As a User I can update my booking so that I can choose another available time and date

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From 'My Bookings' click 'Edit' on booking to be edited| Find the edit booking form loaded  | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing5.jpg">
</details>

6. As a User I can delete my booking so that I can cancel my table reservation

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From 'My Bookings' click 'Cancel' on booking to be cancelled| Find the cancel booking prompt loaded  | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing6.jpg">
</details>

7. As a user I can view my booking so that I can remind myself of the date and time I have booked

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'My Bookings' link in the navigation bar | Booking list will display all bookings made| Works as expected |

<details><summary></summary>
<img src="docs/testing/testing7.jpg">
</details>

8. As a User I can register to create an account so that my details are stored for faster booking in future.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Register' link in the navigation bar | Register an account to allow bookings to be made | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing8.jpg">
</details>

9. As a user I can login so that I can book a table

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Login' link in the navigation bar | Log in, user now able to book a table | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing9.jpg">
</details>

10. As a user I can see my login status so that I know if I am logged in or not

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| While logged in, view navigation bar | Logout button should be visible | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing10.jpg">
</details>

11. As a User I can view the site's about us page to get to know the resturant.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| As a user i can see the about page | Read the about text | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing11.jpg">
</details>


12. As a User I can view the drink menu so that I can decide wether to drink at the business.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| As a user i can see the menu page then go in the drink menu | see what drinks are available | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing12,1.jpg">
<img src="docs/testing/testing12,2.jpg">
</details>

13. As a User I can view the food menu so that I can decide wether to drink at the business.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| As a user i can see the menu page then go in the food menu | food menu | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing13,2.jpg">
<img src="docs/testing/testing13,1.jpg">
</details>

14. As a User I can not book a date in the past so that my booking is valid

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the booking page, click requested date calender icon | Calender will open with all dates from yesterday and older greyed out, cannot select | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing14.jpg">
</details>

15. As a User I can not book a table already booked so that my booking is valid and not double booked

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the bookings page, attempt to book a table and date already booked | Error message displays to say booking not possible | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing15.jpg">
</details>

16. As a Admin I can create, read, update and delete food and drinks items from the database so that we can add, remove, rename and view all our food and drinks items

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the admin page  | Enter admin login credentials, gain access to back end | Works as expected |
| Click on the  Drink Items on the left panel, select an item by id | Item Form is displayed allowing, editing and deletion, see test 12 for creation |Works as expected |

<details><summary></summary>
<img src="docs/testing/testing16.jpg">
</details>

17. As an Admin / Authorised User I can log in so that I can access the back end of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the admin page  | Enter admin login credentials, gain access to back end | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing17.jpg">
</details>

18. As an Admin / Authorised User I can manually add a booking so that I can book a table if someone phones, or emails the business

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the admin page  | Enter admin login credentials, gain access to back end | Works as expected |
| Click on the Bookings button the the left panel, select add booking | Booking form is displayed | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing18.jpg">
</details>


19. As an Admin / Authorised User I can filter bookings by date so that I can see what bookings we have for a particular day

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From the admin panel, select Bookings | Find  filters on displayed right panel of page | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing19.jpg">
</details>

20. As a Site Owner I can validate data entered into my site so that all submitted data is correct to avoid errors

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| From Booking page, make a booking with a phone number that is too short | Error message is displayed | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing20.jpg">
</details>

21. As a Site Owner I can provide a way to contact users so they can get in touch with my business

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Scroll to the bottom of all pages | See contacts | Works as expected |

<details><summary></summary>
<img src="docs/testing/testing21.jpg">
</details>


### Automated testing
* Testing was done using the built in Django module, unittest.
* Coverage was also usesd to generate a report

<details><summary>bookings, test_models.py</summary>
<img src="docs/testing/bookingmodeltest.jpg">
</details>

<details><summary>bookings, test_urls.py</summary>
<img src="docs/testing/testurls.jpg">
</details>

<details><summary>bookings, test_views.py</summary>
<img src="docs/testing/testviews.jpg">
</details>

##### Back to [top](#table-of-contents)<hr>

## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| Css not loading| The css folder was created in uppercase as CSS, renamed and fixed |
| Over bookings | Added max bookings per time slot | 
| Drinks not listing by type, wines, beers and cocktails | I needed to fix the database loop for the drinks item to specify the drink type had to be a wine to display in the wine section of the menu, and the same for beers and cocktails |
| Deleted all the files from my computer | Had to redo everything |


## Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com

2. Create an app, give it a name, and select a region

3. Conect heroku to you github repository

4. Choose buildpacks

5. Add Config Vars

6. Add procfile file web: gunicorn Yourrepository.wsgi

7. Ensure debug is set to false in the settings.py file

8. install plugins

9. use pip3 or pip freeze > requirements.txt or pip freeze > requirements.txt

10. Add localhost, and Yourrepository.herokuapp.com to the ALLOWED_HOSTS variable in settings.py

11. Run "python3 or python manage.py showmigrations" to check the status of the migrations

12. Run "python3 or python manage.py migrate" to migrate the database

13. Run "python3 or python manage.py createsuperuser" to create a super/admin user

14. if u want add automatic deploys

15. Click deploy to deploy your application to Heroku for the first time

16. Click on the link provided to access the application

17. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue



### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

## Credits

### Images

Images used were sourced from chat gpt and with the permission from OpenAI


##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

I would like to take the opportunity to thank:
* My mentor Mo Shami for his feedback, advice, and support.
* My Wife Agnes for her support, advice and help with the baby so i can take time for my project.