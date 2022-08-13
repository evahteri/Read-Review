# Read Review

 Read Review is a website to write and publish reviews of books and read other users' reviews of books.
 The app is hosted on heroku at https://tsoha-read-review.herokuapp.com/
 App can be tested using any browser but I recommend using chrome as the app is developed using chrome as a test environment.

## State of development
[Changelog](https://github.com/evahteri/Read-Review/blob/main/documentation/changelog.md) includes the progress of all main features.
[Timesheet](https://github.com/evahteri/Read-Review/blob/main/documentation/timesheet.md) includes used hours and dates


### Latest improvements
 - Books and reviews can be searched by title
 - User can create a review from search results
 - Recent reviews on homepage
 - Books can be deleted

 ### Known flaws
 - No limit on characters in input/text fields
 - Database accepts same author/book with different uppercase/lowercase letters
 - Books cannot be searched by author
 - No messages to users when new books or authors are created

## Main features

 - ### Users
 - User can be either an admin or a user
 - Users can create a new profile with a username and a password
 - Users can sign in using the created credentials
 - Admin has more rights than a user: e.g. to delete old reviews 
 
 - ### Reviews
 - Reviews of books can be written on a form
 - Reviews are published for everyone to read
 - User must provide the author, name of the book, the written review and a star rating (out of five)
 - Reviews can be found via a search function
 
 - ### Read list
 - User can add books they are planning to read to a read list
 
 - ### Social features
 - Users can read published reviews
 
 ## Possible future features
 - "Newest reviews" are shown on the front page
 - Seeing other users' profiles to read their reviews and see their "read list"
 - Adding friends
 - Having a large database of books and authors to prevent dublicates
