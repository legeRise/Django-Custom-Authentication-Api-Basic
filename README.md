This is a pretty basic api with just 3 endspoints of which one was just for test purpose so that leaves us with two

1. http://127.0.0.1:8000/api/signup
2. http://127.0.0.1:8000/api/login
3. http://127.0.0.1:8000/  -- The third one  it just returns  "checked"  

   -- host may change according to your choice of course

__________________________________________________________HOW TO GET IT RUNNING____________________________________________________________________

1. clone this repo
2. unzip it. Your will find "Api" folder open it
3. look for "manage.py", if you found it open command prompt in that folder and enter "python manage.py runserver"
4. It will be up and running

   Note: And yeah you may need postman or similar application to test it
   OR  if you want to see some interface, you can use  the basic frontend I have created in miniapp/templates
   1. signup.html
   2. login.html
  
      you can setup them up to be rendered in 'views.py' using render function.

      In simple words,
      **JUST GO TO miniapp/views.py**
      In there you will find login and signup functions, chaange the last "return" that will be JsonResponse( I guess) with  'render'
      Still you will have to make few changes as views are not primarily written to work with templates

      So best of luck
      
      
   
