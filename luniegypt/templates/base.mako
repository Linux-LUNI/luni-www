<html lang="en"><head> <title> Linux Users of Norther Illinois - ${title}</title>
 <!-- Bootstrap -->
 <link href="static/css/bootstrap.css" rel="stylesheet">
<link href='http://fonts.googleapis.com/css?family=Oleo+Script+Swash+Caps' rel='stylesheet' type='text/css'>
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <meta name="description" content="">
 <meta name="author" content="">
<base href="/" >

 <!-- Le styles -->
 <style type="text/css">
   h1 {
       font-family: 'Oleo Script Swash Caps', cursive; font-size: 48px; 
    }
   body {
     padding-top: 60px;
     padding-bottom: 40px;
   }
 </style>


</head>
<body>




    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">LUNI</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
              <li><a href="/">Home</a></li>
              <li><a href="/calendar">Calendar</a></li>
              <li><a href="/orgs">Organizations</a></li>
              <li><a href="/contactus">Contact Us</a></li>
              <li><a href="https://github.com/Linux-LUNI/luni-www">Source Code</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>


    <div class="container">

      <div class="well">
        <h1   >Linux Users of Northern Illinois</h1>
      </div>
        <p class="lead"><%block name="blockContent"/></p>

    </div>


    <div id="footer">

		<hr/>
            <!-- Place this tag where you want the +1 button to render -->
            <g:plusone annotation="inline"></g:plusone>

            <!-- Place this render call where appropriate -->
            <script type="text/javascript">
              (function() {
                var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                po.src = 'https://apis.google.com/js/plusone.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
              })();
            </script>

            <!-- Place this tag in the <head> of your document-->
            <link href="https://plus.google.com/117141677404718615863/" rel="publisher" />

            <!-- Place this tag where you want the badge to render-->
            <a href="https://plus.google.com/117141677404718615863/?prsrc=3" style="text-decoration: none;"><img src="https://ssl.gstatic.com/images/icons/gplus-32.png" width="32" height="32" style="border: 0;"/></a>

    </div>
</body>
</html>

