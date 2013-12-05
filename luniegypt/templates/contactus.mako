<%inherit file="base.mako"/>


<%block name="blockContent">
        <p>For general info please send an email to <a href="mailto:info@luni.org">info@luni.org</a></p>
    </div>
     <div class="row">
        <div class="span4">
          <h2>Mailing Lists</h2>
		    <ul>
		    <!-- Begin LUNI -->
		    <table border=0 style="padding: 5px;" cellspacing=0>
		      <tr><td style="padding-left: 5px">
		      <b>Subscribe to <a href="https://groups.google.com/group/luni-chicago/">Linux Users of Northern Illinois</a></b>
		      </td></tr>
		      <form action="http://groups.google.com/group/luni-chicago/boxsubscribe">
		      <input type=hidden name="hl" value="en">
		      <tr><td style="padding-left: 5px;">
		      Email: <input type=text name=email>
		      <input type=submit name="sub" value="Subscribe">
		      </td></tr>
		    </form>
		    </table>
		    <!-- End LUNI -->

		    <!-- LUNI Announce -->
		    <p>
		    <table border=0 style=" padding: 5px;" cellspacing=0>
		      <tr><td style="padding-left: 5px">
		      <b>Subscribe to <a href="https://groups.google.com/group/luni-announce-chicago">Linux Users of Northern Illinois announce list</a></b>
		      </td></tr>
		      <form action="http://groups.google.com/group/luni-announce-chicago/boxsubscribe">
		      <input type=hidden name="hl" value="en">
		      <tr><td style="padding-left: 5px;">
		      Email: <input type=text name=email>
		      <input type=submit name="sub" value="Subscribe">
		      </td></tr>
		    </form>
		    </table>
		    <!-- End LUNI Announce -->

		    </ul>
        </div>

         <div class="span4">
          <h2>Social Media</h2>
             <ul>
		        <li> <a href="http://www.facebook.com/pages/Linux-Users-of-Northern-Illinois/142456219162668"> Facebook Page </a> </li>
		        <li> <a href="http://www.twitter.com/luni_announce"> Twitter Feed </a> rebroadcasts content of facebookpage.</li>
		        <li> <a href="http://www.linkedin.com/groups?gid=160786&mostPopular=&trk=tyah"> LinkedIn Group </a></li>
		        <li><a href="https://plus.google.com/117141677404718615863/posts"> Google Plus Page </a></li>
		        <li> <a href="http://embed.mibbit.com/?server=irc.freenode.org&channel=%23luni&noServerNotices=true&noServerMotd=true">web-based chat client</a> (irc.freenode.org #luni)
             </ul>
        </div>
        <div class="span4">
          <h2>Archives </h2>
		    <ul>
		    <li> <a href="http://mailman.luni.org/pipermail/luni/"> Luni Archives</a> </li>
		    <li> <a href="http://mailman.luni.org/pipermail/luni-announce/"> Luni Announcements Archives</a> </li>
		    </ul>
        </div>

     </div>

</%block>
